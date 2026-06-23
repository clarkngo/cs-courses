SHOW INDEX 
FROM
	sakila.film_actor;

CREATE INDEX
	testIndex
ON
	sakila.film_actor (last_update);

SHOW INDEX 
FROM
	sakila.film_actor;
    
DROP INDEX
	testIndex
ON
	sakila.film_actor;

SHOW INDEX 
FROM
	sakila.film_actor;
