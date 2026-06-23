CREATE TABLE sample_table (
	student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(40),
    last_name VARCHAR(40)
);
    
CREATE TABLE sample_table_2 (
	student_id INT AUTO_INCREMENT,
    first_name VARCHAR(40),
    last_name VARCHAR(40),
    age INT,
    PRIMARY KEY(student_id, age)
);

SHOW INDEX
FROM
	sample_table_2;

CREATE TABLE sample_table_3 (
	student_id INT,
    first_name VARCHAR(40),
    last_name VARCHAR(40)
);

ALTER TABLE
	sample_table_3
ADD PRIMARY KEY(student_id);

ALTER TABLE 
	sample_table
ADD fk_student_id INT,
ADD FOREIGN KEY fk_to_sample_table_3 (fk_student_id)
REFERENCES sample_table_3(student_id);

DROP TABLE 
	sample_table;
    
DROP TABLE 
	sample_table_2;
    
DROP TABLE 
	sample_table_3;
