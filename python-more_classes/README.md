# Python Object-Oriented Programming (OOP) Essentials

Welcome to the Python OOP guide! This repository explores the fundamentals of Object-Oriented Programming in Python, with concise explanations and examples for each concept.

---

## 📌 Why Python Programming is Awesome

* Clean and readable syntax.
* Interpreted and dynamically typed.
* Huge standard library and ecosystem.
* Supports multiple paradigms (OOP, functional, procedural).
* "First-class everything" – everything is an object!

---

## 🧠 Object-Oriented Programming (OOP)

OOP is a paradigm that structures programs using classes and objects. It promotes code reusability, modularity, and abstraction.

---

## 🏗️ Core OOP Concepts in Python

### 🔹 What is a Class?

A blueprint for creating objects (instances), defining attributes and methods.

### 🔹 What is an Object or Instance?

A concrete instantiation of a class; holds actual data and can call methods.

### 🔹 Class vs Object

* **Class**: Blueprint.
* **Object**: Instance created from a class.

### 🔹 What is an Attribute?

A variable associated with a class or an object.

---

## 🔐 Attribute Visibility

### 🔹 Public, Protected, and Private Attributes

* `public_attr`: Accessible anywhere.
* `_protected_attr`: Meant for internal use (convention).
* `__private_attr`: Name-mangled to prevent direct access.

---

## 🔄 Special Variables and Methods

### 🔹 `self`

Represents the instance calling the method; used to access instance data.

### 🔹 `__init__`

Constructor method called automatically when a new object is created.

---

## 🧰 Advanced Concepts

### 🔹 Data Abstraction, Encapsulation, and Information Hiding

* **Abstraction**: Hiding complex logic behind simple interfaces.
* **Encapsulation**: Bundling data with the methods operating on it.
* **Information Hiding**: Restricting direct access to some components.

### 🔹 What is a Property?

An attribute accessed like a variable but implemented using methods (`@property`).

### 🔹 Attribute vs Property

* **Attribute**: Direct variable.
* **Property**: Controlled access using getter/setter logic.

### 🔹 Pythonic Getters and Setters

Use the `@property` and `@<property>.setter` decorators instead of explicit `get_`/`set_` methods.

---

## 👈 Custom String Representations

### 🔹 `__str__` vs `__repr__`

* `__str__`: Informal, user-friendly string (`print(obj)`).
* `__repr__`: Official, developer-facing representation (`repr(obj)`).

---

## 🏷️ Class and Instance Attributes

### 🔹 Class Attribute

Defined directly inside the class, shared across all instances.

### 🔹 Object (Instance) Attribute

Defined using `self`, unique to each instance.

### 🔹 Difference

Class attributes are shared; instance attributes are per object.

---

## 🧩️ Methods in Classes

### 🔹 Instance Method

The default method, requires `self`.

### 🔹 Class Method

Marked with `@classmethod`, receives `cls` (the class) as the first argument.

### 🔹 Static Method

Marked with `@staticmethod`, no `self` or `cls` required.

---

## ⚙️ Dynamic Attribute Management

### 🔹 Dynamically Create Attributes

```python
obj.new_attr = "I was added at runtime!"
```

### 🔹 Bind Attributes to Class or Object

Use `setattr()` or direct assignment:

```python
setattr(obj, 'age', 30)
```

---

## 📦 `__dict__` Attribute

### 🔹 What is `__dict__`?

A dictionary containing an object’s (or class’s) writable attributes.

```python
print(obj.__dict__)
```

---

## 🔎 Attribute Lookup and Introspection

### 🔹 How Python Finds Attributes

Python checks:

1. Instance attributes (`obj.__dict__`)
2. Class attributes (`obj.__class__.__dict__`)
3. Parent classes (method resolution order - MRO)

### 🔹 `getattr()` Function

Safely get an attribute value:

```python
getattr(obj, 'attr_name', default_value)
```

---

## 📂 Project Structure (example)

```text
project/
├── main.py
├── user.py
├── README.md
```
