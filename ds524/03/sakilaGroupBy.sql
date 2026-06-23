-- Query #1
SELECT staff_id, COUNT(*) FROM sakila.rental GROUP BY staff_id;

-- Query #2
SELECT customer_id, COUNT(*) FROM sakila.rental GROUP BY customer_id HAVING COUNT(*) > 40;

-- Query #3
SELECT length, COUNT(*) FROM sakila.film WHERE length > 180 GROUP BY length;

-- Query #4
SELECT length, COUNT(*) FROM sakila.film GROUP BY length HAVING COUNT(*) > 10 ORDER BY COUNT(*) DESC;

-- Query #5
SELECT rating, COUNT(*) FROM sakila.film GROUP BY rating;
