-- creates dtbs hbtn_0d_usa on MySQL server.
   -- states description:
      -- id INT unique - auto generated and comprise primary key
      -- name VARCHAR(256) - cannot be null
   -- If the table hbtn_0d_usa already exists script must not fail
   -- If the table alrdy exists, script must not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
       id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(256) NOT NULL);
