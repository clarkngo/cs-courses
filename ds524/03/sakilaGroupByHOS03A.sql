SELECT
	staff_id, COUNT(*)
FROM
	sakila.rental
GROUP BY
	staff_id;

SELECT
	customer_id, COUNT(*)
FROM
	sakila.rental
GROUP BY
	customer_id
HAVING
	COUNT(*) > 40;

SELECT
	length, COUNT(*)
FROM
	sakila.film
WHERE
	length > 180
GROUP BY
	length;
    
SELECT
	length, COUNT(*)
FROM
	sakila.film
GROUP BY
	length
HAVING
	COUNT(*) > 10
ORDER BY
	COUNT(*) DESC;

SELECT
	rating, COUNT(*)
FROM
	sakila.film
GROUP BY
	rating;
