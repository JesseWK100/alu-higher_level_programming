-- This script lists all privileges of the MySQL users 'user_0d_1' and 'user_0d_2' on the server
-- Save this script in a file named '0-privileges.sql'

-- Check if user_0d_1 exists
SELECT 'Checking if user_0d_1 exists' AS Message;
SELECT user FROM mysql.user WHERE user = 'user_0d_1' AND host = 'localhost';

-- If user_0d_1 does not exist, create the user
DROP PROCEDURE IF EXISTS create_user_0d_1;
DELIMITER //
CREATE PROCEDURE create_user_0d_1()
BEGIN
    DECLARE user_count INT;
    SELECT COUNT(*) INTO user_count FROM mysql.user WHERE user = 'user_0d_1' AND host = 'localhost';
    IF user_count = 0 THEN
        CREATE USER 'user_0d_1'@'localhost';
        GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
    END IF;
END //
DELIMITER ;
CALL create_user_0d_1();
DROP PROCEDURE create_user_0d_1;

-- Check if user_0d_2 exists
SELECT 'Checking if user_0d_2 exists' AS Message;
SELECT user FROM mysql.user WHERE user = 'user_0d_2' AND host = 'localhost';

-- If user_0d_2 does not exist, create the user
DROP PROCEDURE IF EXISTS create_user_0d_2;
DELIMITER //
CREATE PROCEDURE create_user_0d_2()
BEGIN
    DECLARE user_count INT;
    SELECT COUNT(*) INTO user_count FROM mysql.user WHERE user = 'user_0d_2' AND host = 'localhost';
    IF user_count = 0 THEN
        CREATE USER 'user_0d_2'@'localhost';
        GRANT SELECT, INSERT ON user_2_db.* TO 'user_0d_2'@'localhost';
    END IF;
END //
DELIMITER ;
CALL create_user_0d_2();
DROP PROCEDURE create_user_0d_2;

-- Show grants for users
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';

-- To execute the script, use the following command:
-- guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
-- Enter password: 
-- Note: Replace 'localhost' with your MySQL server's hostname and 'root' with your username.
