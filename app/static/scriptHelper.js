$(document).ready(function() {
    const socket = io();
    const $useridInput = $('#userid');
    const $usernameInput = $('#username');
    const $roomInput = $('#room');
    const $userScoreInput = $('#user_score');
    const $logoutButton = $('#logout');
    const $userScoreDisplay = $('#user-score');
    const $quizForm = $('#quiz-form');
    const $userListElement = $('#user-list');

    const userid = $useridInput.val();
    const username = $usernameInput.val();
    const room = $roomInput.val();
    const score = $userScoreInput.val();

    // Handle submit answer
    $quizForm.submit(function(event) {
        event.preventDefault();
        
        let isValid = true;
        const quizID = $('#quizID').val();
        $('.error-message').text(''); 
        const selectedChoices = [];

        $('.question-group').each(function() {
            const $questionGroup = $(this);
            const $errorMessage = $questionGroup.find('.error-message');
            const $selectedRadio = $questionGroup.find('input[type="radio"]:checked');

            if ($selectedRadio.length === 0) {
                $errorMessage.text('Please select answer for this question!');
                isValid = false;
            } else {
                $errorMessage.text('');
                selectedChoices.push({
                    name: $selectedRadio.attr('name'),
                    answervalue: $selectedRadio.val(),
                    questionid: $questionGroup.data('question')
                });
            }
        });

        if (isValid) {
            $.ajax({
                url: $quizForm.attr('action'),
                method: 'POST',
                contentType: 'application/json',
                data: JSON.stringify({
                    selectedChoices: selectedChoices,
                    quiz_ID: quizID,
                    user_id: userid
                }),
                success: function(response) {
                    console.log(response)
                    socket.emit('submit_answer', {
                        'username': username,
                        'room': response.user_score.quiz_id,
                        'points': response.user_score.score
                    });
                },
                error: function(error) {
                    console.log(error);
                }
            });
        }
    });

    // Real-time using quizID as room and add customer joined to room
    if (username && room) {
        socket.emit('join', {
            'username': username,
            'room': room,
            'points': score
        });
    }

    // Real-time display user out room
    if ($logoutButton.length && username) {
        $logoutButton.click(function() {
            socket.emit('leave', { 'username': username });
        });
    }

    // Real-time display user joined
    socket.on('update_user_list', function(data) {
        $userListElement.empty();
        data.users.forEach(user => {
            if (user.username === username) {
                $userScoreDisplay.empty().text(user.points);
            }
            const message = `${user.username} access to the quiz. Point: ${user.points}`;
            $userListElement.append(`<p>${message}</p>`);
        });
    });
});
