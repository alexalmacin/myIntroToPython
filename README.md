# Week 1 - Day 1 
## INTRODUCTION	

### THE ZEN OF PYTHON 
	
The Zen of Python is a set of guiding principles for writing computer programs in the Python programming language. 
It's not just about syntax and technicalities; it encapsulates the philosophy and style of writing Pythonic code. 

Beautiful is better than ugly. <br>
Explicit is better than implicit. <br>
Simple is better than complex. <br>
Complex is better than complicated. <br>
Flat is better than nested. <br>
Sparse is better than dense. <br>
Readability counts. <br>
Special cases aren't special enough to break the rules. <br>
Although practicality beats purity. <br>
Errors should never pass silently. <br>
Unless explicitly silenced. <br>
In the face of ambiguity, refuse the temptation to guess. <br>
There should be one-- and preferably only one --obvious way to do it. <br>
Although that way may not be obvious at first unless you're Dutch. <br>
Now is better than never. <br>
Although never is often better than *right* now. <br>
If the implementation is hard to explain, it's a bad idea. <br>
If the implementation is easy to explain, it may be a good idea. <br>
Namespaces are one honking great idea -- let's do more of those!

These principles serve as guidelines to help Python developers write code that is not only functional but also elegant, maintainable, and easy to collaborate on. 
Following the Zen of Python can lead to more enjoyable programming experiences and higher-quality software.

# Day 2
## Getting Started
### VARIABLES AND TYPES
- Variables:
Variables are used to store data values. Think of them as containers that hold information that your program can manipulate. 

name = "Alice"
age = 30
is_student = True

In this example, name, age, and is_student are all variables. name holds a string (text), age holds an integer (whole number), and is_student holds a boolean value (True or False).

- Data Types:
Every value has a data type, which defines the kind of data it represents. 

Here are some common data types in Python:
- int: Integer numbers, like 5, 10, -3.
- float: Floating-point numbers (decimal numbers), like 3.14, 2.5, -0.5.
- str: Strings, sequences of characters enclosed in single (') or double (") quotes, like "hello", 'Python'.
- bool: Boolean values, either True or False.
- list: Ordered collection of items, enclosed in square brackets [], like [1, 2, 3], ["apple", "banana", "orange"].
- tuple: Similar to lists but immutable (cannot be changed), enclosed in parentheses (), like (1, 2, 3), ("red", "green", "blue").
- dict: Collection of key-value pairs, enclosed in curly braces {}, like {"name": "Alice", "age": 30}.

## DYNAMIC TYPING
Unlike some other programming languages, Python is dynamically typed, meaning you don't need to declare the type of a variable before assigning a value to it. 
Python infers the type based on the value assigned. 

x = 5  # x is now an integer
x = "hello"  # x is now a string

## TYPE CONVERSION 
You can convert values from one type to another using built-in functions like int(), float(), str(), etc. 

num_str = "10"
num_int = int(num_str)  # Converts string to integer

Understanding variables and types is fundamental in Python programming. They allow you to store and manipulate data effectively, making your programs powerful and flexible.

	After this code is run, what is the value of b? a = [1,2,3] b = a a = [4,5,6]
	B = [1,2,3]

	What happens when the computer reads a comment line in Python?
	Nothing. The line is skipped. 
	
	What symbol do "comments" start with?
	#

## DATA STRUCTURES
Data structures in Python are a way of organizing and storing data so that it can be used efficiently. 
Python offers several built-in data structures that can be used to store collections of data.

Lists: Lists are ordered collections of items. 
	my_list = [1, 2, 3, 4, 5]

Tuples: Tuples are similar to lists, but they are immutable, meaning you cannot change their contents after they've been created. 
	my_tuple = (1, 2, 3, 4, 5)

Dictionaries: Dictionaries are collections of key-value pairs. They are unordered, meaning the order of elements is not guaranteed. 
	my_dict = {"name": "Alice", "age": 30, "is_student": False}

Sets: Sets are unordered collections of unique elements. They are useful for tasks like removing duplicates from a sequence or testing membership. 
	my_set = {1, 2, 3, 4, 5}

Strings: Strings are sequences of characters. They are immutable, meaning you cannot change their contents after they've been created. 
	my_string = "Hello, world!"

Each data structure has its own set of methods and operations that you can use to manipulate and access the data it contains.

## OPERATORS
Operators in Python are symbols or keywords that perform operations on one or more operands (values or variables). 
They allow you to perform tasks like arithmetic calculations, comparisons, logical operations, and more.

### Arithmetic Operators: These operators perform arithmetic operations like addition, subtraction, multiplication, division, etc.
	x = 10
	y = 3

	print(x + y)  # Addition
	print(x - y)  # Subtraction
	print(x * y)  # Multiplication
	print(x / y)  # Division
	print(x // y) # Integer Division
	print(x % y)  # Modulus (Remainder)
	print(x ** y) # Exponentiation

### Comparison Operators: These operators are used to compare the values of operands and return True or False.
	x = 10
	y = 20

	print(x == y)  # Equal to
	print(x != y)  # Not equal to
	print(x > y)   # Greater than
	print(x < y)   # Less than
	print(x >= y)  # Greater than or equal to
	print(x <= y)  # Less than or equal to

### Logical Operators: These operators perform logical operations on Boolean values (True or False).

```
	x = True
	y = False
	
	print(x and y)  # Logical AND
	print(x or y)   # Logical OR
	print(not x)    # Logical NOT
```

### Assignment Operators: These operators are used to assign values to variables.

```
	x = 10       # Assigns the value 10 to x
	x += 5      # Adds 5 to the current value of x (Equivalent to x = x + 5)
```

### Membership Operators: These operators are used to test for membership in a sequence (lists, tuples, strings).
```
	x = [1, 2, 3, 4, 5]

	print(3 in x)   # Checks if 3 is in the list x
	print(6 not in x) # Checks if 6 is not in the list x
```

### Identity Operators: These operators are used to compare the memory locations of two objects.

```
	x = [1, 2, 3]
	y = [1, 2, 3]
	z = x

	print(x is y)   # Checks if x and y refer to the same object
	print(x is not z) # Checks if x and z do not refer to the same object
```

## CONTROL FLOW 

Control flow in Python refers to the order in which statements are executed in a program. 
It allows you to make decisions, execute code conditionally, and repeat code based on certain conditions. 

Conditional Statements (if, elif, else): Conditional statements allow you to execute different blocks of code based on specified conditions.

```
	x = 10

	if x > 0:
    	print("x is positive")
	elif x == 0:
    	print("x is zero")
	else:
    	print("x is negative")
```

In this example, the if, elif, and else statements check the value of x and execute different print statements accordingly.

### Loops (for, while): Loops allow you to execute a block of code repeatedly.
	For Loops: Used to iterate over a sequence (like lists, tuples, or strings) or to execute a block of code a specific number of times.

 ```
		fruits = ["apple", "banana", "cherry"]

		for fruit in fruits:
    		print(fruit)
	While Loops: Continuously executes a block of code as long as a specified condition is true.
		x = 0

		while x < 5:
    		print(x)
    		x += 1
```

### Break and Continue Statements: These statements are used within loops to alter the flow of control.
	Break: Terminates the loop prematurely when a certain condition is met.

 ```
		fruits = ["apple", "banana", "cherry"]

		for fruit in fruits:
    		if fruit == "banana":
        		break
    		print(fruit)
	Continue: Skips the rest of the code inside the loop for the current iteration and continues with the next iteration.
		fruits = ["apple", "banana", "cherry"]

		for fruit in fruits:
    		if fruit == "banana":
        		continue
    		print(fruit)
```

Exception Handling (try, except, finally): Allows you to handle errors or exceptional situations gracefully without crashing the program.

```
	try:
    		x = 10 / 0
	except ZeroDivisionError:
    		print("Error: Division by zero")
	finally:
    		print("This block always executes")
```

In this example, the try block attempts to execute the code inside it, and if an exception occurs, the except block catches the exception and handles it. 
The finally block always executes, regardless of whether an exception occurred or not.
Understanding control flow is essential for writing programs that can make decisions, iterate over data, and handle errors effectively. 
It gives you the flexibility to create complex logic and solve a wide range of problems in Python.

## FUNCTIONS

Functions in Python are blocks of reusable code that perform a specific task. 
They help in organizing code into manageable pieces, making it easier to understand, debug, and maintain. 

Defining Functions: You define a function using the def keyword followed by the function name and parentheses ().

```
	def greet(name):
    	print("Hello, " + name + "!")
```

In this example, greet is the function name, and name is a parameter that the function expects.

### Calling Functions: To execute the code inside a function, you "call" the function by using its name followed by parentheses and passing any required arguments.
	greet("Alice")

This line of code calls the greet function and passes the string "Alice" as the name parameter.

### Return Statement: Functions can optionally return a value using the return statement. This allows the function to send data back to the caller.

```
	def add(x, y):
    	return x + y
```

In this example, the add function takes two parameters x and y, adds them together, and returns the result.

### Function Arguments: Functions can have both positional and keyword arguments. 
Positional arguments are passed based on their position, while keyword arguments are passed with a keyword and a value.
	def greet(name, message="Hello"):
    	print(message + ", " + name + "!")
	
In this modified greet function, message is a keyword argument with a default value of "Hello". 
If no message is provided when calling the function, it will default to "Hello".

### Docstrings: Docstrings are documentation strings that describe what the function does. 
They are enclosed in triple quotes """ and are placed immediately after the function definition.

```

	def greet(name):
    	"""
    	This function greets the user with their name.
    	"""
	print("Hello, " + name + "!")
```

Docstrings help other developers understand how to use the function and what it does.

Scope: Variables defined inside a function are local to that function and cannot be accessed from outside. 
Variables defined outside a function are global and can be accessed from within the function.

```
	x = 10
	def print_x():
	print(x)  # Accesses the global variable x
	print_x()  # Prints 10
```

## Classes and Objects 

In Python, a class is a blueprint for creating objects, and an object is an instance of a class. 

### Class: A class is a template or blueprint that defines the attributes (properties) and methods (functions) that all objects of that class will have. 
It serves as a blueprint for creating objects. You define a class using the class keyword.

```
class Dog:
	def __init__(self, name, age):
	self.name = name
	self.age = age
	def bark(self):
	print(f"{self.name} says Woof!")
```

In this example, Dog is a class that has attributes name and age, and a method bark().

### Object: An object is an instance of a class. 
It's a specific realization of the class, with its own unique attributes and methods. 
You create objects from a class using the class name followed by parentheses (). 
	my_dog = Dog("Buddy", 3)

In this example, my_dog is an object (instance) of the Dog class. It has its own name ("Buddy") and age (3).

### Attributes: Attributes are variables that hold data associated with a class or an object. 
They represent the state of the object. You access attributes using dot notation (object.attribute).
	print(my_dog.name)  # Output: Buddy
	print(my_dog.age)   # Output: 3

### Methods: Methods are functions that are defined within a class and perform operations on the object's attributes. 
They represent the behavior of the object. You call methods using dot notation (object.method()).
```
my_dog.bark()  # Output: Buddy says Woof!
```

### Constructor (__init__): The __init__ method is a special method called the constructor. 
It is automatically called when you create a new object of the class and is used to initialize the object's attributes.

```
def __init__(self, name, age):
self.name = name
self.age = age
```

### Self: self is a reference to the current instance of the class. It is used to access variables and methods within the class.

### Inheritance: Inheritance is a mechanism in which a new class inherits properties and behavior (attributes and methods) from an existing class. 
The new class is called a subclass, and the existing class is called a superclass or parent class.
```
class Labrador(Dog):
def __init__(self, name, age, color):
super().__init__(name, age)
self.color = color
```

In this example, Labrador is a subclass of Dog, and it inherits the attributes and methods of the Dog class.

Understanding classes and objects is fundamental in object-oriented programming (OOP) and allows you to create modular and reusable code in Python. 
Classes help in organizing code into logical units and promote code reuse and maintainability.

# Day 3
## Basic Data Types
### Ints and Floats

int and float are two different types of numerical data types used to represent integers and floating-point numbers, respectively.

### Integers (int): <br>
Integers are whole numbers, meaning they don't have any decimal or fractional parts. <br>
Examples of integers are: -10, 0, 42, 1000, etc. <br>
In Python, integers can be positive, negative, or zero. <br>
You can perform arithmetic operations like addition, subtraction, multiplication, and division on integers. <br>
In Python, integer variables are declared without any decimal point.

```
x = 5    # This is an integer assignment
y = -10  # This is also an integer assignment
```

### Floating-Point Numbers (float): <br>
Floating-point numbers, or floats, are numbers that have both integer and fractional parts. <br>
Examples of floats are: 3.14, 0.5, 1.0, -123.456, etc. <br>
Floats can represent a wide range of numbers, including very small and very large values, with varying levels of precision.<br>
In Python, floating-point variables are declared with a decimal point or in scientific notation. 

```
a = 3.14    # This is a floating-point assignment
b = -0.5    # This is also a floating-point assignment
```

The difference between integers and floats in Python:
```
# Integer variables
x = 5
y = -10
```
```
# Float variables
a = 3.14
b = -0.5
```
```
# Performing arithmetic operations
sum_int = x + y  # Sum of two integers
sum_float = a + b  # Sum of two floats

print("Sum of integers:", sum_int)  # Output: Sum of integers: -5
print("Sum of floats:", sum_float)  # Output: Sum of floats: 2.64
```

In summary, integers are used to represent whole numbers, while floats are used to represent numbers with decimal parts. 

## Alternative Number Types 

In Python, there are alternative number types beyond just integers (int) and floating-point numbers (float). <br>
These alternative types offer specialized functionality or optimizations for certain use cases.

### Complex Numbers (complex):
Complex numbers are numbers that have a real part and an imaginary part, represented as a + bj, where a is the real part, b is the imaginary part, and j is the imaginary unit (√-1).
Examples of complex numbers are: 3 + 4j, -2 - 5j, etc.
Python supports complex numbers directly with its built-in complex type.

```
z = 3 + 4j  # This is a complex number assignment
```

### Decimal Numbers (decimal):
Decimal numbers are floating-point numbers with fixed precision.
They are useful for applications where exact decimal representation is required, such as financial calculations.
Python's decimal module provides support for decimal numbers through the Decimal class.

```
from decimal import Decimal

d = Decimal('3.14')  # This is a decimal number assignment
```

### Fractions (fractions):
Fractions represent rational numbers as fractions of two integers: numerator and denominator.
They are useful for precise fractional arithmetic.
Python's fractions module provides support for fractions through the Fraction class.

```
from fractions import Fraction

f = Fraction(3, 4)  # This is a fraction assignment representing 3/4
```

### Boolean (bool):
Boolean values represent truth values, True or False.
They are used for logical operations and comparisons.
Boolean values are often the result of conditional expressions

```
b = True  # This is a boolean assignment
```

### None (NoneType):
None represents the absence of a value or a null value.
It is often used to indicate that a variable or expression does not have a meaningful value.
It is a singleton object of the NoneType.

```
n = None  # This is a None assignment
```

These alternative number types provide additional functionality and precision beyond what integers and floats offer, catering to specific needs such as complex arithmetic, precise decimal calculations, and rational arithmetic. 

## Booleans

Booleans are a data type used to represent truth values. 
They can have one of two possible values: True or False. Booleans are essential for making decisions and controlling the flow of your code through conditional statements and loops.

Here's a breakdown of Booleans in Python:

### True and False Values:
True represents a true or affirmative condition.
False represents a false or negative condition.

### Boolean Operators:
Python provides several operators for working with Booleans, including:
and: Returns True if both operands are True, otherwise returns False.
or: Returns True if at least one of the operands is True, otherwise returns False.
not: Returns the opposite Boolean value of the operand. If the operand is True, not returns False, and vice versa.

### Boolean Expressions:
Boolean expressions are expressions that evaluate to either True or False.
Examples of Boolean expressions include:
Comparisons: == (equal), != (not equal), < (less than), > (greater than), <= (less than or equal to), >= (greater than or equal to).

### Logical operations: and, or, not.
Membership test: in (checks if a value is present in a sequence).

### Conditional Statements:
Conditional statements, such as if, elif (else if), and else, are used to execute different blocks of code based on Boolean conditions.
These statements help in decision-making and branching within your code.

```
# Boolean variables
is_sunny = True
is_raining = False

# Boolean expressions
temperature = 25
is_warm = temperature > 20
is_hot = temperature > 30

# Conditional statement
if is_sunny and not is_raining:
    print("It's a sunny day!")
elif is_raining:
    print("It's raining.")
else:
    print("It's neither sunny nor raining.")

if is_warm:
    print("It's warm outside.")
if is_hot:
    print("It's hot outside.")
```

In this example, we use Boolean variables (is_sunny, is_raining), Boolean expressions (is_warm, is_hot), and conditional statements (if, elif, else) to make decisions based on weather conditions and temperature. 

## Strings

In programming, a string is a sequence of characters, such as letters, numbers, symbols, or spaces, that are enclosed within either single quotes (' ') or double quotes (" "). 

```
name = "Alice"
message = 'Hello, World!'
```

In Python, strings can be manipulated in various ways. 

1) Concatenation: You can concatenate (join) two or more strings together using the + operator:

```
greeting = "Hello"
name = "Alice"
message = greeting + ", " + name + "!"
print(message)  # Output: Hello, Alice!
```

2) Length: You can find the length of a string (the number of characters it contains) using the len() function:

```
name = "Alice"
print(len(name))  # Output: 5
```

3) Indexing and Slicing: You can access individual characters in a string using their index. 
Python uses zero-based indexing, meaning the first character has an index of 0, the second character has an index of 1, and so on. 
You can also extract a substring (a portion of a string) using slicing:

```
message = "Hello, World!"
print(message[0])    # Output: H
print(message[7])    # Output: W
print(message[0:5])  # Output: Hello
print(message[7:])   # Output: World!
```

4) String Methods: Python provides many built-in methods to manipulate strings, such as converting the case, splitting, replacing, stripping whitespace, etc. For example:

```
message = "   Hello, World!   "
print(message.upper())           # Output:    HELLO, WORLD!   
print(message.strip())           # Output: Hello, World!
print(message.replace("Hello", "Hi"))  # Output:    Hi, World!   
```

5) Formatting: You can format strings using the format() method or f-strings (formatted string literals in Python 3.6+):

```
name = "Alice"
age = 30
message = "My name is {} and I am {} years old.".format(name, age)
print(message)  # Output: My name is Alice and I am 30 years old.

# Using f-strings
message = f"My name is {name} and I am {age} years old."
print(message)  # Output: My name is Alice and I am 30 years old.
```


## Bytes

In Python, bytes is a built-in data type used to represent sequences of bytes. A byte is a unit of digital information that typically consists of 8 bits and can represent values from 0 to 255.

1) Immutable Sequence of Bytes: Bytes objects are immutable sequences, meaning once created, their contents cannot be changed. 
You can create a bytes object by enclosing a sequence of bytes within a pair of single quotes (b'') or by using the bytes() constructor function.

```
# Creating bytes objects
b1 = b'hello'
b2 = bytes([104, 101, 108, 108, 111])  # Using bytes constructor with a list of integers representing ASCII values
```

2) Binary Data Representation: Bytes are commonly used to represent binary data, such as raw image data, network packets, or encoded text. 
Each byte in a bytes object represents a single 8-bit character.

3) Byte Literals: Byte literals are prefixed with a lowercase 'b' or 'B' character. They can contain ASCII characters, escape sequences, or hexadecimal notation.

```
# Byte literals
b3 = b'\x48\x65\x6c\x6c\x6f'  # Hexadecimal notation representing ASCII values
b4 = b'\n\t\x41\x42'          # Escape sequences (\n for newline, \t for tab, etc.)
```

4) Byte Operations: Bytes objects support various operations, such as indexing, slicing, concatenation, and iteration, similar to other sequence types in Python (like strings or lists).

```
# Byte operations
print(b1[0])        # Accessing individual byte (Output: 104)
print(b1[1:])       # Slicing (Output: b'ello')
print(b1 + b2)      # Concatenation (Output: b'hellohello')
for byte in b3:
    print(byte)     # Iterating over bytes
```

5) Encoding and Decoding: Bytes objects can be encoded to produce a string or decoded from a string using specific encoding schemes, such as UTF-8, ASCII, etc., using the encode() and decode() methods.

```
# Encoding and decoding bytes
text = 'hello'
encoded_bytes = text.encode('utf-8')   # Encode string to bytes using UTF-8 encoding
decoded_text = encoded_bytes.decode('utf-8')  # Decode bytes to string
```

These are some basic concepts about bytes in Python. They are essential for handling binary data and performing various operations on it efficiently.

# Day 4
## Basic Data Structure
### Lists

A list is a versatile and fundamental data structure used to store collections of items. Here's an explanation of lists in Python:

1) Sequence of Elements: A list is an ordered collection of elements, where each element can be of any data type (e.g., integers, strings, other lists, etc.). 
Lists are mutable, meaning you can change their elements after they have been created.

```
# Example of a list
my_list = [1, 2, 3, 4, 5]
```

2) Creating Lists: Lists are created by enclosing a sequence of comma-separated elements within square brackets [ ]. You can also create an empty list by simply using empty square brackets.

```
# Creating a list
my_list = [1, 2, 3, 4, 5]
empty_list = []
```

3) Accessing Elements: You can access individual elements in a list using indexing. 
Python uses zero-based indexing, where the first element has an index of 0, the second element has an index of 1, and so on. 
Negative indices can be used to access elements from the end of the list.

```
# Accessing elements in a list
print(my_list[0])   # Output: 1
print(my_list[-1])  # Output: 5 (last element)
```

4) Slicing: You can extract a sublist (a portion of a list) using slicing. Slicing allows you to specify a range of indices to extract a subset of the list.

```
# Slicing a list
print(my_list[1:4])  # Output: [2, 3, 4] (elements from index 1 to index 3)
```

5) List Methods: Python provides various built-in methods to manipulate lists, such as append(), extend(), insert(), remove(), pop(), index(), count(), sort(), reverse(), etc.

```
# List methods
my_list.append(6)      # Append an element to the end of the list
my_list.insert(2, 10)  # Insert an element at a specific index
my_list.remove(3)      # Remove the first occurrence of a specified value
my_list.sort()         # Sort the list in ascending order
```

6) Iterating Over a List: You can iterate over the elements of a list using a loop, such as a for loop or a while loop.

```
# Iterating over a list
for item in my_list:
    print(item)
```

Lists are one of the most commonly used data structures in Python due to their flexibility and usefulness in storing and manipulating collections of data. 

## Tuples and Sets

Tuples:
1) Ordered Collection: Like lists, tuples are ordered collections of elements. 
However, unlike lists, tuples are immutable, meaning once they are created, their elements cannot be changed or modified.

```
# Example of a tuple
my_tuple = (1, 2, 3, 4, 5)
```

2) Creating Tuples: Tuples are created by enclosing a sequence of comma-separated elements within parentheses (). 
A tuple with a single element must have a trailing comma to distinguish it from a parenthesized expression.

```
# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
single_element_tuple = (42,)  # Single element tuple
```

3) Accessing Elements: You can access individual elements in a tuple using indexing, similar to lists.

```
# Accessing elements in a tuple
print(my_tuple[0])   # Output: 1
print(my_tuple[-1])  # Output: 5 (last element)
```

4) Immutable Nature: Since tuples are immutable, you cannot modify, add, or remove elements from a tuple after it has been created. 
However, you can create a new tuple by concatenating or slicing existing tuples.

```
# Modifying tuples (creating new tuples)
new_tuple = my_tuple + (6, 7, 8)  # Concatenating tuples
sliced_tuple = my_tuple[1:4]      # Slicing a tuple
```

Sets:
1) Unordered Collection of Unique Elements: A set is an unordered collection of unique elements. It does not allow duplicate elements, and the elements are not stored in any particular order.

```
# Example of a set
my_set = {1, 2, 3, 4, 5}
```

2) Creating Sets: Sets are created by enclosing a sequence of comma-separated elements within curly braces {}.

```
# Creating a set
my_set = {1, 2, 3, 4, 5}
```

3) Adding and Removing Elements: You can add elements to a set using the add() method, and you can remove elements using the remove() or discard() methods.

```
# Adding and removing elements from a set
my_set.add(6)       # Add an element to the set
my_set.remove(3)    # Remove an element from the set
```

4) Operations on Sets: Sets support various set operations such as union, intersection, difference, and symmetric difference.

```
# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2           # Union of sets
intersection_set = set1 & set2   # Intersection of sets
difference_set = set1 - set2     # Difference of sets
```

Sets are useful for tasks that involve testing membership, eliminating duplicates, and performing mathematical set operations efficiently. 
They are mutable, unlike tuples, but similar to dictionaries, sets are unordered collections.

### Dictionaries

Dictionaries in Python are a powerful and flexible data structure used to store collections of data in key-value pairs. 

1) Key-Value Pairs: A dictionary is a collection of items where each item is stored as a pair of a key and its corresponding value. 
Keys are unique within a dictionary, while values can be duplicates.

```
# Example of a dictionary
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
```

2) Creating Dictionaries: Dictionaries are created by enclosing a comma-separated list of key-value pairs within curly braces {}. Each key-value pair is separated by a colon ':'

```
# Creating a dictionary
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
```

3) Accessing Values: You can access the value associated with a key in a dictionary by using the key within square brackets []. If the key doesn't exist, it will raise a KeyError.

```
# Accessing values in a dictionary
print(my_dict['name'])   # Output: Alice
print(my_dict['age'])    # Output: 30
```

4) Adding, Modifying, and Removing Items: You can add new key-value pairs, modify existing values, or remove items from a dictionary.

```
# Adding, modifying, and removing items from a dictionary
my_dict['gender'] = 'Female'   # Adding a new key-value pair
my_dict['age'] = 31            # Modifying the value of an existing key
del my_dict['city']            # Removing an item from the dictionary
```

5) Dictionary Methods: Python provides various built-in methods to manipulate dictionaries, such as keys(), values(), items(), get(), update(), pop(), popitem(), clear(), etc.

```
# Dictionary methods
keys = my_dict.keys()           # Get a list of keys
values = my_dict.values()       # Get a list of values
items = my_dict.items()         # Get a list of key-value pairs
```

6) Iterating Over a Dictionary: You can iterate over the keys, values, or key-value pairs of a dictionary using a loop.

```
# Iterating over a dictionary
for key in my_dict:
    print(key, my_dict[key])
```

Dictionaries are incredibly useful for storing and organizing data in Python, especially when you need to quickly access values based on their associated keys. 
They are commonly used in various programming tasks, from data processing to web development.

### List Comprehensions

List comprehensions are a concise and powerful way to create lists in Python. 
They allow you to generate a new list by applying an expression to each element of an existing iterable (like a list, tuple, or range) while also optionally filtering the elements based on a condition. 

Basic List Comprehension Syntax:

```
new_list = [expression for item in iterable]
```

- expression: The expression to be evaluated and included in the new list for each item in the iterable.
- item: The variable representing each element in the iterable.
- iterable: The existing iterable (e.g., list, tuple, range) from which elements are taken.

Example:
Let's say we have a list of numbers and we want to create a new list containing the squares of each number:

```
numbers = [1, 2, 3, 4, 5]

squares = [x ** 2 for x in numbers]
```

In this example:

The expression x ** 2 calculates the square of each number x.
The variable x represents each element in the numbers list.
The for x in numbers part iterates over each element in the numbers list.

The resulting squares list will be [1, 4, 9, 16, 25].

List Comprehension with Condition:
You can also include an optional condition in a list comprehension to filter elements based on a certain criteria.

```
new_list = [expression for item in iterable if condition]
```

Example:
Let's say we want to create a list containing only the even numbers from the original list:

```
numbers = [1, 2, 3, 4, 5]

even_numbers = [x for x in numbers if x % 2 == 0]
```

In this example:

The condition x % 2 == 0 checks if x is even.
Only the elements for which the condition is True will be included in the new list.

The resulting even_numbers list will be [2, 4].

Benefits of List Comprehensions:
- Concise Code: List comprehensions allow you to achieve the same result with less code compared to traditional loops.
- Readability: They make your code more readable and expressive, especially for simple transformations and filtering operations.
- Efficiency: List comprehensions are often more efficient than equivalent loops in terms of both speed and memory usage.

### Comprehensions

Comprehensions:
Comprehensions in Python are concise and powerful ways to create collections (like lists, dictionaries, or sets) by applying an expression to each element of an existing iterable (such as a list, tuple, or range), while optionally filtering elements based on a condition.

1) List Comprehensions: List comprehensions allow you to create lists based on existing iterables, applying an expression to each element.

```
# Example of list comprehension
numbers = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in numbers]
```

2) Dictionary Comprehensions: Dictionary comprehensions allow you to create dictionaries in a similar way, using key-value pairs.

```
# Example of dictionary comprehension
squares_dict = {x: x ** 2 for x in numbers}
```

3) Set Comprehensions: Set comprehensions allow you to create sets, ensuring uniqueness of elements.

```
# Example of set comprehension
squares_set = {x ** 2 for x in numbers}
```

4) Generator Comprehensions: Generator comprehensions are similar to list comprehensions but produce generator objects, which are memory-efficient lazy iterators.

```
# Example of generator comprehension
squares_generator = (x ** 2 for x in numbers)
```

Comprehensions are concise, readable, and efficient ways to create collections in Python, and they are widely used in Python code for various tasks. 
They are particularly useful for transforming data and applying operations to iterables in a compact and expressive manner.

# Day 5 
## Basic Control Flow
### If and Else

In Python, if and else are control flow statements used for conditional execution of code. They allow you to execute certain blocks of code only if a specified condition is true. 

### if Statement:
The if statement is used to check a condition and execute a block of code if the condition is true.

```
if condition:
    # Code block to execute if the condition is true
    statement1
    statement2
    ...
```

condition: An expression that evaluates to either True or False.
Code block: The indented block of code that executes if the condition is True.

```
x = 10

if x > 5:
    print("x is greater than 5")
```

In this example, "x is greater than 5" will be printed because the condition x > 5 is true.

### else Statement:
The else statement follows an if statement and is used to execute a block of code if the preceding if condition is false.

```
if condition:
    # Code block to execute if the condition is true
    statement1
    statement2
    ...
else:
    # Code block to execute if the condition is false
    statement3
    statement4
    ...
```

Example:

```
x = 3

if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
```

In this example, "x is not greater than 5" will be printed because the condition x > 5 is false.

### Nested if Statements:
You can also nest if statements within other if statements or else blocks to create more complex conditional logic.

```
if condition1:
    if condition2:
        # Code block to execute if both condition1 and condition2 are true
        statement1
        statement2
    else:
        # Code block to execute if condition1 is true but condition2 is false
        statement3
        statement4
else:
    # Code block to execute if condition1 is false
    statement5
    statement6
```

Example:

```
x = 6
y = 2

if x > 5:
    if y > 1:
        print("x is greater than 5 and y is greater than 1")
    else:
        print("x is greater than 5 but y is not greater than 1")
else:
    print("x is not greater than 5")
```

In this example, "x is greater than 5 and y is greater than 1" will be printed because both conditions x > 5 and y > 1 are true.

### While

In Python, while is a control flow statement used for looping, which means it allows you to execute a block of code repeatedly based on a condition. 
Here's a breakdown:


```
while condition:
    # code block
```

- 'while': This is the keyword that tells Python we're starting a while loop.
- 'condition': This is a boolean expression. As long as this condition is True, the code block inside the loop will continue to execute. Once the condition becomes False, the loop will stop.
- ':': It's important to include the colon at the end of the while statement. It indicates the beginning of the code block that belongs to the while loop.
- 'code block': This is the set of Python statements that will be executed repeatedly as long as the condition remains True.

Here's a simple example to illustrate:


```
# Initializing a variable
count = 0

# While loop to print numbers from 0 to 4
while count < 5:
    print(count)
    count += 1  # Incrementing count by 1 in each iteration
```

In this example:

- We start with count equal to 0.
- The while loop's condition checks if count is less than 5. Since count is 0, the condition is True, and the loop executes.
- Inside the loop, it prints the value of count (which is 0) and then increments count by 1.
- This process repeats until count is no longer less than 5. When count becomes 5, the condition becomes False, and the loop stops executing.

So, the output of this code will be:

```
0
1
2
3
4
```

That's the basic idea behind using while loops in Python! They're handy for situations where you want to repeat a block of code until a certain condition is met.

### For

In Python, for is another type of loop that allows you to iterate over a sequence (such as a list, tuple, string, or range) and execute a block of code for each item in that sequence. 

```
for item in sequence:
    # code block
```

- for: This is the keyword that tells Python we're starting a for loop.
- item: This is a variable name that represents each item in the sequence as the loop iterates over it. You can choose any name for this variable.
- in: This keyword is used to link the variable item with the sequence.
- sequence: This is the collection of items over which the loop will iterate. It could be a list, tuple, string, range, or any other iterable object.
- :: Like with while loops, the colon indicates the beginning of the code block that belongs to the for loop.
- code block: This is the set of Python statements that will be executed for each item in the sequence.

```
# Iterating over a list of numbers
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)
```

In this example:

- We have a list of numbers [1, 2, 3, 4, 5].
- The for loop iterates over each item in the list.
- For each iteration, the variable num takes on the value of the current item.
- Inside the loop, it prints the value of num.

So, the output of this code will be:

```
1
2
3
4
5
```

The for loop is very useful for iterating over collections of data, like lists or strings, and performing operations on each item within the collection. 









































