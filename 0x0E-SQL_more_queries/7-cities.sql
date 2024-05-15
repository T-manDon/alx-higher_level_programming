-- this script creates dtbs hbtn_0d_usa and city table on the server.
   -- cities description:
      -- id INT unique - auto generated and is the primary key
      -- state_id INT - is a FOREIGN KEY that
      --                reference id of states table
      -- name VARCHAR(256) - not null
   -- If table hbtn_0d_usa exists, script must not fail
   -- If table cities exists, script must not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
       id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
       state_id INT NOT NULL,
       FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id),
       name VARCHAR(256) NOT NULL);
