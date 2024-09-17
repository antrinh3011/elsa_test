CREATE DATABASE quiz_app_db;
USE quiz_app_db;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
);

CREATE TABLE quizzes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    quiz_id VARCHAR(255) NOT NULL UNIQUE,
    quiz_name VARCHAR(255) NOT NULL
);

CREATE TABLE questions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    quiz_id INT NOT NULL,
    question_text TEXT NOT NULL,
    FOREIGN KEY (quiz_id) REFERENCES quizzes(id)
);

CREATE TABLE questionoptions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    question_id INT NOT NULL,
    optanswer TEXT NOT NULL,
    correct_answer BOOLEAN DEFAULT FALSE
    FOREIGN KEY (question_id) REFERENCES questions(id)
);

CREATE TABLE scores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    quiz_id INT NOT NULL,
    score INT DEFAULT 0,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (quiz_id) REFERENCES quizzes(id)
);
