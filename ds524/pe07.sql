
-- ### 3a. Select and Alias Diver Information

-- This query extracts all scuba diver data, assigns the requested tracking aliases to each column, and sorts the results by last name and then first name in descending order.

sql
SELECT 
    SCUBA_DIVER_ID AS "SCUBA DIVER ID",
    LAST_NAME AS "Diver Last Name",
    FIRST_NAME AS "Diver First Name",
    CERTIFICATION_NUMBER AS "Certification No.",
    CERTIFICATION_DATE AS "Certification Date",
    CERTIFICATION_CODE AS "Certification Code",
    INSTRUCTOR_ID AS "Instructor No.",
    CERTIFICATION_LEVEL AS "Certification Level"
FROM 
    SCUBA_DIVER
ORDER BY 
    LAST_NAME DESC, 
    FIRST_NAME DESC;


-- ### 3b. Update Certification Dates

-- This statement shifts any certification date recorded as `'2004-08-20'` forward to `'2005-08-20'`.


UPDATE SCUBA_DIVER
SET CERTIFICATION_DATE = '2005-08-20'
WHERE CERTIFICATION_DATE = '2004-08-20';



---

-- ### 3c. Update Last Name

-- This statement modifies the last name of the designated diver(s) from `'Williams'` to `'Williams-Smith'`.


UPDATE SCUBA_DIVER
SET LAST_NAME = 'Williams-Smith'
WHERE LAST_NAME = 'Williams';



---

-- ### 3d. Delete Diver Record

-- This command drops the unique row associated with the diver whose `SCUBA_DIVER_ID` is `9`.

DELETE FROM SCUBA_DIVER
WHERE SCUBA_DIVER_ID = 9;


---

-- ### 3e. Insert New Diver Record

-- This statement appends the new record for diver Happy Golucky directly into the table dataset.
INSERT INTO SCUBA_DIVER (
    SCUBA_DIVER_ID, 
    LAST_NAME, 
    FIRST_NAME, 
    CERTIFICATION_NUMBER, 
    CERTIFICATION_DATE, 
    CERTIFICATION_CODE, 
    INSTRUCTOR_ID, 
    CERTIFICATION_LEVEL
)
VALUES (
    10, 
    'GOLUCKY', 
    'HAPPY', 
    '9905400000', 
    '2021-06-30', 
    'P', 
    1876, 
    'OPEN WATER'
);
