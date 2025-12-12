# Stock Management System

A Python + MySQL mini project used to manage stock items, monitor quantities, update prices, and track overall inventory status.  
This project provides full CRUD operations and is suitable for academic submissions and real-world small shop automation.

---

## 🚀 Features

### 1. Stock Item Management
- Add new stock items  
- Each item includes: ID, name, price, and quantity  
- Update price and quantity easily  
- Delete any stock item  
- View all items in a tabular format  

### 2. Inventory Control
- Low-quantity alerts (optional enhancement)  
- Prevent inserting duplicate IDs  
- Automatically track available stock levels  

### 3. User Input–Based Operations
All insert, update, delete, and view actions are performed using user input in Python.

---

## 🗂️ Database Structure (MySQL)

### **stock Table**
| Column         | Type        |
|----------------|-------------|
| stock_id       | INT (PK)    |
| stock_name     | VARCHAR(30) |
| stock_price    | INT         |
| stock_quantity | INT         |

---

## 🛠️ Technologies Used
- **Python 3**
- **MySQL**
- **mysql-connector-python** library

Install connector:
```bash
pip install mysql-connector-python
