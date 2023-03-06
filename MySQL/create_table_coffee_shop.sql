SHOW databases;

CREATE database coffee_store;

use coffee_store;

create table products(
	id INT auto_increment primary key,
	name varchar(30),
    price decimal(3,2)
);

show tables;



create table customers(
	id INT auto_increment primary key,
	first_name varchar(30),
    last_name varchar(30),
    gender enum("M","F"),
    phone_number varchar(11)
);


create table orders(
	id INT auto_increment primary key,
	customer_id int,
    product_id int,
    oder_time datetime,
    foreign key (customer_id) references customers(id),
    foreign key (product_id) references products(id)
);
