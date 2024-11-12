-- This script lists the number of records with the same score in the table 'second_table'
-- Results display the score and the number of records for each score with the label 'number'
-- The list is sorted by the number of records (descending)
-- Save this script in a file named '15-groups.sql'

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;

-- To execute the script, use the following command:
-- guillaume@ubuntu:~/$ cat 15-groups.sql | mysql -hlocalhost -uroot -p <database_name>
-- Enter password: 
-- Note: Replace 'localhost' with your MySQL server's hostname, 'root' with your username, 
-- and '<database_name>' with the name of the database where 'second_table' is located.
