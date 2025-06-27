# 📘 MySQL User Management and Relational Database Concepts

This document provides a beginner-friendly reference to essential MySQL operations and database concepts. Learn how to create users, manage access, and understand key relational principles such as primary keys, foreign keys, constraints, and complex queries.

---

## 🧑‍💻 How to Create a New MySQL User

To create a new user in MySQL:

```sql
CREATE USER 'new_user'@'localhost' IDENTIFIED BY 'secure_password';
```

You can replace `'localhost'` with `'%'` to allow remote access or specify a particular host.

---

## 🔐 How to Manage Privileges for a User

Grant permissions to a user for a specific database or table:

```sql
GRANT ALL PRIVILEGES ON database_name.* TO 'new_user'@'localhost';
```

For read-only access:

```sql
GRANT SELECT ON database_name.table_name TO 'new_user'@'localhost';
```

Apply changes:

```sql
FLUSH PRIVILEGES;
```

Revoke permissions:

```sql
REVOKE INSERT, UPDATE ON database_name.table_name FROM 'new_user'@'localhost';
```

---

## 🔑 What’s a PRIMARY KEY?

A **Primary Key** uniquely identifies each row in a table. It must be:

- Unique
- NOT NULL

Example:

```sql
CREATE TABLE users (
  id INT PRIMARY KEY,
  name VARCHAR(100)
);
```

---

## 🔗 What’s a FOREIGN KEY?

A **Foreign Key** links two tables and enforces referential integrity.

Example:

```sql
CREATE TABLE orders (
  id INT PRIMARY KEY,
  user_id INT,
  FOREIGN KEY (user_id) REFERENCES users(id)
);
```

---

## ❗ NOT NULL and UNIQUE Constraints

- `NOT NULL`: Column cannot contain `NULL` values
- `UNIQUE`: Ensures all values in a column are different

Example:

```sql
CREATE TABLE employees (
  email VARCHAR(100) NOT NULL UNIQUE,
  name VARCHAR(100)
);
```

---

## 🔍 Retrieve Data from Multiple Tables in One Request

Use JOIN to combine data:

```sql
SELECT users.name, orders.id
FROM users
JOIN orders ON users.id = orders.user_id;
```

---

## 🔁 What Are Subqueries?

A **Subquery** is a query inside another query.

Example:

```sql
SELECT name
FROM users
WHERE id IN (
  SELECT user_id
  FROM orders
  WHERE amount > 100
);
```

---

## 🔗 JOIN vs. UNION

### JOIN
Combines rows from related tables:

- `INNER JOIN`: Only matching rows
- `LEFT JOIN`: All rows from the left + matches
- `RIGHT JOIN`: All rows from the right + matches
- `FULL OUTER JOIN`: All rows from both tables (if supported)

```sql
SELECT users.name, orders.amount
FROM users
LEFT JOIN orders ON users.id = orders.user_id;
```

### UNION
Combines results of two `SELECT` statements:

```sql
SELECT name FROM customers
UNION
SELECT name FROM suppliers;
```

Requirements:
- Same number of columns
- Compatible data types

---

## 📚 Summary

| Concept            | Description                                             |
|--------------------|---------------------------------------------------------|
| CREATE USER        | Adds a new MySQL user                                   |
| GRANT / REVOKE     | Manages user permissions                                |
| PRIMARY KEY        | Uniquely identifies records                             |
| FOREIGN KEY        | Links tables and enforces relationships                 |
| NOT NULL / UNIQUE  | Ensures data integrity and uniqueness                   |
| JOIN               | Combines rows based on relationships                    |
| SUBQUERY           | A query within another query                            |
| UNION              | Merges results from multiple queries                    |

---

🛠️ Feel free to fork, modify, or contribute to this reference!
