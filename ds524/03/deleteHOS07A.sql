DELETE FROM
	sakila.city
WHERE
	city_id = 603;

SELECT
	*
FROM
	sakila.city
ORDER BY
	city_id DESC;

DELETE FROM
	sakila.city
WHERE
	city_id > 600;

SELECT
	*
FROM
	sakila.city
ORDER BY
	city_id DESC;
    