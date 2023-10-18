-- Check if the user already exists
SELECT EXISTS (SELECT 1 FROM mysql.user WHERE user = 'user_0d_1') INTO @user_exists;

-- If the user doesn't exist, create it
IF @user_exists = 0 THEN
    CREATE USER 'user_0d_1'@'root' IDENTIFIED BY 'user_0d_1_pwd';
END IF;

-- Grant all privileges to the user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'root';
