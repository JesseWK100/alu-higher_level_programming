-- This script creates the MySQL server user 'user_0d_1' with all privileges
-- and sets the password to 'user_0d_1_pwd'
-- If the user 'user_0d_1' already exists, the script will not fail
-- Save this script in a file named '1-create_user.sql'

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- To execute the script, use the following command:
-- guillaume@ubuntu:~/$ cat 1-create_user.sql | mysql -hlocalhost -uroot -p
-- Enter password: 
-- Note: Replace 'localhost' with your MySQL server's hostname and 'root' with your username.
