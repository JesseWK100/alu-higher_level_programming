-- This script removes all records with a score <= 5 in the table 'second_table'
-- Save this script in a file named '13-change_class.sql'

DELETE FROM second_table
WHERE score <= 5;

-- To execute the script, use the following command:
-- guillaume@ubuntu:~/$ cat 13-change_class.sql | mysql -hlocalhost -uroot -p <database_name>
-- Enter password: 
-- Note: Replace 'localhost' with your MySQL server's hostname, 'root' with your username, 
-- and '<database_name>' with the name of the database where 'second_table' is located.
