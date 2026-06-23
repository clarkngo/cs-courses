INSERT INTO 
	sakila.city(city, country_id, last_update)
VALUES
	('Seattle', 103, CURDATE()); -- ***************************

SELECT 
	* 
FROM 
	sakila.city 
ORDER BY
	last_update DESC;
    
INSERT INTO 
	sakila.city(city, country_id, last_update)
VALUES
	('Bothell', 103, CURDATE()), 
    ('Coupeville', 103, CURDATE()),
    ('Ellensburg', 103, CURDATE()), 
    ('Black Diamond', 103, CURDATE()); 
    
SELECT 
	* 
FROM 
	sakila.city 
ORDER BY
	last_update DESC;

INSERT INTO
	sakila.city(last_update, city, country_id)
VALUES
	(NOW(), 'Leavenworth', 103); 
    
SELECT 
	* 
FROM 
	sakila.city 
ORDER BY
	last_update DESC;
    
    