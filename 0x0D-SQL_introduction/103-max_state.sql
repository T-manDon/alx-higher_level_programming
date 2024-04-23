-- shows max temperature of every state (arranged by State name).

SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state ORDER BY state;
