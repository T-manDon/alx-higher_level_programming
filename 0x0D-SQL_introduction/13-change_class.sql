-- script removes records with <= 5 in the table second_table
-- of the database hbtn_0c_0 in your MySQL server.

DELETE FROM second_table
WHERE score <= 5;
