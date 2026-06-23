-- SCUBA_DIVER Selection with Aliases

SELECT 
    SCUBA_DIVER_ID AS "SCUBA ID",
    LAST_NAME AS "Diver Last Name",
    FIRST_NAME AS "Diver First Name",
    CERTIFICATION_NUMBER AS "Certification No.",
    CERTIFICATION_DATE AS "Certification Date",
    CERTIFICATION_CODE AS "Certification Code",
    INSTRUCTOR_ID AS "Instructor No.",
    CERTIFICATION_LEVEL AS "Certification Level"
FROM 
    SCUBA_DIVER
GROUP BY 
    CERTIFICATION_LEVEL, 
    SCUBA_DIVER_ID, LAST_NAME, FIRST_NAME, 
    CERTIFICATION_NUMBER, CERTIFICATION_DATE, 
    CERTIFICATION_CODE, INSTRUCTOR_ID
ORDER BY 
    LAST_NAME DESC, 
    FIRST_NAME DESC;


-- Joined Selection with IN Filter

SELECT 
    S.SCUBA_DIVER_ID AS "SCUBA ID",
    S.LAST_NAME AS "Diver Last Name",
    S.FIRST_NAME AS "Diver First Name",
    I.LAST_NAME AS "Instructor Last Name",
    I.FIRST_NAME AS "Instructor First Name",
    S.CERTIFICATION_LEVEL AS "Certification Level"
FROM 
    SCUBA_DIVER S
JOIN 
    INSTRUCTOR I ON S.INSTRUCTOR_ID = I.INSTRUCTOR_ID
WHERE 
    S.CERTIFICATION_LEVEL IN ('Master', 'Rescue');


-- IN Statement vs. Correlated Subquery 

-- The primary difference between an IN statement and a correlated subquery lies in how the 
-- database engine executes the logic and handles data dependencies. An IN statement typically 
-- utilizes a non-correlated subquery, meaning the inner query is independent and runs exactly 
-- once to generate a static list of values before the outer query begins its execution. 
-- Because it creates this result set upfront, it is generally more efficient for simple filters or handling static lists. 
-- Conversely, a correlated subquery is functionally dependent on the outer query; it references columns from the outer statement, 
-- forcing the inner query to run repeatedly—once for every single row processed by the outer query. 
-- This row-by-row execution often makes correlated subqueries less efficient, particularly when working with large datasets, 
-- as the overhead of multiple executions can significantly slow down performance. Therefore, for future exercises and 
-- optimized database management, the IN statement is usually the preferred choice unless the specific logic requires a direct, 
-- row-level relationship between the two