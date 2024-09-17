document.addEventListener("DOMContentLoaded", function () {
    const submitButton = document.getElementById('submit-answer');
    const answerInput = document.getElementById('answer');
    const userScore = document.getElementById('user-score');
    const leaderboard = document.getElementById('leaderboard');

    const userId = prompt("Enter your user ID:");
    const ws = new WebSocket(`ws://localhost:8000/ws/${quizId}`);

    ws.onmessage = function (event) {
        const data = JSON.parse(event.data);
        userScore.textContent = data.score;

        leaderboard.innerHTML = "";
        data.leaderboard.forEach(function (entry) {
            const li = document.createElement('li');
            li.textContent = `User ${entry.user_id}: ${entry.score} points`;
            leaderboard.appendChild(li);
        });
    };

    submitButton.addEventListener('click', function () {
        const answer = answerInput.value;
        ws.send(JSON.stringify({ user_id: userId, answer: answer }));
        answerInput.value = "";
    });
});
