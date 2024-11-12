-- This script lists all records of the table 'second_table' in the specified database
-- It does not list rows without a name value
-- Results display both the score and the name (in this order)
-- Records are listed by descending score
-- Save this script in a file named '16-no_link.sql'

SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;

-- To execute the script, use the following command:
-- guillaume@ubuntu:~/$ cat 16-no_link.sql | mysql -hlocalhost -uroot -p <database_name>
-- Enter password: 
-- Note: Replace 'localhost' with your MySQL server's hostname, 'root' with your username, 
-- and '<database_name>' with the name of the database where 'second_table' is located.

