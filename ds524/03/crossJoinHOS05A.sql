SELECT
	staff.first_name, staff.last_name, staff.store_id, store.store_id
FROM
	staff
CROSS JOIN
	store;

SELECT
	category.name, language.name
FROM
	category
CROSS JOIN
	language;
    