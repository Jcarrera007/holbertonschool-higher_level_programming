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
| `0-privileges.sql`     | Script to list all privileges of MySQL users user_0d_1 and user_0d_2 |
| `1-create_user.sql`    | Script to create a MySQL user |
| `2-create_read_user.sql` | Script to create a user with read privileges |
| `3-force_name.sql`     | Script to create a table with NOT NULL constraint |
| `4-never_empty.sql`    | Script to create a table with default values |
| `5-unique_id.sql`      | Script to create a table with unique constraint |
| `6-states.sql`         | Script to create states table |
| `7-cities.sql`         | Script to create cities table with foreign key |
| `8-cities_of_california_subquery.sql` | Script using subquery to find cities in California |
| `9-cities_by_state_join.sql` | Script using JOIN to list cities by state |
| `10-genre_id_by_show.sql` | Script to list shows with their genre IDs |
| `11-genre_id_all_shows.sql` | Script to list all shows including those without genres |
| `12-no_genre.sql`      | Script to list shows without any genre |
| `13-count_shows_by_genre.sql` | Script to count shows by genre |
| `14-my_genres.sql`     | Script to list genres of a specific show |
| `15-comedy_only.sql`   | Script to list comedy shows only |
| `16-shows_by_genre.sql` | Script to list shows by genre |

---

## 🧠 Author

| Name                | Links |
|---------------------|-------|
| **Jimmy Carrera Otero** | [GitHub](https://github.com/Jcarrera007) • [LinkedIn](https://www.linkedin.com/in/jimmy-carrera-a62452268/) |

