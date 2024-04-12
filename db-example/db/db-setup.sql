CREATE DATABASE NovoVoom;

USE NovoVoom;

CREATE TABLE Employee(
	first TEXT,
	last TEXT,
	dept TEXT,
	phone TEXT,
	ID int unsigned AUTO_INCREMENT,
	PRIMARY KEY (ID)
);

INSERT INTO Employee (last, first, dept, phone) VALUES ('Lee', 'Karen', 'IT', '555-555-4129');

INSERT INTO Employee (last, first, dept, phone) VALUES ('Smith', 'Karl', 'IT', '555-555-1419');

INSERT INTO Employee (last, first, dept, phone) VALUES ('Vargas', 'Tony', 'Finance', '555-555-0213');

INSERT INTO Employee (last, first, dept, phone) VALUES ('Stark', 'Susan', 'Finance', '555-555-1122');

INSERT INTO Employee (last, first, dept, phone) VALUES ('Li', 'Jennifer', 'Communications', '555-555-7180');

INSERT INTO Employee (last, first, dept, phone) VALUES ('Garcia', 'Jesus', 'Marketing', '555-555-6933');

INSERT INTO Employee (last, first, dept, phone) VALUES ('Bashar', 'Mohammed', 'Research', '555-555-4033');

INSERT INTO Employee (last, first, dept, phone) VALUES ('Nakamura', 'Yukiko', 'Research', '555-555-9272');

INSERT INTO Employee (last, first, dept, phone) VALUES ('Jones', 'David', 'Research', '555-555-8652');

INSERT INTO Employee (last, first, dept, phone) VALUES ('Williams', 'Olympia', 'Research', '555-555-0227');

INSERT INTO Employee (last, first, dept, phone) VALUES ('Lopez', 'Sofia', 'Sales', '555-555-6822');

INSERT INTO Employee (last, first, dept, phone) VALUES ('Johnson', 'Alex', 'Marketing', '555-555-4801');

INSERT INTO Employee (last, first, dept, phone) VALUES ('Perez', 'Allie', 'HR', '555-555-8743');

INSERT INTO Employee (last, first, dept, phone) VALUES ('Erikson', 'Lars', 'Sales', '555-555-3029');

INSERT INTO Employee (last, first, dept, phone) VALUES ('Lewis', 'Andy', 'Research', '555-555-5520');

INSERT INTO Employee (last, first, dept, phone) VALUES ('Jackson', 'Samantha', 'Research', '555-555-4280');

INSERT INTO Employee (last, first, dept, phone) VALUES ('Anderson', 'Frank', 'IT', '555-555-7712');

INSERT INTO Employee (last, first, dept, phone) VALUES ('Cho', 'Rachel', 'Finance', '555-555-8124');


CREATE USER 'webapp'@'%' IDENTIFIED BY 'novovoom1web';

GRANT ALL ON NovoVoom.* TO 'webapp'@'%';

