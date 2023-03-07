CREATE DATABASE test;

USE test; 

CREATE TABLE addresses (

	id INT,
    house_number INT,
	city VARCHAR(20),
    postcode VARCHAR(7)
);

CREATE TABLE people (

	id INT,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    address_id INT
); 

CREATE TABLE pets (

	id INT,
    name VARCHAR(20),
    species VARCHAR(20), 
    owner_id INT
); 

SHOW TABLES;


describe addresses;
describe people;

-- Add primary key 
alter table addresses
add primary key (id);

alter table people
add primary key (id);

-- remove primary key
alter table addresses
drop primary key ;



-- add foreign key
alter table people
add constraint FK_peopleaddress
foreign key (address_id) references addresses(id);

-- remove foreign key
alter table people
drop foreign key FK_peopleaddress;

describe pets;
-- add unique (Sau khi add xong thì feild không được phép có giá trị trùng lặp)
alter table pets
add constraint u_species unique (species);

-- remove unique
alter table pets
drop index u_species




USE test; 

-- 1. Add a primary key to the id fields in the pets and people tables.

ALTER TABLE people
ADD PRIMARY KEY (id);

DESCRIBE pets;
DESCRIBE people;

-- 2. Add a foreign key to the owner_id field in the pets table referencing the id field 
-- in the people table. 

ALTER TABLE pets 
ADD CONSTRAINT FK_PetsOwner 
FOREIGN KEY (owner_id) REFERENCES people(id);

-- 3. Add a column named email to the people table. 

ALTER TABLE people
ADD COLUMN email VARCHAR(20);

-- 4. Add a unique constraint to the email column in the people table.

ALTER TABLE people
ADD CONSTRAINT u_email UNIQUE (email);



-- 5. Rename the name column in the pets table to ‘first_name’.

ALTER TABLE pets CHANGE `name` `first_name` VARCHAR(20);

-- 6. Change the postcode data type to CHAR(7) in the addresses table.

ALTER TABLE addresses MODIFY postcode CHAR(7);

DESCRIBE addresses;












