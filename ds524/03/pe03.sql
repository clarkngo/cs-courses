-- a. Select data from the SCUBA_DIVER table to display all SCUBA diver information by last
-- name, first name in descending order. Use the Alias Names for each column name,
-- “SCUBA ID, ”Diver Last Name”, “Diver First Name”, “Certification No.”, “Certification
-- Date”, “Certification Code”, “Instructor No.”, “Certification Level” group by Certification
-- Level.

-- b. Select data from the SCUBA_DIVER table to display all SCUBA diver information and
-- group by Instructor Id. Use the Alias Names stated above.

i. Select data from the SCUBA_DIVER table and display the unique types of SCUBA diver
certification levels.
j. Select data from the SCUBA_DIVER table and display the lowest SCUBA Id in the table.
k. Select data from the SCUBA_DIVER table and display the highest SCUBA Id in the table.
SELECT SCUBA_DIVER_ID AS "SCUBA ID", LAST_NAME AS "Diver Last Name", FIRST_NAME AS "Diver First Name", 
       CERTIFICATION_NUMBER AS "Certification No.", CERTIFICATION_DATE AS "Certification Date", 
       CERTIFICATION_CODE AS "Certification Code", INSTRUCTOR_ID AS "Instructor No.", 
       CERTIFICATION_LEVEL AS "Certification Level"
FROM SCUBA_DIVER
ORDER BY LAST_NAME DESC, FIRST_NAME DESC;


-- c. Select data from the SCUBA_DIVER table to count the number of Scuba Divers. Use an
-- Alias Name as stated above to describe the resulting column.

SELECT INSTRUCTOR_ID AS "Instructor No.", COUNT(*) AS "Total Divers"
FROM SCUBA_DIVER
GROUP BY INSTRUCTOR_ID;

-- d. Select data from the SCUBA_DIVER table to display distinct values of each Instructor Id.
SELECT DISTINCT INSTRUCTOR_ID
FROM SCUBA_DIVER;

-- e. Select data from the SCUBA_DIVER table to display distinct values of each Certification
-- Level.
SELECT DISTINCT CERTIFICATION_LEVEL
FROM SCUBA_DIVER;

-- f. Select data from the SCUBA_DIVER table to display all SCUBA diver information for the
-- SCUBA diver(s) with certifications less than 6 months old group by Instructor Id.

SELECT * FROM SCUBA_DIVER 
WHERE CERTIFICATION_DATE >= CURRENT_DATE - INTERVAL '6' MONTH
ORDER BY INSTRUCTOR_ID;

-- g. Select data from the SCUBA_DIVER table to display all SCUBA diver information for the
-- SCUBA diver(s) with the oldest certification date group by Instructor Id.
SELECT * FROM SCUBA_DIVER WHERE CERTIFICATION_DATE = (SELECT MIN(CERTIFICATION_DATE) FROM SCUBA_DIVER);

-- h. Select data from the SCUBA_DIVER table to display all SCUBA diver information for the
-- SCUBA diver(s) with the most recent certification date group by Instructor Id.
SELECT * FROM SCUBA_DIVER WHERE CERTIFICATION_DATE = (SELECT MAX(CERTIFICATION_DATE) FROM SCUBA_DIVER);

-- i. Select data from the SCUBA_DIVER table and display the unique types of SCUBA diver
-- certification levels.
SELECT DISTINCT CERTIFICATION_LEVEL FROM SCUBA_DIVER;

-- j. Select data from the SCUBA_DIVER table and display the lowest SCUBA Id in the table.
SELECT MIN(SCUBA_DIVER_ID) AS Lowest_ID FROM SCUBA_DIVER; 

-- k. Select data from the SCUBA_DIVER table and display the highest SCUBA Id in the table.
SELECT MAX(SCUBA_DIVER_ID) AS Highest_ID FROM SCUBA_DIVER;

-- What is a constraint? What about this feature improves the efficiency of data stored in a
-- database? Justify your answer and results for input that will be used in the future PE(s).
-- A constraint is a rule applied to a database column to limit the type of data that can be entered.