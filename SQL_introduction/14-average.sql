-- This script computes the score average of all records in the table 'second_table'
-- The result column name will be 'average'
-- Save this script in a file named '14-average.sql'

SELECT AVG(score) AS average FROM second_table;

-- To execute the script, use the following command:
-- guillaume@ubuntu:~/$ cat 14-average.sql | mysql -hlocalhost -uroot -p <database_name>
-- Enter password: 
-- Note: Replace 'localhost' with your MySQL server's hostname, 'root' with your username, 
-- and '<database_name>' with the name of the database where 'second_table' is located.
