from database.db import PRODUCTS, CUSTOMERS, ORDERS
# from playhouse.shortcuts import model_to_dict, dict_to_model


# list_product = PRODUCTS.select()

# for product in list_product:
#     print(product.name)


# list_customers = CUSTOMERS.select()

# for customer in list_customers:
#     print(customer.first_name)

# list_orders = ORDERS.select()
# # json_data = json.dumps(model_to_dict(list_orders))

# # print(json_data)

# for order in list_orders:
#     print(model_to_dict(order))



""" 
    select * from products
    where price = 3.00
    and coffee_origin = "Brazil" 
=> and: &
=> or: |
"""
# querry = PRODUCTS.select().where((PRODUCTS.price == 3) & (PRODUCTS.coffee_origin == "Brazil"))

    

"""
select * from products
where price >= 3 ;   
"""
# querry = PRODUCTS.select().where((PRODUCTS.price >= 3))



"""
select * from customers
where phone_number is null ;   
"""
# querry = CUSTOMERS.select().where((CUSTOMERS.phone_number.is_null(True)))




"""
select * from customers
where phone_number is not null ;  
"""
# querry = CUSTOMERS.select().where((CUSTOMERS.phone_number.is_null(False)))



"""
select first_name, phone_number from customers
where gender = "F"
and last_name = "Bluth";
"""
# querry = CUSTOMERS.select(CUSTOMERS.first_name, CUSTOMERS.phone_number) \
#         .where( (CUSTOMERS.gender == "F" ) & (CUSTOMERS.last_name == "Bluth") )






"""
select name from products
where price > 3
or coffee_origin = "Brazil";
"""
# querry = PRODUCTS.select(PRODUCTS.name) \
#         .where( (PRODUCTS.price > 3 ) | (PRODUCTS.coffee_origin == "Brazil") )




"""
select id from customers
where phone_number is null
and gender = "M";
"""
# querry = CUSTOMERS.select(CUSTOMERS.id) \
#         .where( (CUSTOMERS.phone_number.is_null(True) ) & (CUSTOMERS.gender == "M") )







"""
select * from customers
where last_name in ("Taylor","Bluth")
and first_name not in ("Sarah");
"""
# querry = CUSTOMERS.select() \
#         .where( ( CUSTOMERS.last_name.in_(["Taylor","Bluth"]) ) & (CUSTOMERS.first_name.not_in(["Sarah"]) ) )




"""
select * from orders
where order_time between "2017-01-01" and "2017-07-01";
"""

# querry = CUSTOMERS.select() \
#         .where( ( CUSTOMERS.last_name.in_(["Taylor","Bluth"]) ) & (CUSTOMERS.first_name.not_in(["Sarah"]) ) )




"""
select * from orders
where id between 100 and 130;
"""
# querry = ORDERS.select() \
#         .where(  ORDERS.id.between(100,139)  )



"""
select * from customers
where last_name like "W%";
"""
# querry = CUSTOMERS.select() \
#         .where(  CUSTOMERS.last_name.like("W%")  )




"""
select * from customers
where last_name like "%o%";
"""
# querry = CUSTOMERS.select() \
#         .where(  CUSTOMERS.last_name.like("%o%")  )





"""
select * from products
where price like "3%";
"""
# querry = PRODUCTS.select() \
#         .where(  PRODUCTS.price.like("3%")  )



"""
select * from customers
order by first_name asc; 
"""
# querry = CUSTOMERS.select() \
#         .order_by(CUSTOMERS.first_name.asc())



"""
select * from customers
order by first_name desc; -- Ngược chiều
"""
# querry = CUSTOMERS.select() \
#         .order_by(CUSTOMERS.first_name.desc())




"""
select * from products
where coffee_origin in ("Brazil","Indonesia")
order by name asc;
"""

# querry = PRODUCTS.select() \
#         .where(PRODUCTS.coffee_origin.in_(["Brazil","Indonesia"])) \
#         .order_by(PRODUCTS.name.asc())



"""
select * from orders
where (order_time >= "2017-02-01")
and (id like "%2" or id like "%4" or id like "%6" or id like "%8");
"""
# querry = ORDERS.select() \
#         .where( (ORDERS.order_time >= "2017-02-01") & ( (ORDERS.id.like("%2")) | (ORDERS.id.like("%4")) | (ORDERS.id.like("%6")) | (ORDERS.id.like("%8")) ) )


"""
select * from orders
where (order_time >= "2017-02-01")
and customer_id in (2,4,6,8);
"""
# querry = ORDERS.select() \
#         .where( (ORDERS.order_time >= "2017-02-01") & ( ORDERS.customer_id.in_(["2","4","6","8"])  ) )




"""
select * from customers
where last_name like "%ar%";
"""
# querry = CUSTOMERS.select() \
#         .where( CUSTOMERS.last_name.contains("ar") )  




"""
select distinct coffee_origin from products
order by coffee_origin;
"""

# querry = PRODUCTS.select(PRODUCTS.coffee_origin.distinct()) \
#         .order_by( PRODUCTS.coffee_origin)  




"""
select distinct customer_id, product_id from orders
where order_time between "2017-02-01" and "2017-02-28"
order by customer_id;
"""

# querry = ORDERS.select(ORDERS.customer_id.distinct(), ORDERS.product_id) \
#         .where(ORDERS.order_time.between("2017-02-01","2017-02-28")) \
#         .order_by( ORDERS.customer_id)  




"""
select * from customers
limit 5;
"""
querry = CUSTOMERS.select() \
        .limit(5)



"""
select * from customers
limit 5 offset 6;
"""
# querry = CUSTOMERS.select() \
#         .limit(5)\
#         .offset(6)




"""
select name as name1, coffee_origin as country from products;
"""
# querry = PRODUCTS.select(PRODUCTS.name.alias("name1"), PRODUCTS.coffee_origin.alias("country"))





"""
select distinct last_name from customers
order by last_name;
"""
# querry = CUSTOMERS.select(CUSTOMERS.last_name.distinct()) \
#         .order_by(CUSTOMERS.last_name)\



"""
select * from orders
where customer_id = 1 
and order_time between "2017-02-01" and "2017-02-28"
order by order_time asc
limit 3;
"""
# querry = ORDERS.select() \
#         .where( (ORDERS.customer_id == 1) & (ORDERS.order_time.between("2017-02-01","2017-02-28")) ) \
#         .order_by(ORDERS.order_time)\
#         .limit(3)



"""
select name, price as retails_price, coffee_origin from products; 
"""
# querry = PRODUCTS.select(PRODUCTS.name, PRODUCTS.price.alias("retails_price"), PRODUCTS.coffee_origin) 
        



"""
---------------------------JOIN
"""

"""
select products.name, orders.order_time from orders 
inner join products on orders.product_id = products.id;
"""

querry = (ORDERS.select().join(
    PRODUCTS, on = (ORDERS.product_id == PRODUCTS.id) ))

dataDict = list(querry.dicts()) 
for data in querry:
    print(data)
