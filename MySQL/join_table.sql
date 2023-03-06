select products.name, orders.order_time from orders 
inner join products on orders.product_id = products.id;

select p.name, p.price, o.order_time from orders o
join products p on o.product_id = p.id
order by p.price desc;

-- left join
select * from orders;
select * from customers;

update orders
set customer_id = null
where id = 103;

select o.id, c.phone_number, c.last_name, o.order_time from customers c 
left join orders o on c.id = o.customer_id
order by o.order_time
limit 10;

select o.id, c.phone_number, c.last_name, o.order_time from orders o  
left join customers c on  o.customer_id = c.id 
order by o.order_time
limit 10;


-- right join

select o.id, c.phone_number, c.last_name, o.order_time from customers c 
right join orders o on c.id = o.customer_id
order by o.order_time
limit 10;

select o.id, c.phone_number, c.last_name, o.order_time from orders o  
right join customers c on  o.customer_id = c.id 
order by o.order_time
limit 10;


-- join many table
select p.name as name_coffee, c.last_name , p.price, o.order_time from orders o
join products p on o.product_id = p.id
join customers c on c.id = o.customer_id
order by o.order_time;



select o.id, c.phone_number from orders o 
join customers c on o.customer_id = c.id
where o.product_id = 4;

select p.name, o.order_time from products p
join orders o on p.id = o.product_id
where p.name = "Flinter"
and o.order_time between "2017-01-15" and "2017-02-14";


select p.name as name_coffee, p.price, o.order_time from orders o
join products p on o.product_id = p.id
join customers c on c.id = o.customer_id
where c.gender = "F" 
and o.order_time between "2017-01-01" and "2017-01-31";
