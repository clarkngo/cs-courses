SELECT 
	customer.first_name, address.address
FROM 
	customer
RIGHT JOIN
	address
USING (address_id);

SELECT 
	customer.first_name, address.address
FROM 
	customer
RIGHT JOIN
	address
USING (address_id)
WHERE
	customer.first_name IS NULL;
