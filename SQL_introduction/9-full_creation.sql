-- This script creates the table 'second_table' and inserts multiple rows in the specified database
-- Save this script in a file named '9-full_creation.sql'

CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

INSERT INTO second_table (id, name, score)
VALUES 
    (1, 'John', 10),
    (2, 'Alex', 3),
    (3, 'Bob', 14),
    (4, 'George', 8);

-- To execute the script, use the following command:
-- guillaume@ubuntu:~/$ cat 9-full_creation.sql | mysql -hlocalhost -uroot -p <database_name>
-- Enter password: 
-- Note: Replace 'localhost' with your MySQL server's hostname, 'root' with your username, 
-- and '<database_name>' with the name of the database where 'second_table' is located.
