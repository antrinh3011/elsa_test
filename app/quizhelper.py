from flask import jsonify
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
                "quiz_id": question.quiz_id,
                "question_text": question.question_text,
                "options": [{"optanswer": option.optanswer, "correct_answer": option.correct_answer} for option in question_options]
            })
        
        return questions_list
    
# async def check_answer(db: AsyncSession, 
#                        quiz_id: int, 
#                        answer: str):
#     # Giả sử mỗi quiz chỉ có 1 câu hỏi hiện tại cho đơn giản
#     async with db.begin():
#         question = await db.execute(select(Question).filter(Question.quiz_id == quiz_id))
#         result = question.scalars().first()
#         if result.correct_answer.lower() == answer.lower():
#             return True
#         return False
    

# async def update_score(db: AsyncSession, 
#                        quiz_id: int, 
#                        user_id: int, 
#                        iscorrect: bool):
#     async with db.begin():
#         score_entry = await db.execute(select(Score).filter(Score.quiz_id == quiz_id, Score.user_id == user_id))
#         result = score_entry.scalars().first()
#         if iscorrect:
#             result.score += 10  # Cộng thêm điểm nếu đúng
#             db.commit()
#         return result.score
    
# # Lấy bảng xếp hạng hiện tại
# async def get_leaderboard(db: AsyncSession, 
#                           quiz_id: str):
#     async with db.begin():
#         scores = await db.execute(select(Score).filter(Score.quiz_id == quiz_id).order_by(Score.score.desc()))
#         results = scores.scalars().all()
#         return [{"user_id": item.user_id, "score": item.score} for item in results]
    