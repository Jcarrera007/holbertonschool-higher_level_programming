# 🧠 Python Object-Oriented Programming (OOP) Concepts

This repository contains notes, examples, and explanations covering fundamental and advanced **Object-Oriented Programming (OOP)** concepts in Python.

---

## 📘 Table of Contents

- [What is OOP?](#what-is-oop)
- [“First-Class Everything” in Python](#first-class-everything-in-python)
- [What is a Class?](#what-is-a-class)
- [What is an Object and an Instance?](#what-is-an-object-and-an-instance)
- [Class vs Object (Instance)](#class-vs-object-instance)
- [What is an Attribute?](#what-is-an-attribute)
- [Public, Protected, and Private Attributes](#public-protected-and-private-attributes)
- [What is `self`?](#what-is-self)
- [What is a Method?](#what-is-a-method)
- [The `__init__` Method](#the-__init__-method)
- [Data Abstraction, Encapsulation, and Information Hiding](#data-abstraction-encapsulation-and-information-hiding)
- [What is a Property?](#what-is-a-property)
- [Attribute vs Property](#attribute-vs-property)
- [Getters and Setters in Python](#getters-and-setters-in-python)
- [Dynamically Creating Attributes](#dynamically-creating-attributes)
- [Binding Attributes to Objects and Classes](#binding-attributes-to-objects-and-classes)
- [Understanding `__dict__`](#understanding-__dict__)
- [How Python Finds Attributes](#how-python-finds-attributes)
- [Using `getattr()`](#using-getattr)

---

## What is OOP?

**Object-Oriented Programming (OOP)** is a programming paradigm based on the concept of "objects", which can contain data (attributes) and code (methods). It promotes reusability, scalability, and modularity in software design.

---

## “First-Class Everything” in Python

In Python, everything is an object—including functions and classes. This means you can:

* Pass functions as arguments
* Return functions from functions
* Assign them to variables
* Store them in data structures

---

## What is a Class?

A **class** is a blueprint for creating objects. It defines a set of attributes and behaviors (methods) that its instances will have.

---

## What is an Object and an Instance?

An **object** is a concrete instantiation of a class.
An **instance** is another term for an object created from a class.

```python
class Car:
    pass

my_car = Car()  # my_car is an instance of class Car
```

---

## Class vs Object (Instance)

| Feature    | Class                       | Object (Instance)           |
| ---------- | --------------------------- | --------------------------- |
| Definition | Blueprint                   | Concrete realization        |
| Memory     | Doesn't occupy memory       | Allocated memory            |
| Access     | Cannot access instance data | Can access class attributes |

---

## What is an Attribute?

An **attribute** is a variable that belongs to a class or an instance.

```python
class Car:
    color = "red"  # class attribute

    def __init__(self, model):
        self.model = model  # instance attribute
```

---

## Public, Protected, and Private Attributes

* **Public**: `name` – accessible from anywhere
* **Protected**: `_name` – convention for internal use
* **Private**: `__name` – name-mangled to prevent external access

---

## What is `self`?

`self` refers to the instance of the class and is used to access instance attributes and methods from within class definitions.

---

## What is a Method?

A **method** is a function defined inside a class. It operates on instances of the class.

---

## The `__init__` Method

`__init__` is the constructor method automatically called when a new object is created.

```python
class Car:
    def __init__(self, model):
        self.model = model
```

---

## Data Abstraction, Encapsulation, and Information Hiding

* **Abstraction**: Hiding complex logic behind simple interfaces
* **Encapsulation**: Bundling data and methods that operate on it
* **Information Hiding**: Restricting access to internal details (e.g., private attributes)

---

## What is a Property?

A **property** allows you to define methods that can be accessed like attributes.

```python
class Car:
    def __init__(self, model):
        self._model = model

    @property
    def model(self):
        return self._model
```

---

## Attribute vs Property

* **Attribute**: Direct data access
* **Property**: Method accessed like an attribute, typically used with getters/setters

---

## Getters and Setters in Python

```python
class Car:
    def __init__(self, model):
        self._model = model

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value
```

---

## Dynamically Creating Attributes

Attributes can be created at runtime:

```python
car = Car("Toyota")
car.color = "Blue"  # dynamically added
```

---

## Binding Attributes to Objects and Classes

* **To an instance**:

  ```python
  obj.attr = "value"
  ```
* **To a class**:

  ```python
  ClassName.attr = "value"
  ```

---

## Understanding `__dict__`

`__dict__` is a dictionary that contains an object’s (or class's) writable attributes.

```python
print(obj.__dict__)
```

---

## How Python Finds Attributes

Python searches for attributes in this order:

1. Instance’s `__dict__`
2. Class’s `__dict__`
3. Base classes (following MRO)

---

## Using `getattr()`

`getattr(object, 'attribute', default)` returns the value of the named attribute or a default if it doesn’t exist.

```python
getattr(obj, 'name', 'Unknown')
```

