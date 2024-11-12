-- This script prints the full description of the table 'first_table' in the specified database
-- Save this script in a file named '5-full_table.sql'

SELECT table_name, column_name, column_type, is_nullable, column_default
FROM information_schema.columns
WHERE table_schema = 'hbtn_0c_0'
AND table_name = 'first_table';

-- To execute the script, use the following command:
-- guillaume@ubuntu:~/$ cat 5-full_table.sql | mysql -hlocalhost -uroot -p <database_name>
-- Enter password: 
-- Note: Replace 'localhost' with your MySQL server's hostname, 'root' with your username, 
-- and '<database_name>' with the name of the database where 'first_table' is located.
