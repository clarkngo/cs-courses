-- a. Select All Scuba Diver Information
-- Note on standard SQL constraints: A standard GROUP BY clause requires all non-aggregated columns in 
-- the SELECT list to be included in the GROUP BY statement. To fulfill the prompt's instruction to sort
--  descending while grouping by Certification Level, the standard query is structured as follows:
SELECT 
    SCUBA_DIVER_ID AS "SCUBA ID", 
    LAST_NAME AS "Diver Last Name", 
    FIRST_NAME AS "Diver First Name", 
    CERTIFICATION_NUMBER AS "Certification No.", 
    CERTIFICATION_DATE AS "Certification Date", 
    CERTIFICATION_CODE AS "Certification Code", 
    INSTRUCTOR_ID AS "Instructor No.", 
    CERTIFICATION_LEVEL AS "Certification Level"
FROM SCUBA_DIVER
GROUP BY 
    CERTIFICATION_LEVEL, 
    LAST_NAME, 
    FIRST_NAME, 
    SCUBA_DIVER_ID, 
    CERTIFICATION_NUMBER, 
    CERTIFICATION_DATE, 
    CERTIFICATION_CODE, 
    INSTRUCTOR_ID
ORDER BY LAST_NAME DESC, FIRST_NAME DESC;

-- b. Largest Scuba ID using GREATEST
-- The GREATEST function in SQL compares values across multiple columns or expressions per row, 
-- rather than evaluating an entire column vertically (which uses MAX).
SELECT GREATEST(SCUBA_DIVER_ID) AS "SCUBA ID"
FROM SCUBA_DIVER;

-- c. Smallest Certification Date using LEAST
-- Similar to GREATEST, the LEAST function compares multiple values row-by-row.
SELECT LEAST(CERTIFICATION_DATE) AS "Smallest Certification Date"
FROM SCUBA_DIVER;

-- d. Minimum Certification Number using MIN
SELECT MIN(CERTIFICATION_NUMBER) AS "Minimum Certification No."
FROM SCUBA_DIVER;

-- e. Maximum Certification Number using MAX
SELECT MAX(CERTIFICATION_NUMBER) AS "Certification No."
FROM SCUBA_DIVER;

-- Part 4: Conceptual Review & Real-World Application
-- The RANK function in SQL serves to assign a unique position or rank to each row within a 
-- result set partition based on a specified ordering column. If a tie occurs, identical values 
-- receive the same rank, and subsequent ranks are skipped. In a real-world scenario, a diving 
-- center could use RANK to evaluate instructor performance by ordering their total issued certifications. 
-- This allows management to easily identify top performers for bonuses or safety milestones while prioritizing 
-- the distribution of new students.  The COS function is a mathematical tool that calculates the trigonometric 
-- cosine of an angle provided in radians. While seemingly detached from typical business databases, it is highly 
-- beneficial in geospatial applications. For instance, it can be embedded into the Haversine formula to compute 
-- the exact distance between two geographical points using their latitude and longitude coordinates. 
-- A diving agency could leverage this to help users find the nearest certified dive sites or ocean mapping coordinates 
-- relative to their current location.  The SUM function is an aggregate mathematical tool used to calculate the grand 
-- total of a numeric column across a set of rows. In a practical business setting, a scuba facility would use SUM for 
-- financial auditing and resource tracking, such as totaling up the exact revenue generated from equipment rentals or 
-- course fees over a specific fiscal quarter. This aggregate data is vital for generating accurate profit-and-loss statements 
-- and ensuring the business meets its financial targets.  The AVG function is an aggregate math function that 
-- computes the arithmetic mean of a specified numeric column. For a dive safety and performance database, 
-- AVG provides critical insights by tracking metrics like the average depth or average dive duration across hundreds of logged trips. 
-- Measuring these averages allows the system to identify abnormal trends—such as sudden increases in air consumption or 
-- unusually deep profiles—helping instructors monitor student safety and equipment efficiency.  

-- Future Project Justification
-- Using these math and aggregate functions establishes a foundation for predictive data metrics in future exercises. 
-- For instance, combining AVG and SUM data with RANK allows a system to dynamically categorize diver performance or 
-- automatically flag anomalies—such as an instructor certifying an unrealistic volume of divers—thereby safeguarding 
-- data quality and regulatory compliance.