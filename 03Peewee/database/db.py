from peewee import *

# Connect to a MySQL database on network.
my_db = MySQLDatabase(
    database = "coffee_store",
    user='root', 
    password='01032023',
    host='127.0.0.1', 
    port=3306, 
)


class BaseModel(Model):
    class Meta:
        database = my_db

class PRODUCTS(BaseModel):
    id             = IntegerField(db_column='id', primary_key= True)
    name           = CharField(db_column='name')
    price          = DecimalField(db_column='price')
    coffee_origin  = CharField(db_column='coffee_origin')

    class Meta:
        db_table = 'products'


class CUSTOMERS(BaseModel):
    id             = IntegerField(db_column='id', primary_key= True)
    first_name     = TextField(db_column='first_name')
    last_name      = TextField(db_column='last_name')
    gender         = CharField(db_column='gender')
    phone_number   = CharField(db_column='phone_number')

    class Meta:
        db_table = 'customers'


class ORDERS(BaseModel):
    id              = IntegerField(db_column='id', primary_key= True)
    product_id      = ForeignKeyField(PRODUCTS, db_column='product_id', backref='id')
    customer_id     = ForeignKeyField(PRODUCTS, db_column='customer_id', backref='id')
    order_time      = DateTimeField (db_column='order_time')

    class Meta:
        db_table = 'orders'


