# 📘 MySQL Basics – Database and SQL Concepts

This repository contains scripts and examples to learn and practice the basics of SQL using MySQL. It includes creating databases and tables, querying data, and using functions and subqueries.

---

## 📚 General Concepts

| Concept                        | Description |
|-------------------------------|-------------|
| **What’s a Database**         | A database is an organized collection of data that allows efficient storage, access, and management. |
| **What’s a Relational DB**    | A relational database stores data in tables with rows and columns. Tables relate through primary and foreign keys. |
| **What Does SQL Stand For?**  | SQL stands for *Structured Query Language*. It’s used to manage and manipulate relational databases. |
| **What’s MySQL?**             | MySQL is an open-source RDBMS that uses SQL. It's commonly used in web applications and enterprise systems. |

---

## 🔨 Common SQL Operations

| Operation                    | Example |
|-----------------------------|---------|
| **Create a Database**       | `CREATE DATABASE database_name;` |
| **DDL (Definition)**        | `CREATE`, `ALTER`, `DROP` – Defines/modifies structure |
| **DML (Manipulation)**      | `SELECT`, `INSERT`, `UPDATE`, `DELETE` – Manipulates data |
| **Create a Table**          | <pre>CREATE TABLE users (  <br>id INT AUTO_INCREMENT PRIMARY KEY,<br>name VARCHAR(100),<br>email VARCHAR(100));</pre> |
| **Alter a Table**           | `ALTER TABLE users ADD COLUMN age INT;` |
| **Select Data**             | `SELECT name, email FROM users WHERE age > 25;` |
| **Insert Data**             | `INSERT INTO users (name, email, age) VALUES ('Alice', 'alice@example.com', 30);` |
| **Update Data**             | `UPDATE users SET age = 31 WHERE name = 'Alice';` |
| **Delete Data**             | `DELETE FROM users WHERE name = 'Alice';` |
| **Subqueries**              | `SELECT name FROM users WHERE id IN (SELECT user_id FROM orders WHERE total > 100);` |
| **MySQL Functions**         | <pre>SELECT UPPER(name);<br>SELECT ROUND(score, 2);<br>SELECT NOW();</pre> |

---

## 📂 Files in This Repository

| File Name              | Description                           |
|------------------------|---------------------------------------|
| `0-list_databases.sql` | Script to list all databases in MySQL |

---

## 🧠 Author

| Name                | Links |
|---------------------|-------|
| **Jimmy Carrera Otero** | [GitHub](https://github.com/Jcarrera007) • [LinkedIn](https://www.linkedin.com/in/jimmy-carrera-a62452268/) |

