-- This script creates a table called first_table in the specified database
-- Save this script in a file named '4-first_table.sql'

CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);

-- To execute the script, use the following command:
-- guillaume@ubuntu:~/$ cat 4-first_table.sql | mysql -hlocalhost -uroot -p <database_name>
-- Enter password: 
-- Note: Replace 'localhost' with your MySQL server's hostname, 'root' with your username, 
-- and '<database_name>' with the name of the database where you want to create the table.
