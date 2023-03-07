use coffee_store;

select * from products;
select * from orders;
select * from customers;

describe products;
describe orders;
describe customers;



select first_name, last_name, phone_number from customers;

select * from products
where price = 3.00
and coffee_origin = "Brazil"; -- Có thể thay and bằng or


select * from products
where price >= 3 ;   


select * from customers
where phone_number is null ;   

select * from customers
where phone_number is not null ;  


select first_name, phone_number from customers
where gender = "F"
and last_name = "Bluth";

select name from products
where price > 3
or coffee_origin = "Brazil";


select id from customers
where phone_number is null
and gender = "M";


select * from customers
where last_name in ("Taylor","Bluth")
and first_name not in ("Sarah");

select * from orders
where order_time between "2017-01-01" and "2017-07-01";

select * from orders
where id between 100 and 130;



select * from customers
where last_name like "W%";


select * from customers
where last_name like "%o%";

select * from products
where price like "3%";


select * from customers
order by first_name asc; -- Thuận chiều

select * from customers
order by first_name desc; -- Ngược chiều


select * from products
where coffee_origin in ("Brazil","Indonesia")
order by name asc;

select * from orders
where (order_time >= "2017-02-01")
and (id like "%2" or id like "%4" or id like "%6" or id like "%8");

select * from orders
where (order_time >= "2017-02-01")
and customer_id in (2,4,6,8);

select * from customers
where last_name like "%ar%";


select distinct coffee_origin from products
order by coffee_origin;

select distinct customer_id, product_id from orders
where order_time between "2017-02-01" and "2017-02-28"
order by customer_id;


select * from customers
limit 5;


select * from customers
limit 5 offset 6;


select name as name1, coffee_origin as country from products;

select distinct last_name from customers
order by last_name;

select * from orders
where customer_id = 1 
and order_time between "2017-02-01" and "2017-02-28"
order by order_time asc
limit 3;

select name, price as retails_price, coffee_origin from products; 



