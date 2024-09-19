from flask_socketio import SocketIO, emit, join_room, leave_room

active_users = {}

def setup_socketio(app):

    socketio = SocketIO(app)

    @socketio.on('join')
    def handle_join(data):
        quiz_id = data['room']
        username = data['username']
        points = data.get('points', 0)
        roomid = f"room_{quiz_id}"
        if username and quiz_id:
            #If the user isn't exsited,init there infomation
            if username not in active_users:
                active_users[username] = {'rooms': {}}

            #If the user room isn't in list,init the zero point for that room
            if roomid not in active_users[username]['rooms']:
                active_users[username]['rooms'][roomid] = points  
            #John the room
            join_room(roomid)

        # Update the user list,room and their points
        room_users = [{'username': user, 'points': data['rooms'][roomid]} 
                        for user, data in active_users.items() 
                            if roomid in data['rooms']]
        room_users_sorted = sorted(room_users, key=lambda x: x['points'], reverse=True)
        # Broadcast an event to update the room's user list and scores
        emit('update_user_list', {'users': room_users_sorted}, room=roomid)

    @socketio.on('leave')
    def handle_leave(data):
        username = data['username']
        quiz_id = data.get('room')
        roomid = f"room_{quiz_id}"
        if username:
            if quiz_id and username in active_users:
                if roomid in active_users[username]['rooms']:
                # Leave and remove room in list
                    leave_room(roomid)
                    del active_users[username]['rooms'][roomid]  
                # Remove the user if they don't join any rooms
                if not active_users[username]['rooms']:
                    del active_users[username]

            else:
                if username in active_users:
                    rooms = list(active_users[username]['rooms'].keys()) 
                    for room in rooms:
                        leave_room(room)
                    del active_users[username]

            room_users = [{'username': user, 'points': data['rooms'].get(roomid, 0)} 
                            for user, data in active_users.items() 
                                if roomid in data['rooms']]
            
            room_users_sorted = sorted(room_users, key=lambda x: x['points'], reverse=True)
            # Broadcast an event to update the room's user list and scores
            emit('update_user_list', {'users': room_users_sorted}, room=roomid)
                    

    @socketio.on('submit_answer')
    def handle_submit_answer(data):
        username = data.get('username')
        quiz_id = data.get('room')
        points = data.get('points')
        roomid = f"room_{quiz_id}"
        print(f"Username : {username}, quiz_id : {quiz_id}, points : {points}")
        if username and quiz_id is not None and points is not None:
            # Update user points
            if username in active_users and roomid in active_users[username]['rooms']:
                active_users[username]['rooms'][roomid] = points
            print(f"Updated active_users: {active_users}")
            room_users = [{'username': user, 'points': data['rooms'].get(roomid, 0)} 
                            for user, data in active_users.items() 
                                if roomid in data['rooms']]
            print(f"Updated room_users: {room_users}")
            join_room(roomid)
            # Broadcast an event to update the room's user list and scores
            room_users_sorted = sorted(room_users, key=lambda x: int(x['points']), reverse=True)
            emit('update_user_list', {'users': room_users_sorted}, room=roomid)
			
            

