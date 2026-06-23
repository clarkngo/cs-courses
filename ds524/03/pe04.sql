-- 1. SQL Table Creation with Referential Integrity
-- To demonstrate referential integrity, we must first have a parent table (e.g., `INSTRUCTORS`) before the child table (`SCUBA_DIVER`) can reference it.

-- Creating the parent table for referential integrity
CREATE TABLE INSTRUCTORS (
    INSTRUCTOR_ID INTEGER PRIMARY KEY,
    INSTRUCTOR_NAME VARCHAR(50)
);

-- Creating the Scuba Diver table with PK and FK
CREATE TABLE SCUBA_DIVER (
    SCUBA_DIVER_ID INTEGER PRIMARY KEY,
    DIVER_NAME VARCHAR(50),
    CERTIFICATION_LEVEL VARCHAR(50),
    LAST_DIVE_DATE DATE,
    INSTRUCTOR_ID INTEGER,
    CONSTRAINT fk_instructor 
        FOREIGN KEY (INSTRUCTOR_ID) 
        REFERENCES INSTRUCTORS(INSTRUCTOR_ID)
);


---

-- 3. Progressive CREATE Statements
-- Based on your requirements for the `SCUBA_DIVER` table:

-- **a. Basic CREATE TABLE**
CREATE TABLE SCUBA_DIVER (
    SCUBA_DIVER_ID INTEGER,
    DIVER_NAME VARCHAR(50),
    CERTIFICATION_DATE DATE,
    DIVE_COUNT INTEGER,
    INSTRUCTOR_ID INTEGER
);

-- **b. Including Primary Key (PK)**
CREATE TABLE SCUBA_DIVER (
    SCUBA_DIVER_ID INTEGER PRIMARY KEY,
    DIVER_NAME VARCHAR(50),
    CERTIFICATION_DATE DATE,
    DIVE_COUNT INTEGER,
    INSTRUCTOR_ID INTEGER
);

-- **c. Including Primary Key (PK) and Foreign Key (FK)**
CREATE TABLE SCUBA_DIVER (
    SCUBA_DIVER_ID INTEGER PRIMARY KEY,
    DIVER_NAME VARCHAR(50),
    CERTIFICATION_DATE DATE,
    DIVE_COUNT INTEGER,
    INSTRUCTOR_ID INTEGER,
    FOREIGN KEY (INSTRUCTOR_ID) REFERENCES INSTRUCTOR_TABLE(INSTRUCTOR_ID)
);

---

### 4. Primary Key Index (PK)
A **Primary Key** is a unique identifier for a specific record in a table. It must contain unique values and cannot contain `NULL` values.

* **Integrity:** It ensures **Entity Integrity**. By requiring a unique PK, the database guarantees that no two rows are identical, preventing "ghost" records or duplicate entries.
* **Performance:** Databases automatically create a **Clustered Index** on the PK. This physically organizes the data on the disk in the order of the key, making searches (queries) for specific IDs incredibly fast (O(log n) time complexity rather than a full table scan).

---

### 5. Unique Index (UK)
A **Unique Index** ensures that all values in a column (or a group of columns) are distinct from one another.

* **Integrity:** It maintains data accuracy by preventing duplicate business logic data (like an Email or Social Security Number) that isn't necessarily the Primary Key. Unlike a PK, a Unique Index usually allows for a single `NULL` value (depending on the SQL dialect).
* **Performance:** It speeds up data retrieval for those specific columns because the database builds a lookup B-tree, allowing the engine to find the "unique" value without checking every row.

---

### 6. Foreign Key (FK)
A **Foreign Key** is a column that creates a link between data in two tables. It references the Primary Key of another table.

* **Integrity:** It enforces **Referential Integrity**. This ensures that the relationship between tables remains consistent. For example, you cannot assign a `SCUBA_DIVER` to an `INSTRUCTOR_ID` that doesn't exist in the Instructor table. It also prevents the deletion of a parent record if child records are still attached to it.
* **Justification:** Using FKs eliminates "orphaned" records. In professional environments, this is the backbone of relational logic, ensuring that your data remains a cohesive "web" rather than isolated, unreliable lists.

---

### Comparison Summary

| Feature | Primary Key (PK) | Unique Index (UK) | Foreign Key (FK) |
| :--- | :--- | :--- | :--- |
| **Purpose** | Unique identifier for the row. | Prevents duplicates in specific columns. | Links tables together. |
| **Nulls** | Never allowed. | Usually one NULL allowed. | Allowed (if the relationship is optional). |
| **Limit** | One per table. | Multiple per table. | Multiple per table. |
| **Integrity** | Entity Integrity. | Data Uniqueness. | Referential Integrity. |