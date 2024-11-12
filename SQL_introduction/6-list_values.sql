-- This script lists all rows of the table 'first_table' in the specified database
-- Save this script in a file named '6-list_values.sql'

SELECT * FROM first_table;

-- To execute the script, use the following command:
-- guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p <database_name>
-- Enter password: 
-- Note: Replace 'localhost' with your MySQL server's hostname, 'root' with your username, 
-- and '<database_name>' with the name of the database where 'first_table' is located.
