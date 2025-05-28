# Python Inheritance & Class Hierarchy

This repository contains notes and examples to help understand Python's object-oriented inheritance system, including superclass-subclass relationships, attribute resolution, and the use of built-in functions for introspection.

## 📚 General Topics Covered

### ✅ What is a Superclass, Base Class, or Parent Class?

A **superclass** (also called a **base class** or **parent class**) is the class from which another class inherits. It contains common behavior (methods/attributes) that can be reused by its subclasses.

### ✅ What is a Subclass?

A **subclass** is a class that inherits from another class (the superclass). It can override or extend the functionality of the base class.

```python
class Animal:
    def speak(self):
        return "Sound"

class Dog(Animal):
    def speak(self):
        return "Bark"
```

### ✅ How to List All Attributes and Methods of a Class or Instance

You can use the `dir()` built-in function:

```python
print(dir(MyClass))
print(dir(my_instance))
```

### ✅ When Can an Instance Have New Attributes?

Instances can have new attributes added dynamically after they are created, usually like this:

```python
my_instance.new_attr = "Hello"
```

Unless the class uses `__slots__`, which restricts dynamic attribute creation.

### ✅ How to Inherit a Class from Another

Use parentheses to inherit a class:

```python
class Parent:
    pass

class Child(Parent):
    pass
```

### ✅ How to Define a Class with Multiple Base Classes

Use a comma-separated list in the parentheses:

```python
class Mother:
    pass

class Father:
    pass

class Child(Mother, Father):
    pass
```

### ✅ What is the Default Class Every Class Inherits From?

In Python 3, all classes implicitly inherit from the `object` class.

```python
class MyClass:
    pass

print(issubclass(MyClass, object))  # True
```

### ✅ How to Override a Method or Attribute Inherited from the Base Class

Simply redefine the method or attribute in the subclass:

```python
class Parent:
    def greet(self):
        return "Hello"

class Child(Parent):
    def greet(self):
        return "Hi"
```

### ✅ Which Attributes or Methods Are Available by Inheritance?

All public and protected attributes and methods are available unless explicitly overridden in the subclass. Private attributes (with double underscore `__`) are not inherited.

### ✅ What is the Purpose of Inheritance?

* Code reusability
* Logical organization
* Method overriding for polymorphism
* Facilitates maintainability and scalability

### ✅ What Are, When and How to Use `isinstance`, `issubclass`, `type`, and `super`

* `isinstance(obj, Class)` → Checks if an object is an instance of a class or subclass.
* `issubclass(ClassA, ClassB)` → Checks if ClassA is derived from ClassB.
* `type(obj)` → Returns the exact class of the object (not considering inheritance).
* `super()` → Allows you to call methods from a superclass inside a subclass.

```python
class Parent:
    def greet(self):
        return "Hello"

class Child(Parent):
    def greet(self):
        return super().greet() + " from Child"
```

---

📂 This repo serves as a handy reference for Python OOP inheritance and introspection features. Ideal for beginners and intermediate learners working on class-based design in Python.
