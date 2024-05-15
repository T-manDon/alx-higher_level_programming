-- this script creates MySQL server and user user_0d_1.
   -- user_0d_1 granted all privileges on the MySQL server
   -- password is user_0d_1_pwd
   -- If user_0d_1 already exists, script must not fail

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
