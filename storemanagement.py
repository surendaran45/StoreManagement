import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="store_db"
)

cur = con.cursor()

def insert_emp():
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    gender = input("Enter Gender: ")
    salary = float(input("Enter Salary: "))
    cur.execute("INSERT INTO emp_details VALUES (%s,%s,%s,%s,%s)",
                (emp_id, name, phone, gender, salary))
    con.commit()
    print("Employee Added\n")

def update_emp():
    emp_id = int(input("Enter Employee ID to Update: "))
    new_salary = float(input("Enter New Salary: "))
    cur.execute("UPDATE emp_details SET salary=%s WHERE emp_id=%s",
                (new_salary, emp_id))
    con.commit()
    print("Employee Updated\n")

def delete_emp():
    emp_id = int(input("Enter Employee ID to Delete: "))
    cur.execute("DELETE FROM emp_details WHERE emp_id=%s", (emp_id,))
    con.commit()
    print("Employee Deleted\n")

def view_emp():
    cur.execute("SELECT * FROM emp_details")
    print("\nEMPLOYEE DETAILS")
    for row in cur.fetchall():
        print(row)
    print()

def insert_stock():
    sid = int(input("Enter Stock ID: "))
    name = input("Enter Stock Name: ")
    price = int(input("Enter Stock Price: "))
    qty = int(input("Enter Stock Quantity: "))
    cur.execute("INSERT INTO stock VALUES (%s,%s,%s,%s)",
                (sid, name, price, qty))
    con.commit()
    print("Stock Added\n")

def update_stock():
    sid = int(input("Enter Stock ID to Update: "))
    price = int(input("Enter New Price: "))
    cur.execute("UPDATE stock SET stock_price=%s WHERE stock_id=%s",
                (price, sid))
    quant = int(input("Enter New Quantity: "))
    cur.execute("UPDATE stock SET stock_quantity=%s WHERE stock_id=%s",
                (quant, sid))
    con.commit()
    print("Stock Updated\n")

def delete_stock():
    sid = int(input("Enter Stock ID to Delete: "))
    cur.execute("DELETE FROM stock WHERE stock_id=%s", (sid,))
    con.commit()
    print("Stock Deleted\n")

def view_stock():
    cur.execute("SELECT * FROM stock")
    print("\nSTOCK DETAILS")
    for row in cur.fetchall():
        print(row)
    print()

def insert_customer():
    cid = int(input("Enter Customer ID: "))
    name = input("Enter Customer Name: ")
    amt = int(input("Enter Amount: "))
    date = input("Enter Purchase Date (YYYY-MM-DD HH:MM:SS): ")
    cur.execute("INSERT INTO customer VALUES (%s,%s,%s,%s)",
                (cid, name, amt, date))
    con.commit()
    print("Customer Added\n")

def update_customer():
    cid = int(input("Enter Customer ID to Update: "))
    amt = int(input("Enter New Amount: "))
    cur.execute("UPDATE customer SET amt=%s WHERE c_id=%s",
                (amt, cid))
    con.commit()
    print("Customer Updated\n")

def delete_customer():
    cid = int(input("Enter Customer ID to Delete: "))
    cur.execute("DELETE FROM customer WHERE c_id=%s", (cid,))
    con.commit()
    print("Customer Deleted\n")

def view_customer():
    cur.execute("SELECT * FROM customer")
    print("\nCUSTOMER DETAILS")
    for row in cur.fetchall():
        print(row)
    print()

def total_purchase():
    cid = int(input("Enter Customer ID: "))
    cur.execute("SELECT SUM(amt) FROM customer WHERE c_id=%s", (cid,))
    total = cur.fetchone()[0]
    print("\nTotal Purchase Amount =", total if total else 0, "\n")

while True:
    print("1. Insert Employee")
    print("2. Update Employee")
    print("3. Delete Employee")
    print("4. View All Employees")
    print("5. Insert Stock")
    print("6. Update Stock")
    print("7. Delete Stock")
    print("8. View Stock")
    print("9. Insert Customer")
    print("10. Update Customer")
    print("11. Delete Customer")
    print("12. View Customers")
    print("13. Find Total Purchase Amount")
    print("14. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        insert_emp()
    elif ch == 2:
        update_emp()
    elif ch == 3:
        delete_emp()
    elif ch == 4:
        view_emp()
    elif ch == 5:
        insert_stock()
    elif ch == 6:
        update_stock()
    elif ch == 7:
        delete_stock()
    elif ch == 8:
        view_stock()
    elif ch == 9:
        insert_customer()
    elif ch == 10:
        update_customer()
    elif ch == 11:
        delete_customer()
    elif ch == 12:
        view_customer()
    elif ch == 13:
        total_purchase()
    elif ch == 14:
        print("Exiting...")
        break
    else:
        print("Invalid Choice\n")
