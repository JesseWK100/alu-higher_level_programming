-- This script counts the number of records with id = 89 in the table 'first_table'
-- Save this script in a file named '8-count_89.sql'

SELECT COUNT(*) FROM first_table WHERE id = 89;

-- To execute the script, use the following command:
-- guillaume@ubuntu:~/$ cat 8-count_89.sql | mysql -hlocalhost -uroot -p <database_name>
-- Enter password: 
-- Note: Replace 'localhost' with your MySQL server's hostname, 'root' with your username, 
-- and '<database_name>' with the name of the database where 'first_table' is located.
