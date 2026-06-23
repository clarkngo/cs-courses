-- Query #1
SELECT continent FROM world.country GROUP BY continent;

-- Query #2
SELECT DISTINCT continent FROM world.country;

-- Query #3
SELECT continent, COUNT(*) FROM world.country GROUP BY continent;

-- Query #4
SELECT continent, COUNT(*) FROM world.country GROUP BY continent ORDER BY COUNT(*) DESC;

-- Query #5
SELECT continent, COUNT(*) FROM world.country WHERE lifeexpectancy > 60 GROUP BY continent;

-- Query #6
SELECT continent, COUNT(*), AVG(lifeexpectancy) FROM world.country GROUP BY continent HAVING AVG(lifeexpectancy) > 60;

-- Query #7
SELECT continent, COUNT(*), AVG(lifeexpectancy) FROM world.country GROUP BY continent;

-- Query #8
SELECT continent, COUNT(*), AVG(lifeexpectancy) FROM world.country WHERE lifeexpectancy > 60 GROUP BY continent HAVING AVG(lifeexpectancy) > 60;
