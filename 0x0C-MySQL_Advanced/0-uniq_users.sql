-- 0. We are all unique!
-- Write a SQL script that creates a table users following these requirements
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    PRIMARY KEY(id)
);