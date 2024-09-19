from flask import Blueprint, render_template, request, redirect, url_for, session ,jsonify,make_response
from app import db
from app.models import User,Score
from app.quizhelper import *
import uuid

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/quizlist', methods=['GET', 'POST'])
def quizlist():
    user = None
    if request.method == 'POST':
        username = request.form.get('username')
        if username:
            user = User.query.filter_by(username=username).first()
            if not user:
                user = User(username=username)
                db.session.add(user)
                db.session.commit()
            session['user_id'] = user.id
        else:
            return redirect(url_for('main.index'))
    
    user_id = session.get('user_id')
    if user_id:
        user = User.query.get(user_id) 
        quizzes = get_quizzes()
        return render_template('list_quizzes.html', quizzes=quizzes, loginuser = user)
    else:
        return redirect(url_for('main.index'))
     
@main_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('main.index'))

#Get question list by quiz_id
@main_bp.route('/questions/<int:user_id>/<int:quiz_id>', methods=['GET'])
def questions(user_id:str,quiz_id: str):
    questions_list = get_questions(quiz_id)
    if user_id:
        user = User.query.get(user_id)
        user_scores = [score for score in user.scores if score.quiz_id == quiz_id]
        first_score = user_scores[0] if user_scores else {'quiz_id':quiz_id,'score':0}
        return render_template('question.html', questions=questions_list,loginuser = user,user_score=first_score)
    return redirect(url_for('main.index'))

#Submit answer
@main_bp.route('/submit_answer', methods=['POST'])
def submit_answer():
    if request.method == 'POST':
        try:    
            data = request.json  
            selected_choices = data.get('selectedChoices', [])
            quiz_id = data.get('quiz_ID')
            user_id = data.get('user_id')
            points = 0
            for anwser in selected_choices:
                points += check_answer(anwser['questionid'],anwser['answervalue'])
            #Insert point to db
            user_score = add_user_score(int(quiz_id),user_id,points)
            #emit score here
            return jsonify({'success': True, 'user_score': user_score.to_dict()}), 200
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)}), 500

@main_bp.route('/scores')
def scores():
    all_scores = Score.query.all()
    return render_template('score.html', scores=all_scores)
