import os
import mysql.connector
import mysql
import datetime

now = datetime.datetime.now()

def product_mgmt():
    print("\t\t\t 1. Add New Product")
    print("\t\t\t 2. List Product")
    print("\t\t\t 3. Update Product")
    print("\t\t\t 4. Delete Product")
    print("\t\t\t 5. Back (Main Menu)")
    p = input("\t\t Enter Your Choice :")
    if p == '1':
        add_product()
    elif p == '2':
        search_product()
    elif p == '3':
        update_product()
    elif p == '4':
        delete_product()
    else :
        main()

def purchase_mgmt():
        print("\t\t\t 1. Add Order")
        print("\t\t\t 2. List Order")
        print("\t\t\t 3. Back (Main Menu)")
        o = input("\t\t Enter Your Choice :")
        if o == '1':
            add_order()
        elif o == '2':
            list_order()
        else :
            main()
            
def sales_mgmt():
        print("\t\t\t 1. Sales Items")
        print("\t\t\t 2. List Sales")
        print("\t\t\t 3. Back (Main Menu)")
        s = input("\t\t Enter Your Choice :")
        if s == '1':
            sale_product()
        elif s == '2':
            list_sales()

        else:
            main()

def user_mgmt():
        print("\t\t\t 1. Add user")
        print("\t\t\t 2. List user")
        print("\t\t\t 3. Back (Main Menu)")
        u = input("\t\t Enter Your Choice :")
        if u == '1':
            add_user()
        elif u == '2':
            list_user()
        else:
            main()


def create_database():
    mydb = mysql.connector.connect(host="localhost", user="root", password="Inc0rr3ct@123", database="stock")
    mycursor = mydb.cursor()
    print("Creating PRODUCT table")
    sql = "CREATE TABLE if not exists product(pcode int(4) PRIMARY KEY,pname char(30) NOT NULL,price float(8,2),pqty int(4),pcat char(30));"
    mycursor.execute(sql)
    print("Creating ORDER table")
    sql = "CREATE TABLE if not exists orders(orderid int(4) PRIMARY KEY,orderdate DATE,pcode char(30) NOT NULL,pprice float(8,2),pqty int(4),psupplier char(50),pcat char(30));"
    mycursor.execute(sql)
    print("ORDER table created")
    print("Creating SALES table")
    sql = "CREATE TABLE if not exists sales(salesid int(4),salesdate DATE,pcode char(30) references product(pcode),pprice float(8,2),pqty int(4),Total double(8,2));"
    mycursor.execute(sql)
    print("SALES table created")
    sql = "CREATE TABLE if not exists user(uid char(40) PRIMARY KEY,uname char(30) NOT NULL,upwd char(30));"
    mycursor.execute(sql)
    print("USER table created")

def list_database():
    mydb = mysql.connector.connect(host="localhost", user="root", password="Inc0rr3ct@123", database="stock")
    mycursor = mydb.cursor()
    sql = "show tables;"
    mycursor.execute(sql)

    for i in mycursor:
        print(i)


def add_order():
    mydb = mysql.connector.connect(host="localhost", user="root", password="Inc0rr3ct@123", database="stock")
    mycursor = mydb.cursor()
    now = datetime.datetime.now()
    sql = "INSERT INTO orders (orderid, orderdate, pcode, pprice, pqty, psupplier, pcat) values(%s,%s,%s,%s,%s,%s,%s)"
    code = int(input("Enter product code :"))
    old = now.year + now.month + now.day + now.hour + now.minute + now.second
    qty = input("Enter product quantity : ")
    price = input("Enter Product unit price: ")
    cat = input("Enter product category: ")
    supplier = input("Enter Supplier details: ")
    val = (old, now, code, price, qty, supplier, cat)
    mycursor.execute(sql)
    mydb.commit()

def list_order():
    mydb = mysql.connector.connect(host="localhost", user="root", password="Inc0rr3ct@123", database="stock")
    mycursor = mydb.cursor()
    sql = "SELECT * from orders;"
    mycursor.execute(sql)
    print("\t\t\t\t\t\t\t ORDER DETAILS")
    print("-" * 85)
    for i in mycursor:
        print(i[0], "\t", i[1], "\t", i[2], "\t", i[3], "\t", i[4], "\t", i[5], "\t", i[6])
        print("-" * 85)


def db_mgmt():
        print("\t\t\t 1. Database creation")
        print("\t\t\t 2. List Database")
        print("\t\t\t 3. Back (Main Menu)")
        p = input("\t\t Enter Your Choice :")
        if p == '1':
            create_database()
        elif p == '2':
            list_database()
        else :
            main()

def add_product():
    mydb = mysql.connector.connect(host="localhost", user="root", password="Inc0rr3ct@123", database="stock")
    mycursor = mydb.cursor()
    sql = "INSERT INTO product(pcode,pname,price,pqty,pcat) values(%s,%s,%s,%s,%s)"
    code = input("\t\t Enter product code :")
    search = "SELECT count(*) FROM product WHERE pcode=%s;"
    val = (code,)
    mycursor.execute(search, val)
    for x in mycursor:
        cnt = x[0]
        if cnt == 0:
            name = input("\t\t Enter product name :")
            qty = input("\t\t Enter product quantity :")
            price = input("\t\t Enter product unit price :")
            cat = input("\t\t Enter Product category :")
            val = (code, name, price, qty, cat)
            mycursor.execute(sql, val)
            mydb.commit()
        else:
            print("\t\t Product already exist")


def update_product():
    mydb = mysql.connector.connect(host="localhost", user="root", password="Inc0rr3ct@123", database="stock")
    mycursor = mydb.cursor()
    code = int(input("Enter the product code :"))
    qty = int(input("Enter the quantity :"))
    sql = "UPDATE product SET pqty=pqty+%s WHERE pcode=%s;"
    val = [qty, code]
    mycursor.execute(sql, val)
    mydb.commit()
    print("\t\t Product details updated")


def delete_product():
    mydb = mysql.connector.connect(host="localhost", user="root", password="Inc0rr3ct@123", database="stock")
    mycursor = mydb.cursor()
    code = int(input("Enter the product code :"))
    sql = "DELETE FROM product WHERE pcode = %s;"
    val = (code)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted");


def search_product():
    while True:
        print("\t\t\t 1. List all product")
        print("\t\t\t 2. List product code wise")
        print("\t\t\t 3. List product category wise")
        print("\t\t\t 4. Back (Main Menu)")
        s = input("\t\t Enter Your Choice :")
        if s == '1':
            list_product()
        if s == '2':
            code = int(input(" Enter product code :"))
            list_prcode(code)
        if s == '3':
            cat = input("Enter category :")
            list_prcat(cat)
        if s == '4':
            main()

def list_product():
    mydb = mysql.connector.connect(host="localhost", user="root", password="Inc0rr3ct@123", database="stock")
    mycursor = mydb.cursor()
    sql = "SELECT * from product"
    mycursor.execute(sql)
    print("\t\t\t\t PRODUCT DETAILS")
    print("\t\t", "-" * 47)
    print("\t\t code   name   price   quantity     category")
    print("\t\t", "-" * 47)
    for i in mycursor:
        print("\t\t", i[0], "\t", i[1], "\t", i[2], "\t", i[3], "\t", i[4])
        print("\t\t", "-" * 47)


def list_prcode(code):
    mydb = mysql.connector.connect(host="localhost", user="root", password="Inc0rr3ct@123", database="stock")
    mycursor = mydb.cursor()
    sql = "SELECT * from product WHERE pcode=%s"
    val = (code,)
    mycursor.execute(sql, val)
    print("\t\t\t\t PRODUCT DETAILS")
    print("\t\t", "-" * 47)
    print("\t\t code   name   price   quantity     category")
    print("\t\t", "-" * 47)
    for i in mycursor:
        print("\t\t", i[0], "\t", i[1], "\t", i[2], "\t", i[3], "\t\t", i[4])
        print("\t\t", "-" * 47)

def sale_product():
    mydb = mysql.connector.connect(host="localhost", user="root", password="Inc0rr3ct@123", database="stock")
    mycursor = mydb.cursor()
    pcode = input("Enter product code: ")
    sql = "SELECT count(*) from product WHERE pcode=%s;"
    val = (pcode,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    for x in myresult:
        cnt = x[0]
        if cnt != 0:
            sql = "SELECT * from product WHERE pcode=%s;"
            val = (pcode,)
            mycursor.execute(sql, val)
    for x in mycursor:
        print(x[0], "\t", x[1], "\t", x[2], "\t", x[3], "\t\t", x[4])
        print("-" * 80)
        price = x[2]
        pqty = x[3]
        qty = int(input("Enter no of quantity :"))
        if qty <= pqty:
            total = qty * price
            print("Collect Rs. ", total)
            sql = "INSERT into sales values(%s,%s,%s,%s,%s,%s)"
            abc=int(cnt) + 1
            val = (abc, datetime.datetime.now(), pcode, price, qty, total)
            mycursor.execute(sql, val)
            sql = "UPDATE product SET pqty=pqty-%s WHERE pcode=%s"
            val = (qty, pcode)
            mycursor.execute(sql, val)
            mydb.commit()
        else:
            print("Product is not available")

def list_sales():
    mydb = mysql.connector.connect(host="localhost", user="root", password="Inc0rr3ct@123", database="stock")
    mycursor = mydb.cursor()
    sql = "SELECT * FROM sales"
    mycursor.execute(sql)
    print("\t\t\t\t SALES DETAILS")
    print("-" * 80)
    print("Sales ID    Date   Product Code    Price     Quantity    Total")
    print("-" * 80)
    for x in mycursor:
        print(x[0], "\t", x[1], "\t", x[2], "\t", x[3], "\t\t", x[4], "\t\t", x[5])
    print("-" * 80)

def list_prcat(cat):
    mydb = mysql.connector.connect(host="localhost", user="root", password="Inc0rr3ct@123", database="stock")
    mycursor = mydb.cursor()
    print(cat)
    sql = "SELECT * from product WHERE pcat =%s"
    val = (cat,)
    mycursor.execute(sql, val)
    clrscr()
    print("\t\t\t\t PRODUCT DETAILS")
    print("\t\t", "-" * 47)
    print("\t\t code    name    price   quantity    category")
    print("\t\t", "-" * 47)
    for i in mycursor:
        print("\t\t", i[0], "\t", i[1], "\t", i[2], "\t", i[3], "\t\t", i[4])
        print("\t\t", "-" * 47)


def add_user():
    mydb = mysql.connector.connect(host="localhost", user="root", password="Inc0rr3ct@123", database="stock")
    mycursor = mydb.cursor()
    uid = input("Enter email id :")
    name = input("Enter Name :")
    password = input("Enter Password :")
    sql = "INSERT INTO user(uid,uname,upwd) values (%s,%s,%s);"
    val = (uid, name, password)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "user created")


def list_user():
    mydb = mysql.connector.connect(host="localhost", user="root", password="Inc0rr3ct@123", database="stock")
    mycursor = mydb.cursor()
    sql = "SELECT uid, uname from user"
    mycursor.execute(sql)
    clrscr()
    print("\t\t\t\t USER DETAILS")
    print("\t\t", "-" * 27)
    print("\t\t UID        name   ")
    print("\t\t", "-" * 27)
    for i in mycursor:
        print("\t\t", i[0], "\t", i[1])
        print("\t\t", "-" * 27)


def clrscr():
    print("\n" * 5)


def main ():
    print("\t\t\t STOCK MANAGEMENT")
    print("\t\t\t **************************\n")
    print("\t\t\ 1. PRODUCT MANAGEMENT")
    print("\t\t\ 2. PURCHASE MANAGEMENT")
    print("\t\t\ 3. SALES MANAGEMENT")
    print("\t\t\ 4. USER MANAGEMENT")
    print("\t\t\ 5. DATABASE SETUP")
    print("\t\t\ 6. EXIT\n")
    n = input("Enter your choice :")
    if n == '1':
      product_mgmt()
    elif n == '2':
        os.system('cls')
        purchase_mgmt()
    elif n == '3':
        sales_mgmt()
    elif n == '4':
        user_mgmt()
    elif n == '5':
        db_mgmt()
    else :
         print("\t Incorrect choice")

main()
