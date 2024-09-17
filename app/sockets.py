from flask_socketio import SocketIO, emit
from app import db
from app.models import Score, User

def setup_socketio(app):
    socketio = SocketIO(app)

    @socketio.on('submit_answer')
    def handle_submit_answer(data):
        user_id = data['user_id']
        quiz_id = data['quiz_id']
        answer = data['answer']
        question_id = data['question_id']
        
        # Kiểm tra câu trả lời và cập nhật điểm số
        # Lưu điểm số mới vào cơ sở dữ liệu
        # Cập nhật điểm số của người dùng
        # Lấy điểm số mới nhất
        score = Score.query.filter_by(user_id=user_id, quiz_id=quiz_id).first()
        if score:
            score.score += 1  # Cập nhật điểm số (thay đổi logic nếu cần)
        else:
            score = Score(user_id=user_id, quiz_id=quiz_id, score=1)
            db.session.add(score)
        
        db.session.commit()
        
        # Gửi dữ liệu bảng xếp hạng đến tất cả các client
        all_scores = Score.query.all()
        scores = [
            {'username': User.query.get(score.user_id).username, 'score': score.score}
            for score in all_scores
        ]
        emit('update_leaderboard', {'scores': scores}, broadcast=True)
