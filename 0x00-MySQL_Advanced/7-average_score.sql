-- SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student. Note: An average score can be a decimal
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE avg_score FLOAT;
    SELECT  AVG(score) INTO avg_score FROM users
    JOIN corrections ON users.id = corrections.user_id
    WHERE users.id = user_id;
    UPDATE users SET average_score = avg_score WHERE users.id = user_id;
    
END $$
DELIMITER ;
