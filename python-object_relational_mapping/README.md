# 📊 Python & MySQL Integration Guide

This repository demonstrates how to interact with a MySQL database using Python, including direct SQL execution and Object Relational Mapping (ORM) with SQLAlchemy.

---

## 🔌 How to Connect to a MySQL Database from a Python Script

Install the MySQL connector:

```bash
pip install mysql-connector-python
```

Basic connection example:

```python
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)

cursor = conn.cursor()
print("Connected to MySQL!")
```

---

## 📅 How to SELECT Rows in a MySQL Table from a Python Script

```python
cursor.execute("SELECT * FROM your_table")

for row in cursor.fetchall():
    print(row)
```

---

## 📄 How to INSERT Rows in a MySQL Table from a Python Script

```python
query = "INSERT INTO your_table (column1, column2) VALUES (%s, %s)"
values = ("value1", "value2")

cursor.execute(query, values)
conn.commit()
print(f"{cursor.rowcount} row(s) inserted.")
```

---

## 🧠 What ORM Means

**ORM** stands for **Object Relational Mapping**. It is a programming technique used to convert data between incompatible systems—in this case, between Python objects and relational database tables.

ORM allows developers to interact with the database using Python classes instead of writing raw SQL queries.

---

## 🐄 How to Map a Python Class to a MySQL Table Using SQLAlchemy

Install SQLAlchemy and MySQL driver:

```bash
pip install sqlalchemy pymysql
```

Define your ORM model:

```python
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(100))

# Connect to MySQL
engine = create_engine("mysql+pymysql://user:password@localhost/your_database")
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Add a new user
new_user = User(name="John Doe", email="john@example.com")
session.add(new_user)
session.commit()
```

---

## 🛠️ Project Structure (Example)

```
mysql_python_project/
│
├── main.py                 # Script with MySQL operations
├── orm_model.py            # SQLAlchemy ORM models
├── config.py               # MySQL credentials and setup
└── README.md               # This guide
```

---

## 📚 References

* [MySQL Connector for Python](https://dev.mysql.com/doc/connector-python/en/)
* [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
