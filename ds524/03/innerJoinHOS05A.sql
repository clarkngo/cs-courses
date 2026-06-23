SELECT 
	city.city, country.country
FROM
	city
INNER JOIN
	country
ON
	city.country_id = country.country_id;

SELECT
	city.city, country.country
FROM
	city
INNER JOIN
	country
USING (country_id);

SELECT
	store.store_id, staff.first_name, staff.last_name
FROM
	store
INNER JOIN
	staff
ON
	store.manager_staff_id = staff.staff_id;

SELECT
	store.store_id, address.address, staff.first_name, staff.last_name
FROM
	store
INNER JOIN
	address
ON
	store.address_id = address.address_id
INNER JOIN
	staff
ON
	store.manager_staff_id = staff.staff_id;
