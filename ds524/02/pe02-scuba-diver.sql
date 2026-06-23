-- a. Display all information by last name, first name in descending order with Aliases
-- IMPROVEMENT: Using explicit column lists instead of SELECT * is better for performance and security.
-- Sorting by LAST_NAME then FIRST_NAME ensures a predictable order for identical surnames.
SELECT 
    SCUBA_DIVER_ID AS "SCUBA DIVER ID", 
    LAST_NAME AS "Diver Last Name", 
    FIRST_NAME AS "Diver First Name", 
    CERTIFICATION_NUMBER AS "Certification No.", 
    CERTIFICATION_DATE AS "Certification Date", 
    CERTIFICATION_CODE AS "Certification Code", 
    INSTRUCTOR_ID AS "Instructor No.", 
    CERTIFICATION_LEVEL AS "Certification Level"
FROM SCUBA_DIVER
ORDER BY LAST_NAME DESC, FIRST_NAME DESC;

-- b. Display all information ordered by certification date
-- IMPROVEMENT: Alias names help non-technical users understand the report.
-- Consider adding DESC if you want to see the newest certifications first.
SELECT 
    SCUBA_DIVER_ID AS "SCUBA DIVER ID", 
    LAST_NAME AS "Diver Last Name", 
    FIRST_NAME AS "Diver First Name", 
    CERTIFICATION_NUMBER AS "Certification No.", 
    CERTIFICATION_DATE AS "Certification Date", 
    CERTIFICATION_CODE AS "Certification Code", 
    INSTRUCTOR_ID AS "Instructor No.", 
    CERTIFICATION_LEVEL AS "Certification Level"
FROM SCUBA_DIVER
ORDER BY CERTIFICATION_DATE;

-- c. Display unique Instructor Id, Names, and Date ordered by cert level descending
-- IMPROVEMENT: DISTINCT is useful here to avoid duplicate rows if an instructor certified
-- the same diver multiple times on the same date.
SELECT DISTINCT
    INSTRUCTOR_ID AS "Instructor No.", 
    LAST_NAME AS "Diver Last Name", 
    FIRST_NAME AS "Diver First Name", 
    CERTIFICATION_DATE AS "Certification Date"
FROM SCUBA_DIVER
ORDER BY CERTIFICATION_LEVEL DESC;

-- d. Display all information with most recent certification dates first
-- IMPROVEMENT: Avoid using SELECT * in production code; specify columns to reduce data transfer.
SELECT * FROM SCUBA_DIVER
ORDER BY CERTIFICATION_DATE DESC;

-- e. Display information for the diver with the oldest certification date
-- IMPROVEMENT: The subquery method is accurate even if there's a tie for the oldest date.
-- A simpler (but slightly different) way is: ORDER BY CERTIFICATION_DATE ASC LIMIT 1.
SELECT * FROM SCUBA_DIVER
WHERE CERTIFICATION_DATE = (SELECT MIN(CERTIFICATION_DATE) FROM SCUBA_DIVER);

-- f. Display divers with certifications less than 6 months old (Relative to current date)
-- IMPROVEMENT: Using dynamic date functions like CURDATE() ensures the report is always up to date
-- without manual editing of the SQL script.
SELECT * FROM SCUBA_DIVER
WHERE CERTIFICATION_DATE >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH);

-- g. Count divers with 'P' code certifications and display as 'PADI'
-- IMPROVEMENT: Hardcoding 'PADI' as a constant string makes the output clear for stakeholders.
SELECT 
    'PADI' AS "Certification Type", 
    COUNT(*) AS "Diver Count"
FROM SCUBA_DIVER
WHERE CERTIFICATION_CODE = 'P';

-- h. Count the number of SCUBA divers with PADI certifications (Using alias/description context)
-- IMPROVEMENT: Ensure the WHERE clause matches exactly the code used in the source table.
SELECT COUNT(*) AS "PADI Diver Total"
FROM SCUBA_DIVER
WHERE CERTIFICATION_CODE = 'P';

-- i. Group divers by certification code
-- IMPROVEMENT: Grouping is the most efficient way to see a breakdown of the population.
-- Adding 'ORDER BY COUNT(*) DESC' would show the most common certifications at the top.
SELECT 
    CERTIFICATION_CODE, 
    COUNT(*) AS "Number of Divers"
FROM SCUBA_DIVER
GROUP BY CERTIFICATION_CODE;