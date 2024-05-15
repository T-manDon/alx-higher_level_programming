-- this script lists cities of California in hbtn_0d_usa
   -- the table contains a record in which name = California
   -- outcome sorted in an ascending order by the cities.id
   -- database name will pass as an arg of mysql command

SELECT id, name FROM cities
WHERE state_id = (
      SELECT id FROM states
      WHERE name = "California")
ORDER BY id;
