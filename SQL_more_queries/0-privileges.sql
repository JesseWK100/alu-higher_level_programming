-- This script lists all privileges of the MySQL users 'user_0d_1' and 'user_0d_2' on the server
-- Save this script in a file named '0-privileges.sql'

SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';

-- To execute the script, use the following command:
-- guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
-- Enter password: 
