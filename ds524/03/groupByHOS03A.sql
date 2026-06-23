SELECT
	continent
FROM
	world.country
GROUP BY 
	continent;

SELECT DISTINCT
	continent
FROM 
	world.country;
    
SELECT
	continent, COUNT(*)
FROM
	world.country
GROUP BY 
	continent;

SELECT
	continent, COUNT(*)
FROM
	world.country
GROUP BY 
	continent
ORDER BY
	COUNT(*) DESC;


SELECT
	continent, COUNT(*)
FROM 
	world.country
WHERE
	lifeexpectancy > 60
GROUP BY 
	continent;

SELECT
	continent, COUNT(*), AVG(lifeexpectancy)
FROM
	world.country
GROUP BY
	continent
HAVING
	AVG(lifeexpectancy) > 60;
    
SELECT
	continent, COUNT(*), AVG(lifeexpectancy)
FROM
	world.country
GROUP BY
	continent;

SELECT
	continent, COUNT(*), AVG(lifeexpectancy)
FROM
	world.country
WHERE
	lifeexpectancy > 60
GROUP BY
	continent
HAVING
	AVG(lifeexpectancy) > 60;
