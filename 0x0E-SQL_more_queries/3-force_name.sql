-- script creates table force_name on the MySQL server.
   -- force_name description:
      -- id INT
      -- name VARCHAR(256) cannot be a null value
   -- database name passes as an arg of mysql command
   -- If force_name alrdy exists, script must not not fail

CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);
