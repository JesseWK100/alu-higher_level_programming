-- This script lists all records of the table 'second_table' in the specified database
-- Results display both the score and the name (in this order)
-- Records are ordered by score (top first)
-- Save this script in a file named '10-top_score.sql'

SELECT score, name FROM second_table
ORDER BY score DESC;

-- To execute the script, use the following command:
-- guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p <database_name>
-- Enter password: 
-- Note: Replace 'localhost' with your MySQL server's hostname, 'root' with your username, 
-- and '<database_name>' with the name of the database where 'second_table' is located.
