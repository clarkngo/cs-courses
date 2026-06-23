SELECT * FROM actor;

SELECT
first_name,
last_name
FROM
actor;

SELECT
   first_name,
   last_name
FROM
   actor;


SELECT
  *
FROM
Sakila.payment
WHERE
amount > 6;


 
SELECT
  *
FROM
Sakila.payment
WHERE
payment_date
between
‘2005-06-15’
and
‘2005-06-16’;

 SELECT * FROM sakila.actor where first_name like “%P”;

 SELECT * FROM sakila.actor where first_name like “%P%”;