-- 11. No table for a meeting
-- Write a SQL script that creates a function SafeDiv that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.
DROP VIEW IF EXISTS need_meeting;
CREATE VIEW need_meeting AS
SELECT name FROM students
WHERE
    score < 80 AND
    (last_meeting IS NULL
        OR
    last_meeting < ADDDATE(CURDATE(), interval -1 MONTH));