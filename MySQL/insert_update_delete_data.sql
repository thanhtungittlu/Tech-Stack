use coffee_store;

show tables;

select * from products;

insert into products(name, price, coffee_origin)
values ("Espresso", 2.50, "Brazil");

insert into products(name, price, coffee_origin)
values ("Late", 3.50, "Costa rica"), 
	("Americo", 3.50, "Brazil"),
    ("Flat white", 3.50, "Spain"), 
    ("Fliter", 3.50, "Indonesia"), 
    ("Trung Nguyên", 6.0, "VietNam");

-- update

update products
set coffee_origin = "India"
where id = 3;

-- Mặc định where chỉ dùng được cho khóa chính.
-- Tuy nhiên có thể thay đổi bằng cách dùng lệnh dưới.

set SQL_SAFE_UPDATES = 0;

update products
set price = 4.0, coffee_origin = "India"
where name = "Flat white";


-- delete

delete from products
where id = 3;

select * from orders;

describe orders;
describe products;








	
