DELIMITER //
CREATE PROCEDURE sp_GetActors()
BEGIN
	SELECT 
		first_name, last_name
    FROM
		actor;
END //
DELIMITER ;

CALL sp_GetActors();

DELIMITER //
CREATE PROCEDURE sp_GetCountryId(IN countryName varchar(50))
BEGIN
	SELECT
		country_id, country
	FROM
		country
	WHERE
		country = countryName;
END //
DELIMITER ;

CALL sp_GetCountryId('USA');

CALL sp_GetCountryId('United States');

DELIMITER //
CREATE PROCEDURE sp_CountCitiesByCountry(OUT cityCount int)
BEGIN
	SELECT
		count(city_id) INTO cityCount
	FROM
		city
	WHERE
		country_id = 103;
END //
DELIMITER ;

CALL sp_CountCitiesByCountry(@UnitedStatesCities);
SELECT @UnitedStatesCities as Cities;

DELIMITER //
CREATE PROCEDURE sp_CountCitiesByCountry_Inout(INOUT cityCount int, IN countryId int)
BEGIN
	SELECT
		count(city_id) INTO cityCount
	FROM
		city
	WHERE
		country_id = countryId;
END //
DELIMITER ;

CALL sp_CountCitiesByCountry_Inout(@CanadaCities, 20);
SELECT @CanadaCities as Cities;

DROP PROCEDURE sp_CountCitiesByCountry_Inout;
DROP PROCEDURE sp_CountCitiesByCountry;
DROP PROCEDURE sp_GetActors;
DROP PROCEDURE sp_GetCountryId;
