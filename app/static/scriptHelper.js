$(document).ready(function() {
    var socket = io();
    //Get user data from base.html
    var username = $('#username').val();
    var room = $('#room').val();
    var score = $('#user_score').val();
    var logout = $('#logout');
    var user_score = $('#user-score');


    //Handle submit answer
    $('#quiz-form').submit(function(event) {
        event.preventDefault();
        var isValid = true;
        var quiz_ID = $('#quizID').val();
        $('.error-message').text(''); 
        var selectedChoices = [];
        
        $('.question-group').each(function() {
            var questionGroup = $(this);
            var errorMessage = questionGroup.find('.error-message');
            if (questionGroup.find('input[type="radio"]:checked').length === 0) {
                errorMessage.text('Please select anwser for this question!');
                isValid = false;
            } else {
                errorMessage.text(''); 
                var selectedRadio = questionGroup.find('input[type="radio"]:checked');
                selectedChoices.push({
                    name: selectedRadio.attr('name'),
                    answervalue: selectedRadio.val(),
                    questionid: questionGroup.data('question')
                });
            }
        });

        if (isValid) {
            $.ajax({
                url:  $(this).attr('action'), 
                method: 'POST',
                contentType: 'application/json',
                data: JSON.stringify({
                    'selectedChoices': selectedChoices,
                    'quiz_ID': quiz_ID
                }),
                success: function(response) {
                    //console.log(response);
                    //Handle real time submit answer to update new score
                    socket.emit('submit_answer', {username: username,
                                                    room: response.user_score.quiz_id,
                                                    points: response.user_score.score}); // socket.js >> @socketio.on('submit_answer')
                },
                error: function(error) {
                    console.log(error);
                }
            });
        }
       
    });

    
    //Real time using quizID is room and add customer joined to room
    if(username && room) {
        socket.emit('join', {username: username, room: room,points:score}); // socket.js >> @socketio.on('join')
    }
    //Real time display user out room : socket.js >> @socketio.on('join')
    if(logout && username) {
        logout.click(function() {
            socket.emit('leave', {username: username});
        });
    }
    //Real time display user joined
    socket.on('update_user_list', function(data) { // socket.js >> emit('update_user_list')
        var $userListElement = $('#user-list');
        $userListElement.empty();
        $.each(data.users, function(index, user) {
            if(user['username'] == username) {
                user_score.empty();
                user_score.append(`${user['points']}`);
            }
            var message = user['username'] + ' access to the quiz. Point : ' + user['points'];
            $userListElement.append(`<p>${message}</p>`);
        });
        
    });
    
    
});
