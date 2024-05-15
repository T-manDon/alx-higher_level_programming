-- creates id_not_null on the MySQL server
   -- id_not_null description:
      -- id INT - default value 1
      -- name VARCHAR(256)
   -- The database name passes as an arg of the mysql command
   -- If table id_not_null alrdy exists, script must not fail

CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));
