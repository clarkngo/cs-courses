SELECT
	Name, Continent
FROM
	world.country
WHERE
	Code IN (SELECT
			CountryCode
		FROM
			world.city
		WHERE
			population > 7000000);

SELECT
	Name, Continent, Population, LifeExpectancy
FROM
	world.country
WHERE
	LifeExpectancy = (SELECT MAX(LifeExpectancy) FROM world.country);


SELECT
	Name, Continent, Population, LifeExpectancy
FROM
	world.country
WHERE
	LifeExpectancy <= (SELECT
			AVG(LifeExpectancy)
		FROM
			world.country);

SELECT
	address, district
FROM
	sakila.address
WHERE
	address_id IN (SELECT DISTINCT
			address_id
		FROM
			sakila.store);

SELECT
	address, district
FROM
	sakila.address
WHERE
	address_id NOT IN (SELECT DISTINCT
			address_id
		FROM
			sakila.store);
        
SELECT
	MIN(customer_total), MAX(customer_total), AVG(customer_total)
FROM
	(SELECT
		customer_id, COUNT(customer_id), SUM(amount) as customer_total
	FROM
		sakila.payment
	GROUP BY 
		customer_id) AS customer_payments;

SELECT
	payment_id, customer_id, amount
FROM
	sakila.payment p
WHERE 
	amount > (SELECT
			AVG(amount)
		FROM
			sakila.payment
		WHERE
			customer_id = p.customer_id);
        
SELECT
	title, description
FROM
	film_text ft
WHERE
	EXISTS (SELECT
			film_id, COUNT(actor_id)
		FROM
			sakila.film_actor
		INNER JOIN
			sakila.film
		USING (film_id)
		WHERE
			sakila.film.length > 180
		AND
			film_id = ft.film_id
		GROUP BY 
			sakila.film.film_id);
