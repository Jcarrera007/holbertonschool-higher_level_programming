# Python Input/Output and File Handling

## General

This repository contains Python scripts and exercises focused on file input/output (I/O), file handling, and working with JSON data. The goal is to demonstrate and practice essential concepts for reading, writing, and manipulating files, as well as serializing and deserializing data in Python.

## Topics Covered

- **Why Python programming is awesome:**  
  Python is a powerful, easy-to-learn language with a rich ecosystem for handling files, data, and automation tasks.

- **How to open a file:**  
  Use the built-in `open()` function to open files for reading, writing, or appending.

- **How to write text in a file:**  
  Use file methods like `.write()` or `.writelines()` to add content to a file.

- **How to read the full content of a file:**  
  Use `.read()` to get the entire file content as a string.

- **How to read a file line by line:**  
  Use `.readline()`, `.readlines()`, or iterate directly over the file object in a loop.

- **How to move the cursor in a file:**  
  Use `.seek()` to move the file pointer to a specific position.

- **How to make sure a file is closed after using it:**  
  Always close files with `.close()`, or better, use the `with` statement to handle files automatically.

- **What is and how to use the with statement:**  
  The `with` statement ensures that resources like files are properly managed and closed, even if errors occur.

- **What is JSON:**  
  JSON (JavaScript Object Notation) is a lightweight data-interchange format that is easy for humans to read and write, and easy for machines to parse and generate.

- **What is serialization:**  
  Serialization is the process of converting a Python data structure into a format (like JSON) that can be stored or transmitted.

- **What is deserialization:**  
  Deserialization is the process of converting data (like a JSON string) back into a Python data structure.

- **How to convert a Python data structure to a JSON string:**  
  Use `json.dumps()` to serialize Python objects to JSON strings.

- **How to convert a JSON string to a Python data structure:**  
  Use `json.loads()` to deserialize JSON strings to Python objects.

- **How to access command line parameters in a Python script:**  
  Use the `sys.argv` list from the `sys` module to access command line arguments.

## Usage

Each script in this repository demonstrates one or more of the above concepts. You can run the scripts directly with Python 3:

```bash
python3 script_name.py
```
