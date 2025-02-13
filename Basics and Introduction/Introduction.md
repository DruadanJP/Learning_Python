

## Table of Contents

Python Overview
<details>
<summary>Introduction to Python</summary>

1. [Introduction to Python](#introduction-to-python)
    1. [Python Interpreter & Execution](#python-interpreter--execution)
    2. [Python Execution Model](#python-execution-model)
    3. [Modules and Scripts](#modules-and-scripts)
    4. [Variables and Basic Expressions](#variables-and-basic-expressions)
    5. [Data Structures: Sequences (Strings, Lists, Tuples)](#data-structures-sequences)
    6. [List Comprehension](#list-comprehension)
    7. [Object-Oriented Programming (OOP)](#object-oriented-programming-oop)

</details>



## Python Overview

## Introduction to Python
Python is commonly defined as an **object-oriented scripting language**, blending support for object-oriented programming (OOP) with scripting capabilities. It is widely used for:
- **System administration**: Portable and maintainable shell tools.
- **General-purpose programming**: Web development, automation, data science, etc.

## [Python Interpreter & Execution](Python%20Interpreter%20%26%20Execution.py)
A **Python interpreter** is a program that executes other programs. It acts as a software layer between the user's code and the computer hardware.

### How Python Runs Programs
Python programs undergo the following execution steps:
1. **Source Code**: The code you write in `.py` files.
2. **Compilation to Byte Code**:
    - Python compiles source code into **byte code** to speed up execution.
    - Byte code files (`.pyc`) can be used to distribute programs without sharing source code.
3. **Execution in the Python Virtual Machine (PVM)**:
    - The **PVM** is the runtime engine that executes Python byte code.
    - Python programs are **interpreted** at runtime.

### Code Execution Example
```python
# Example Python Script
def greet():
    print("Hello, World!")

greet()
```
When executed, Python first compiles this script to byte code before running it on the **PVM**.

## Python Execution Model
Python’s execution model follows these steps:
1. Source code → Byte code
2. Byte code → Python Virtual Machine (PVM)
3. PVM interprets and runs the program

### Byte Code and PVM
- **Byte code** is not machine code; it is a Python-specific format.
- The **PVM** translates byte code into machine instructions at runtime.
- **JIT Compilers** (e.g., PyPy) improve performance by compiling byte code just-in-time.
- **Frozen Binaries** can turn Python programs into standalone executables.

## Modules and Scripts
Python programs are typically written in **modules** (i.e., `.py` files).

### Terminology:
- **Module**: A reusable Python file (e.g., `math.py`).
- **Script**: A standalone program that runs directly.
- **Stream Redirection**: Saving output to a file:
  ```bash
  python script.py > output.txt
  ```

## [Variables and Basic Expressions](Variables%20and%20Basic%20Expressions.py)
Variables are simply names that are used to keep track of information in your program. In Python:
- Variables are created when they are first assigned values.
- Variables are replaced with their values when used in expressions.
- Variables must be assigned before they can be used in expressions.
- Variables refer to objects and are never declared ahead of time.

### Example:
```python
# Assigning variables
a = 3  # Name created
b = 4  # Another variable
print(a + b)  # Output: 7
```

## [Data Structures Sequences](Data%20Structures%20-%20Sequences.py)
Python provides **sequences**, which are ordered collections of objects.

### Types of Sequences:
1. **Strings**: Immutable sequences of characters.
2. **Lists**: Mutable sequences that can be modified in place.
3. **Tuples**: Immutable sequences.

#### Example:
```python
s = "hello"
print(s[0])  # Accessing first character
print(s[-1]) # Accessing last character
```

### [List Comprehension](List%20Comprehension.py)
A concise way to create lists:
```python
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]
```

## Object-Oriented Programming (OOP)
Everything in Python is an **object**.

