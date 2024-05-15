-- creates unique_id on the MySQL server.
   -- unique_id description:
      -- id INT - default value 1, must be unique
      -- name VARCHAR(256)
   -- The database name will pass as arg of mysql command
   -- If table unique_id already exists, script should run

CREATE TABLE IF NOT EXISTS unique_id
       (id INT DEFAULT 1,
       UNIQUE (ID),
       name VARCHAR(256));
