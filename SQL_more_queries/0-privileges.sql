-- Step 1: Create user_0d_1 and grant all root-level privileges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Step 2: Create user_0d_2 and grant SELECT and INSERT privileges on user_2_db
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
GRANT SELECT, INSERT ON user_2_db.* TO 'user_0d_2'@'localhost';

-- Apply changes
FLUSH PRIVILEGES;

-- Step 3: List privileges for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Step 4: List privileges for user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';
