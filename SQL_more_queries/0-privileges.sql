-- This script creates the users 'user_0d_1' and 'user_0d_2', grants privileges,
-- and lists all privileges of the MySQL users 'user_0d_1' and 'user_0d_2' on the server
-- Save this script in a file named '0-privileges.sql'

CREATE USER 'user_0d_1'@'localhost';
CREATE USER 'user_0d_2'@'localhost';

GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
GRANT SELECT, INSERT ON user_2_db.* TO 'user_0d_2'@'localhost';

SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';

-- To execute the script, use the following command:
-- guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
-- Enter password: 
-- Note: Replace 'localhost' with your MySQL server's hostname and 'root' with your username.
