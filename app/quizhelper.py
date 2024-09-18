from app.models import *

def get_quizzes():
        quizzes = Quiz.query.all()
        quiz_list = []
        for quiz in quizzes:
            quiz_data = {
                'id': quiz.id,
                'quiz_id': quiz.quiz_id,
                'quiz_name': quiz.quiz_name
            }
            quiz_list.append(quiz_data)
        
        return quiz_list
    
def get_questions(quiz_id : str):
        question_list = Question.query.filter(Question.quiz_id == quiz_id).all()
        if not question_list:
            return {"error": "Questions not found"}
        # Prepare the output
        questions_list = []
        for question in question_list:
            question_options = QuestionOption.query.filter(QuestionOption.question_id == question.id).all()
            questions_list.append({
                "question_id" : question.id,
                "quiz_id": question.quiz_id,
                "question_text": question.question_text,
                "options": [{"optanswer": option.optanswer} for option in question_options]
            })
        
        return questions_list
    
def check_answer(question_id: int,answer: str):
    # Assume that only one correct anwser
    question_option = QuestionOption.query.filter(QuestionOption.question_id == question_id,
                                                  QuestionOption.optanswer == answer).first()
    if question_option:
        if question_option.correct_answer == True:
             return 10
    return 0


def add_user_score(quiz_id: int, 
                user_id: int, 
                points: int):
        score_entry = Score.query.filter(Score.user_id == user_id,
                                        Score.quiz_id == quiz_id).first()
        
        if not score_entry:
            user_score = Score(user_id=user_id,
                               quiz_id=quiz_id,
                               score=points)
            db.session.add(user_score)
            db.session.commit() 
            return user_score
        else:
            score_entry.score = points
            db.session.commit() 
        return score_entry
    