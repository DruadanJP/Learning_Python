

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
    8. [Division - Classic, Floor, and True](#division---classic-floor-and-true)
    9. [Numeric Types](#numeric-types)
    10. [Bitwise Operations](#bitwise-operations)
    11. [Precision Handling with Decimals](#precision-handling-with-decimals)

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

## [Division - Classic, Floor, and True](Division%20-%20Classic%2C%20Floor%2C%20and%20True.py)
Python provides different types of division:
- **True Division (`/`)**: Always returns a float, even for integers.
- **Floor Division (`//`)**: Truncates the result to the nearest whole number.

### Example:
```python
print(10 / 3)   # Output: 3.333...
print(10 // 3)  # Output: 3
```

## [Numeric Types](Numeric%20Types.py)
Python supports different numeric types:
- **Integers** (`int`)
- **Floating-Point Numbers** (`float`)
- **Complex Numbers** (`complex`)

### [Bitwise Operations](Bitwise%20Operations.py)
Bitwise operators manipulate bits directly:
```python
x = 8  # 1000 in binary
print(x >> 1)  # Right shift: 4 (0100)
print(x << 1)  # Left shift: 16 (10000)
```

## Expressions and Operators
Python allows mathematical operations:
```python
# Square root calculations
import math
print(math.sqrt(144))   # Using math module
print(144 ** 0.5)      # Using exponentiation
print(pow(144, 0.5))   # Using built-in function
```

## [Precision Handling with Decimals](Precision%20Handling%20with%20Decimals.py)
Python’s `decimal` module provides precise calculations:
```python
from decimal import Decimal
result = Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
print(result)  # Decimal('0.0')
```

### Setting Global Precision
```python
import decimal
decimal.getcontext().prec = 4  # Set precision to 4 decimal places
print(decimal.Decimal(1) / decimal.Decimal(7))  # Decimal('0.1429')
```


