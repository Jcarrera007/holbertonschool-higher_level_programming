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
- Pass functions as arguments
- Return functions from functions
- Assign them to variables
- Store them in data structures

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
