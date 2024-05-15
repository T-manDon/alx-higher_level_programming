-- this script lists cities in the database hbtn_0d_usa
   -- every record display the cities.id - cities.name - states.name
   -- Results sorted in ascending order
   -- database name will pass as arg of mysql command

SELECT cities.id, cities.name, states.name FROM cities
JOIN states ON cities.state_id=states.id
ORDER BY cities.id;
