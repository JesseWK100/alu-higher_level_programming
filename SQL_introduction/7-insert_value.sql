-- This script inserts a new row into the table 'first_table' in the specified database
-- Save this script in a file named '7-insert_value.sql'

INSERT INTO first_table (id, name)
VALUES (89, 'Best School');

-- To execute the script, use the following command:
-- guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p <database_name>
-- Enter password: 
-- Note: Replace 'localhost' with your MySQL server's hostname, 'root' with your username, 
-- and '<database_name>' with the name of the database where 'first_table' is located.
