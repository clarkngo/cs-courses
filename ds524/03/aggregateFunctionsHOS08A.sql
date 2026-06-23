SELECT
	Continent, AVG(Population)
FROM
	world.country
GROUP BY
	Continent;
    
SELECT
	cl.Language, AVG(c.LifeExpectancy)
FROM 
	world.country c
INNER JOIN
	world.countrylanguage cl
ON
	c.Code = cl.CountryCode
GROUP BY
	cl.Language;
    
SELECT
	Language, COUNT(*) as Count
FROM
	world.countrylanguage
GROUP BY
	Language
ORDER BY
	Count DESC;
    
SELECT
	COUNT(*)
FROM
	world.city
WHERE
	Population > 1000000;
    
SELECT
	SUM(Population)
FROM
	world.country;
    
SELECT
	CountryCode, SUM(Percentage)
FROM
	world.countrylanguage
GROUP BY 
	CountryCode;

SELECT
	MIN(Population)
FROM
	world.city;
    
SELECT
	MIN(Name)
FROM
	world.city;

SELECT
	MAX(Name), MAX(Population)
FROM
	world.country;
    
SELECT
	Continent, MAX(LifeExpectancy)
FROM
	world.country
GROUP BY
	Continent;

SELECT
	MIN(Population), MAX(Population), AVG(Population), SUM(Population), COUNT(*)
FROM
	world.country;
    
SELECT
	MIN(SurfaceArea), MAX(SurfaceArea), AVG(SurfaceArea), SUM(SurfaceArea), COUNT(*)
FROM
	world.country;