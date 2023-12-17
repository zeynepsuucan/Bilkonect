-- Create the student table
CREATE TABLE student (
    sid CHAR(6) PRIMARY KEY,
    sname VARCHAR(50),
    bdate VARCHAR(50),
    dept CHAR(2),
    year VARCHAR(15),
    gpa FLOAT,
    email VARCHAR(50)
);

-- Create the company table
CREATE TABLE company (
    cid CHAR(5) PRIMARY KEY,
    cname VARCHAR(20),
    quota INT,
    gpa_threshold FLOAT,
    city VARCHAR(20)
);

-- Create the apply table to track student applications
CREATE TABLE apply (
    sid CHAR(6),
    cid CHAR(5),
    PRIMARY KEY (sid, cid),
    FOREIGN KEY (sid) REFERENCES student(sid),
    FOREIGN KEY (cid) REFERENCES company(cid)
);

-- Insert data into the student table
INSERT INTO student (sid, sname, bdate, dept, year, email, gpa)
VALUES
    ('S101', 'Ali', '1999-07-15', 'CS', 'sophomore', 'ali@gmail.com', 2.92),
    ('S102', 'Veli', '2002-01-07', 'EE', 'junior', 'veli@gmail.com', 3.96),
    ('S103', 'Ayşe', '2004-02-12', 'IE', 'freshman', 'ayse@gmail.com',3.30),
    ('S104', 'Mehmet', '2003-05-23', 'CS', 'junior', 'mehmet@gmail.com', 3.07);

-- Insert data into the company table
INSERT INTO company (cid, cname, quota, gpa_threshold, city)
VALUES
    ('C101', 'tübitak', 10, 2.50, 'Ankara'),
    ('C102', 'bist', 2, 2.80, 'Istanbul'),
    ('C103', 'aselsan', 3, 3.00, 'Ankara'),
    ('C104', 'thy', 5, 2.40, 'Istanbul'),
    ('C105', 'milsoft', 6, 2.50, 'Ankara'),
    ('C106', 'amazon', 1, 3.80, 'Palo Alto'),
    ('C107', 'tai', 4, 3.00, 'Ankara');

-- Insert data into the apply table
INSERT INTO apply (sid, cid)
VALUES
    ('S101', 'C101'),
    ('S101', 'C102'),
    ('S101', 'C104'),
    ('S102', 'C106'),
    ('S102', 'C105'),
    ('S103', 'C104'),
    ('S103', 'C107'),
    ('S104', 'C102'),
    ('S104', 'C107');

ALTER TABLE student MODIFY COLUMN sname VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci;
