from flask_socketio import SocketIO, emit, join_room, leave_room
from flask import session
from app.models import Score, User

active_users = {}

def setup_socketio(app):

    socketio = SocketIO(app)

    @socketio.on('join')
    def handle_join(data):
        quiz_id = data['room']
        username = data['username']
        points = data.get('points', 0)
        if username and quiz_id:
            # Nếu người dùng chưa tồn tại, khởi tạo thông tin cho họ
            if username not in active_users:
                active_users[username] = {'rooms': {}}

            # Nếu room chưa có trong danh sách, khởi tạo điểm số cho room đó
            if quiz_id not in active_users[username]['rooms']:
            # Điểm khởi tạo là 0
                active_users[username]['rooms'][quiz_id] = points  
            # Tham gia room
            join_room(quiz_id)

        # Cập nhật danh sách người dùng và điểm số trong room
        room_users = [{'username': user, 'points': data['rooms'][quiz_id]} 
                        for user, data in active_users.items() 
                            if quiz_id in data['rooms']]

        # Phát sự kiện để cập nhật danh sách người dùng và điểm số trong room
        emit('update_user_list', {'users': room_users}, room=quiz_id)

    @socketio.on('leave')
    def handle_leave(data):
        username = data['username']
        quiz_id = data.get('room')  # Sử dụng get để lấy room hoặc None nếu không truyền vào

        if username:
        # Nếu room được truyền vào, rời khỏi room đó
            if quiz_id and username in active_users:
                if quiz_id in active_users[username]['rooms']:
                    leave_room(quiz_id)
                    del active_users[username]['rooms'][quiz_id]  # Xóa room đó khỏi danh sách

                # Nếu người dùng không còn tham gia phòng nào nữa, xóa họ khỏi danh sách
                if not active_users[username]['rooms']:
                    del active_users[username]

            # Nếu không có room nào được truyền vào, rời khỏi tất cả các room
            else:
                if username in active_users:
                    rooms = list(active_users[username]['rooms'].keys())  # Lấy danh sách các quiz_id
                    for room in rooms:
                        leave_room(room)
                    del active_users[username]

            # Cập nhật danh sách người dùng trong room
            room_users = [{'username': user, 'points': data['rooms'].get(quiz_id, 0)} 
                            for user, data in active_users.items() 
                                if quiz_id in data['rooms']]
            
            emit('update_user_list', {'users': room_users}, room=quiz_id)
                    
    # @socketio.on('connect')
    # def handle_connect():
    #     username = session.get('username')
    #     quiz_id = session.get('quiz_id')
    #     if username and quiz_id:
    #         if quiz_id not in active_users:
    #             active_users[quiz_id] = []
    #         if username not in active_users[quiz_id]:
    #             active_users[quiz_id].append(username)
            
    #         join_room(quiz_id)
    #         emit('user_joined', {'users': active_users[quiz_id]}, room=quiz_id)

    # @socketio.on('disconnect')
    # def handle_disconnect():
    #     username = session.get('username', '')
    #     quiz_id = session.get('quiz_id', '')

    #     if quiz_id and username:
    #         if username in active_users.get(quiz_id, []):
    #             active_users[quiz_id].remove(username)
    #             emit('user_joined', {'users': active_users[quiz_id]}, room=quiz_id)

    @socketio.on('submit_answer')
    def handle_submit_answer(data):
        username = data.get('username')
        quiz_id = data.get('room')
        points = data.get('points')

        #print(f"Username : {username}, quiz_id : {quiz_id}, points : {points}")

        if username and quiz_id is not None and points is not None:
            # Cập nhật điểm số của người dùng trong active_users
            if username in active_users:
                active_users[username]['rooms'][quiz_id] = points
            else:
                active_users[username] = {'rooms': {quiz_id: points}}

            # Cập nhật danh sách người dùng và điểm số trong room
            room_users = [{'username': user, 'points': data['rooms'].get(quiz_id, 0)} 
                            for user, data in active_users.items() 
                                if quiz_id in data['rooms']]
            print(f"Updated room_users: {room_users}")

            # Phát sự kiện để cập nhật danh sách người dùng và điểm số trong room
            join_room(quiz_id)
            emit('update_user_list', {'users': room_users}, room=quiz_id)
            
            


    # def update_leaderboard(quiz_id):
    #     # Cập nhật bảng xếp hạng dựa trên điểm số mới
    #     leaderboard = sorted(
    #         [{'username': user, 'points': data['rooms'].get(quiz_id, 0)} 
    #         for user, data in active_users.items() if quiz_id in data['rooms']], 
    #         key=lambda x: x['points'], 
    #         reverse=True
    #     )
        
        # Phát sự kiện để cập nhật bảng xếp hạng cho tất cả người dùng trong phòng
        #emit('update_leaderboard', {'leaderboard': leaderboard}, room=quiz_id)
