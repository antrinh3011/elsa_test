from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.models import User, Quiz, Question, QuestionOption, Score
from app.quizhelper import *
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        user = User.query.filter_by(username=username).first()
        if not user:
            # Create a new user if they don't exist
            user = User(username=username)
            db.session.add(user)
            db.session.commit()
            
        session['user_id'] = user.id 
        session['username'] = user.username
    if session.get('username'):
        quizzes = get_quizzes()
        return render_template('list_quizzes.html',quizzes = quizzes,username=session.get('username'))
    else:
        return redirect(url_for('main.index'))
     
    

@main_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    return redirect(url_for('main.index'))

@main_bp.route('/questions/<int:quiz_id>', methods=['GET'])
def questions(quiz_id: str):
    questions_list = get_questions(quiz_id)
    return render_template('question.html', questions=questions_list)

@main_bp.route('/submit_answer', methods=['POST'])
def submit_answer():
    question_id = request.form['question_id']
    answer = request.form['answer']
    question = Question.query.get_or_404(question_id)
    correct_option = QuestionOption.query.filter_by(question_id=question_id, correct_answer=True).first()
    user_id = session.get('user_id')
    if correct_option and answer == correct_option.optanswer:
        score = Score.query.filter_by(user_id=user_id, quiz_id=question.quiz_id).first()
        if not score:
            score = Score(user_id=user_id, quiz_id=question.quiz_id, score=0)
            db.session.add(score)
        score.score += 1
        db.session.commit()
    return redirect(url_for('main.index'))

@main_bp.route('/scores')
def scores():
    all_scores = Score.query.all()
    return render_template('score.html', scores=all_scores)
