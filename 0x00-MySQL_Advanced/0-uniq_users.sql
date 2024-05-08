-- Create holberton database
CREATE DATABASE IF NOT EXISTS holberton;
CREATE TABLE IF NOT EXISTS holberton.users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL
);
