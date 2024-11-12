-- This script creates the MySQL server user 'user_0d_1' with all privileges
-- and sets the password to 'user_0d_1_pwd'
-- If the user 'user_0d_1' already exists, the script will not fail
-- Save this script in a file named '1-create_user.sql'

-- Check if user_0d_1 exists
SELECT 'Checking if user_0d_1 exists' AS Message;
SELECT user FROM mysql.user WHERE user = 'user_0d_1' AND host = 'localhost';

-- If user_0d_1 does not exist, create the user and grant privileges
DELIMITER //
CREATE PROCEDURE create_user_0d_1()
BEGIN
    DECLARE user_count INT;
    SELECT COUNT(*) INTO user_count FROM mysql.user WHERE user = 'user_0d_1' AND host = 'localhost';
    IF user_count = 0 THEN
        CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
        GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
    END IF;
END //
DELIMITER ;
CALL create_user_0d_1();
DROP PROCEDURE create_user_0d_1;

-- To execute the script, use the following command:
-- guillaume@ubuntu:~/$ cat 1-create_user.sql | mysql -hlocalhost -uroot -p
-- Enter password: 
-- Note: Replace 'localhost' with your MySQL server's hostname and 'root' with your username.
