-- This script updates the score of Bob to 10 in the table 'second_table'
-- Save this script in a file named '12-no_cheating.sql'

UPDATE second_table
SET score = 10
WHERE name = 'Bob';

-- To execute the script, use the following command:
-- guillaume@ubuntu:~/$ cat 12-no_cheating.sql | mysql -hlocalhost -uroot -p <database_name>
-- Enter password: 
-- Note: Replace 'localhost' with your MySQL server's hostname, 'root' with your username, 
-- and '<database_name>' with the name of the database where 'second_table' is located.
