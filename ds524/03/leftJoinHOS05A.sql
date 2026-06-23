SELECT 
	address.address, store.store_id
FROM 
	address
LEFT JOIN
	store
USING (address_id);

SELECT 
	address.address, store.store_id
FROM 
	address
LEFT JOIN
	store
USING (address_id)
WHERE
	store.store_id IS NULL;
