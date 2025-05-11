# Python Programming Basics

Welcome to the **Python Programming Basics** repository. This guide covers fundamental concepts and best practices for writing Python code, including how to import functions, create modules, handle command line arguments, and more.

## Table of Contents

1. [Why Python Programming is Awesome](#why-python-programming-is-awesome)
2. [Importing Functions from Another File](#importing-functions-from-another-file)
3. [Using Imported Functions](#using-imported-functions)
4. [Creating a Python Module](#creating-a-python-module)
5. [Using the Built-in `dir()` Function](#using-the-built-in-dir-function)
6. [Preventing Code Execution on Import](#preventing-code-execution-on-import)
7. [Using Command Line Arguments](#using-command-line-arguments)
8. [Conclusion](#conclusion)

---

## Why Python Programming is Awesome

Python is one of the most popular programming languages in the world, known for its simplicity and readability. It is widely used for web development, data analysis, artificial intelligence, machine learning, and scientific computing.

Key Benefits of Python:

* Simple and intuitive syntax
* Extensive library support
* Cross-platform compatibility
* Strong community support
* Great for beginners and experts alike

## Importing Functions from Another File

In Python, you can organize your code into multiple files for better structure and readability. To use functions from another file, you can use the `import` statement.

**Example:**

```python
# main.py
import my_module

my_module.greet()
```

```python
# my_module.py
def greet():
    print("Hello from my_module!")
```

## Using Imported Functions

Once a function is imported, you can use it just like any other function in your script. If you only need a specific function, you can import it directly:

**Example:**

```python
from my_module import greet

greet()
```

## Creating a Python Module

A module is simply a Python file that contains functions, classes, or variables that you want to reuse. Creating a module is as easy as creating a new `.py` file.

**Example:**

```python
# my_module.py
def greet():
    print("Hello from my_module!")
```

## Using the Built-in `dir()` Function

The `dir()` function is a built-in Python function that returns a list of all the attributes and methods of a module or object.

**Example:**

```python
import my_module
print(dir(my_module))
```

## Preventing Code Execution on Import

To prevent code from being executed when a module is imported, use the `if __name__ == "__main__":` pattern.

**Example:**

```python
# my_module.py
def greet():
    print("Hello from my_module!")

if __name__ == "__main__":
    greet()
```

## Using Command Line Arguments

Python provides the `sys.argv` list to capture command line arguments passed to a script.

**Example:**

```python
# script.py
import sys
print(f"Arguments: {sys.argv}")
```

Run this script as follows:

```bash
$ python3 script.py arg1 arg2
```

## Conclusion

Python's flexibility and simplicity make it an ideal language for a wide range of applications. Understanding how to effectively organize and reuse your code is a critical skill for any Python developer.

Happy coding! 🚀

