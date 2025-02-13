# Comprehensive Overview of Python Numeric Types

## Introduction

Python provides a rich set of numeric data types, enabling a broad range of mathematical computations. Data in Python is represented as objects, and numeric types form the foundation of mathematical and scientific applications. Python supports various built-in numeric types, including integers, floating-point numbers, complex numbers, and specialized types such as fractions and decimals for precise calculations.

This document provides a detailed overview of Python's numeric types, complete with explanations, examples, and practical use cases.

## Table of Contents
<details>
<summary>Numeric Types Table of Contents</summary>

1. [Integers and Floating-Point Numbers](#1-integers-and-floating-point-numbers)
2. [Booleans](#2-booleans)
3. [Division - Classic, Floor, and True](#3-division---classic-floor-and-true)
4. [Complex Numbers](#4-complex-numbers)
5. [Rational Fraction Numbers](#5-rational-fraction-numbers)
6. [Sets](#6-sets)
7. [Unlimited Integer Precision](#7-unlimited-integer-precision)
8. [Numeric Built-ins and Modules](#8-numeric-built-ins-and-modules)
9. [Bitwise Operations](#9-bitwise-operations)
10. [Expressions and Operators](#10-expressions-and-operators)
11. [Precision Handling with Decimals](#11-precision-handling-with-decimals)
12. [Setting Global Precision](#setting-global-precision)
13. [Numeric Extensions](#numeric-extensions)
14. [Test Your Knowledge: Quiz](#test-your-knowledge-quiz)



</details>

---

## 1. [Integers and Floating-Point Numbers](Numeric%20Types.py)

### **Integers (`int`)**

- Whole numbers (positive, negative, or zero)
- No size limit (only constrained by available memory)
- Supports various arithmetic operations: `+`, `-`, `*`, `//`, `%`, `**`
- Can be represented in different bases: Binary (`0b`), Octal (`0o`), Hexadecimal (`0x`)

#### **Examples:**

```python
x = 42           # Integer
hex_x = 0x2A     # Hexadecimal representation (42)
bin_x = 0b101010 # Binary representation (42)
print(type(x), hex_x, bin_x)
```

---

### **Floating-Point Numbers (`float`)**

- Numbers with a fractional component
- Uses double-precision (64-bit) floating point representation
- Can be expressed in scientific notation (`1.23e3` for `1230.0`)
- May suffer from floating-point precision errors

#### **Examples:**

```python
y = 3.14      # Float
z = 1.23e3    # Scientific notation
print(type(y), type(z), z)
```

---

## 2. Booleans

- Represents logical values `True` and `False`
- Subtype of integers (`True` behaves as `1`, `False` behaves as `0`)
- Supports logical operations: `and`, `or`, `not`

#### **Examples:**

```python
x = True
y = False
print(x + y)  # Output: 1
print(x and y)  # Output: False
print(x or y)  # Output: True
```

---

## 3. [Division - Classic, Floor, and True](Division%20-%20Classic%2C%20Floor%2C%20and%20True.py)

Python provides different types of division:

- **True Division (`/`)**: Always returns a floating-point result, even for integers.
- **Floor Division (`//`)**: Rounds down to the nearest whole number.

#### **Examples:**

```python
print(10 / 3)   # Output: 3.333...
print(10 // 3)  # Output: 3
```

---

## 4. Complex Numbers

- Represented as `a + bj`, where `j` is the imaginary unit.
- Supports arithmetic operations like addition, subtraction, multiplication, and division.

#### **Examples:**

```python
c1 = 3 + 4j
c2 = 1 - 2j
result = c1 * c2
print(result)  # Output: (11-2j)
```

---

## 5. Rational Fraction Numbers

- Represents numbers as fractions (`numerator/denominator`)
- Useful for exact arithmetic, avoiding floating-point precision errors.

#### **Examples:**

```python
from fractions import Fraction
frac1 = Fraction(3, 4)
frac2 = Fraction(2, 3)
print(frac1 + frac2)  # Output: 17/12
print(frac1 * frac2)  # Output: 1/2
```

---

## 6. Sets

- Unordered collection of unique items.
- Supports set operations such as union, intersection, and difference.

#### **Examples:**

```python
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1 | s2)  # Union: {1, 2, 3, 4, 5}
print(s1 & s2)  # Intersection: {3}
```

---

## 7. Unlimited Integer Precision

- Python integers can grow arbitrarily large, limited only by available memory.

#### **Examples:**

```python
x = 10**100  # A very large number
print(x)
```

---

## 8. Numeric Built-ins and Modules

- **Built-in functions**: `abs()`, `round()`, `pow()`, `int()`, `float()`
- **Modules**:
    - `math`: Provides advanced mathematical functions.
    - `random`: Generates random numbers.

#### **Examples:**

```python
import math
print(math.sqrt(16))  # Output: 4.0
```

---

## 9. [Bitwise Operations](Bitwise%20Operations.py)

Bitwise operators manipulate binary representations of integers:

- **AND (`&`)**: `1` if both bits are `1`
- **OR (`|`)**: `1` if at least one bit is `1`
- **XOR (`^`)**: `1` if bits are different
- **Left Shift (`<<`)**: Shifts bits left (multiplies by 2)
- **Right Shift (`>>`)**: Shifts bits right (divides by 2)

#### **Examples:**

```python
x = 8  # 1000 in binary
print(x >> 1)  # Right shift: 4 (0100)
print(x << 1)  # Left shift: 16 (10000)
```

---

## 10. Expressions and Operators

Python allows mathematical operations:

```python
import math
print(math.sqrt(144))   # Using math module
print(144 ** 0.5)      # Using exponentiation
print(pow(144, 0.5))   # Using built-in function
```

---

## 11. [Precision Handling with Decimals](Precision%20Handling%20with%20Decimals.py)

Python’s `decimal` module provides precise calculations:

```python
from decimal import Decimal
result = Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
print(result)  # Output: 0.0 (Precise result)
```

## **Setting Global Precision**

```python
import decimal
decimal.getcontext().prec = 4  # Set precision to 4 decimal places
print(decimal.Decimal(1) / decimal.Decimal(7))  # Decimal('0.1429')
```

## Numeric Extensions

Finally, while Python’s core numeric types provide ample power for most applications, a vast library of third-party open-source extensions is available to address specific needs. 

For instance, if you require serious number crunching, an optional extension for Python called NumPy (Numeric Python) offers advanced numeric programming capabilities, including a matrix data type, vector processing, and sophisticated computation libraries. 

The combination of Python and NumPy is often likened to a free and more flexible version of Matlab—you gain NumPy’s performance, complemented by the Python language and its extensive libraries.

## Test Your Knowledge: Quiz

1. What is the value of the expression 2 * (3 + 4) in Python?
2. What is the value of the expression 2 * 3 + 4 in Python?
3. What is the value of the expression 2 + 3 * 4 in Python?
4. What tools can you use to find a number’s square root, as well as its square?
5. What is the type of the result of the expression 1 + 2.0 + 3?
6. How can you truncate and round a floating-point number?
7. How can you convert an integer to a floating-point number?
8. How would you display an integer in octal, hexadecimal, or binary notation?
9. How might you convert an octal, hexadecimal, or binary to a plain integer?

