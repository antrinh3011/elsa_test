
-- ALTER TABLE questionoptions    
-- MODIFY optanswer TEXT;  
INSERT INTO questionoptions (question_id, optanswer, correct_answer) VALUES 
-- Math Basics Quiz
-- Question 1: What is 5 + 7?
(1, '12', TRUE),
(1, '10', FALSE),
(1, '14', FALSE),
(1, '15', FALSE),

-- Question 2: What is the square root of 16?
(2, '4', TRUE),
(2, '5', FALSE),
(2, '6', FALSE),
(2, '7', FALSE),

-- Question 3: What is 9 * 8?
(3, '72', TRUE),
(3, '64', FALSE),
(3, '81', FALSE),
(3, '90', FALSE),

-- History of Computers Quiz
-- Question 1: Who is considered the father of computers?
(4, 'Charles Babbage', TRUE),
(4, 'Alan Turing', FALSE),
(4, 'Bill Gates', FALSE),
(4, 'Steve Jobs', FALSE),

-- Question 2: When was the first computer virus discovered?
(5, '1983', TRUE),
(5, '1975', FALSE),
(5, '1991', FALSE),
(5, '2000', FALSE),

-- Question 3: What was the first personal computer?
(6, 'Altair 8800', TRUE),
(6, 'IBM PC', FALSE),
(6, 'Apple II', FALSE),
(6, 'Commodore 64', FALSE),

-- World Capitals Quiz
-- Question 1: What is the capital of Japan?
(7, 'Tokyo', TRUE),
(7, 'Osaka', FALSE),
(7, 'Kyoto', FALSE),
(7, 'Hiroshima', FALSE),

-- Question 2: What is the capital of Canada?
(8, 'Ottawa', TRUE),
(8, 'Toronto', FALSE),
(8, 'Vancouver', FALSE),
(8, 'Montreal', FALSE),

-- Question 3: What is the capital of Brazil?
(9, 'Brasília', TRUE),
(9, 'Rio de Janeiro', FALSE),
(9, 'São Paulo', FALSE),
(9, 'Salvador', FALSE),

-- Biology Basics Quiz
-- Question 1: What is the basic unit of life?
(10, 'Cell', TRUE),
(10, 'Tissue', FALSE),
(10, 'Organ', FALSE),
(10, 'Organism', FALSE),

-- Question 2: Which organ is responsible for pumping blood?
(11, 'Heart', TRUE),
(11, 'Lung', FALSE),
(11, 'Kidney', FALSE),
(11, 'Liver', FALSE),

-- Question 3: What is the powerhouse of the cell?
(12, 'Mitochondria', TRUE),
(12, 'Nucleus', FALSE),
(12, 'Ribosome', FALSE),
(12, 'Endoplasmic Reticulum', FALSE),

-- Physics Quiz for Beginners
-- Question 1: What is the unit of force?
(13, 'Newton', TRUE),
(13, 'Joule', FALSE),
(13, 'Watt', FALSE),
(13, 'Pascal', FALSE),

-- Question 2: What is the speed of light in a vacuum?
(14, '299,792,458 m/s', TRUE),
(14, '150,000,000 m/s', FALSE),
(14, '300,000,000 m/s', FALSE),
(14, '299,792,000 m/s', FALSE),

-- Question 3: Who formulated the law of gravitation?
(15, 'Isaac Newton', TRUE),
(15, 'Albert Einstein', FALSE),
(15, 'Galileo Galilei', FALSE),
(15, 'Nikola Tesla', FALSE),

-- Chemistry Reactions Quiz
-- Question 1: What is the chemical formula for water?
(16, 'H2O', TRUE),
(16, 'CO2', FALSE),
(16, 'NaCl', FALSE),
(16, 'O2', FALSE),

-- Question 2: What is the pH value of pure water?
(17, '7', TRUE),
(17, '5', FALSE),
(17, '9', FALSE),
(17, '10', FALSE),

-- Question 3: Which element is represented by the symbol Na?
(18, 'Sodium', TRUE),
(18, 'Neon', FALSE),
(18, 'Nickel', FALSE),
(18, 'Nitrogen', FALSE),

-- Space Exploration Quiz
-- Question 1: Who was the first human to travel into space?
(19, 'Yuri Gagarin', TRUE),
(19, 'Neil Armstrong', FALSE),
(19, 'Buzz Aldrin', FALSE),
(19, 'John Glenn', FALSE),

-- Question 2: What was the name of the first satellite launched into space?
(20, 'Sputnik 1', TRUE),
(20, 'Explorer 1', FALSE),
(20, 'Apollo 11', FALSE),
(20, 'Hubble', FALSE),

-- Question 3: Which planet is known as the Red Planet?
(21, 'Mars', TRUE),
(21, 'Jupiter', FALSE),
(21, 'Saturn', FALSE),
(21, 'Venus', FALSE),

-- Famous Landmarks Quiz
-- Question 1: Where is the Eiffel Tower located?
(22, 'Paris', TRUE),
(22, 'London', FALSE),
(22, 'Berlin', FALSE),
(22, 'New York', FALSE),

-- Question 2: What is the name of the ancient pyramid in Egypt?
(23, 'Great Pyramid of Giza', TRUE),
(23, 'Pyramid of the Sun', FALSE),
(23, 'Machu Picchu', FALSE),
(23, 'Chichen Itza', FALSE),

-- Question 3: Which landmark is known as the Statue of Liberty?
(24, 'New York City', TRUE),
(24, 'Los Angeles', FALSE),
(24, 'Washington D.C.', FALSE),
(24, 'San Francisco', FALSE),

-- Movie Trivia Quiz
-- Question 1: Who directed the movie "Titanic"?
(25, 'James Cameron', TRUE),
(25, 'Steven Spielberg', FALSE),
(25, 'Martin Scorsese', FALSE),
(25, 'Ridley Scott', FALSE),

-- Question 2: Which movie won the Oscar for Best Picture in 1994?
(26, 'Forrest Gump', TRUE),
(26, 'Pulp Fiction', FALSE),
(26, 'Shawshank Redemption', FALSE),
(26, 'The Lion King', FALSE),

-- Question 3: What is the name of the fictional African country in "Black Panther"?
(27, 'Wakanda', TRUE),
(27, 'Zamunda', FALSE),
(27, 'Elbonia', FALSE),
(27, 'Genosha', FALSE),

-- Music Theory Quiz
-- Question 1: What is the term for the distance between two notes?
(28, 'Interval', TRUE),
(28, 'Chord', FALSE),
(28, 'Scale', FALSE),
(28, 'Tempo', FALSE),

-- Question 2: What is the musical symbol for a sharp note?
(29, '♯', TRUE),
(29, '♭', FALSE),
(29, '♮', FALSE),
(29, '♩', FALSE),

-- Question 3: Which scale is made up of seven notes?
(30, 'Major Scale', TRUE),
(30, 'Minor Scale', FALSE),
(30, 'Chromatic Scale', FALSE),
(30, 'Pentatonic Scale', FALSE);