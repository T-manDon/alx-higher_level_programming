-- sript create database hbtn_0d_2 and user_0d_2
   -- user_0d_2 has only SELECT privilege
   -- user_0d_2 password be set to user_0d_2_pwd
   -- If hbtn_0d_2 databse already exists, script should not fail
   -- If user_0d_2 alrdy exists, script should not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
