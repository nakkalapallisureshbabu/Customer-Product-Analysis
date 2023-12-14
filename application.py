from bottle import route, post, run, template, redirect, request
import database

# Initialize the database
database.initialize_database()

@route("/")
def get_index():
    redirect("/customers")

@route("/customers")
def get_customers():
    customers = database.get_all_customers()
    return template("customers.tpl", customers=customers)

@route("/customers/add")
def get_add_customer():
    return template("add_customer.tpl")

@post("/customers/add")
def post_add_customer():
    name = request.forms.get("name")
    email = request.forms.get("email")
    database.add_customer(name, email)
    redirect("/customers")

@route("/customers/<customer_id>")
def get_customer_details(customer_id):
    customer = database.get_customer_details(customer_id)
    return template("customer_details.tpl", customer=customer)

@route("/customers/<customer_id>/update")
def get_update_customer(customer_id):
    customer = database.get_customer_details(customer_id)
    return template("update_customer.tpl", customer=customer)

@post("/customers/<customer_id>/update")
def post_update_customer(customer_id):
    name = request.forms.get("name")
    email = request.forms.get("email")
    database.update_customer(customer_id, name, email)
    redirect("/customers")

@route("/customers/<customer_id>/delete")
def get_delete_customer(customer_id):
    database.delete_customer(customer_id)
    redirect("/customers")

@route("/products")
def get_products():
    products = database.get_all_products()
    return template("products.tpl", products=products)

@route("/products/add")
def get_add_product():
    return template("add_product.tpl")

@post("/products/add")
def post_add_product():
    name = request.forms.get("name")
    price = request.forms.get("price")
    quantity = request.forms.get("quantity")
    database.add_product(name, price, quantity)
    redirect("/
