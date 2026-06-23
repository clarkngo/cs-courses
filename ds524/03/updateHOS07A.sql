SELECT
	*
FROM
	sakila.actor
WHERE
	first_name = 'TOM';

UPDATE
	sakila.actor
SET
	first_name = 'TOMMY'
WHERE
	first_name = 'TOM';
    
SELECT
	*
FROM
	sakila.actor
WHERE
	first_name IN ('TOM','TOMMY');

UPDATE
	sakila.actor
SET
	first_name = 'JENNY',
    last_name = 'CHASE'
WHERE
	actor_id = 4;

SELECT
	*
FROM
	sakila.actor
WHERE
	actor_id = 4;

UPDATE
	sakila.actor
SET
	first_name = 'TOM'
WHERE
	first_name = 'TOMMY'; 
    
UPDATE
	sakila.actor
SET
	first_name = 'JENNIFER',
    last_name = 'DAVIS'
WHERE
	actor_id = 4;
    
SELECT
	*
FROM
	sakila.actor
WHERE
	first_name IN ('TOM', 'JENNIFER');
