# 🐍 Understanding Python Objects: Mutability, References, and More

This repository explores Python's object model and fundamental concepts like mutability, object identity, and how variables are passed to functions. Understanding these principles will help you write better, more predictable Python code.

---

## 📘 Table of Contents

* [What is an Object?](#what-is-an-object)
* [Class vs Object (Instance)](#class-vs-object-instance)
* [Mutable vs Immutable Objects](#mutable-vs-immutable-objects)
* [What is a Reference?](#what-is-a-reference)
* [Assignment in Python](#assignment-in-python)
* [What is an Alias?](#what-is-an-alias)
* [Object Identity](#object-identity)
* [Mutable and Immutable Types](#mutable-and-immutable-types)
* [How Python Passes Variables to Functions](#how-python-passes-variables-to-functions)
* [Examples](#examples)

---

## 🔹 What is an Object?

In Python, **everything is an object**. This includes integers, strings, functions, classes, modules, and even types themselves.

Every object has:

* **Identity** (memory address)
* **Type** (determines what kind of object it is)
* **Value** (the actual data stored)

---

## 🔹 Class vs Object (Instance)

* A **class** is a blueprint for creating objects.
* An **object** (or **instance**) is a specific realization of a class.

```python
class Dog:
    def bark(self):
        print("Woof!")

fido = Dog()  # fido is an instance of the Dog class
```

---

## 🔹 Mutable vs Immutable Objects

* **Mutable objects** can be changed after creation (e.g. lists).
* **Immutable objects** cannot be changed once created (e.g. strings, integers).

---

## 🔹 What is a Reference?

A **reference** is a pointer to an object in memory. When you assign a variable, you're creating a reference to that object — not a copy.

```python
a = [1, 2, 3]
b = a  # b now references the same list as a
```

---

## 🔹 Assignment in Python

Assignment does **not copy** an object. It creates a new reference to the same object in memory.

```python
x = [1, 2]
y = x  # Both refer to the same list
```

---

## 🔹 What is an Alias?

When two variables reference the same object, they are **aliases** of each other.

---

## 🔹 Object Identity

To check if two variables point to the **same object**, use the `is` keyword or the `id()` function.

```python
a = [1, 2]
b = a
print(a is b)          # True
print(id(a) == id(b))  # True
```

---

## 🔹 Mutable and Immutable Types

### ✅ Built-in Mutable Types:

* `list`
* `dict`
* `set`
* `bytearray`
* Custom objects (usually)

### 🔒 Built-in Immutable Types:

* `int`
* `float`
* `str`
* `tuple`
* `frozenset`
* `bytes`

---

## 🔹 How Python Passes Variables to Functions

Python uses **"pass-by-object-reference"** (or "pass-by-assignment"). The function receives a reference to the object — not a copy.

* If the object is **mutable**, the function can modify it.
* If the object is **immutable**, changes inside the function won't affect the original.

```python
def modify(lst):
    lst.append(4)

nums = [1, 2, 3]
modify(nums)
print(nums)  # [1, 2, 3, 4] — the list is modified
```

```python
def update(x):
    x = x + 10

a = 5
update(a)
print(a)  # 5 — original integer unchanged
```

---

## 📌 Examples

### Checking if two variables point to the same object:

```python
a = [1, 2]
b = a
print(a is b)  # True
```

### Getting an object's identifier (memory address in CPython):

```python
print(id(a))
```

---

## 📚 Summary

| Concept         | Description                                           |
| --------------- | ----------------------------------------------------- |
| Object          | Everything in Python                                  |
| Class vs Object | Class is a blueprint; object is an instance           |
| Mutable         | Can be changed in-place                               |
| Immutable       | Cannot be changed after creation                      |
| Reference       | Points to an object in memory                         |
| Assignment      | Binds a variable to an object                         |
| Alias           | Multiple variables referencing the same object        |
| `id()`          | Returns object’s identity (memory address in CPython) |
| `is`            | Checks object identity                                |

---

## 🐍 Happy Pythoning!
