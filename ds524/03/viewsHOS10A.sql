CREATE VIEW filmsWithCategories
AS
SELECT
	f.film_id, f.title, c.name as 'genre', f.rating
FROM
	film f
INNER JOIN
	film_category fc
ON 
	f.film_id = fc.film_id
INNER JOIN
	category c
ON
	fc.category_id = c.category_id;
    
SELECT
	*
FROM
	filmsWithCategories
WHERE
	rating = 'PG-13';
    
CREATE VIEW monthsofyear (month)
AS
	SELECT 'January'
    UNION
    SELECT 'February'
    UNION
    SELECT 'March'
    UNION
    SELECT 'April'
    UNION
    SELECT 'May'
    UNION
    SELECT 'June'
    UNION
    SELECT 'July'
    UNION
    SELECT 'August'
    UNION
    SELECT 'September'
    UNION
    SELECT 'October'
    UNION
    SELECT 'November'
    UNION
    SELECT 'December';
    
SELECT
	*
FROM
	monthsofyear;
    
DROP VIEW filmsWithCategories;
DROP VIEW monthsofyear;
