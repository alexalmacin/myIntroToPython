# Day 1 
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

# DYNAMIC TYPING
Unlike some other programming languages, Python is dynamically typed, meaning you don't need to declare the type of a variable before assigning a value to it. 
Python infers the type based on the value assigned. 

x = 5  # x is now an integer
x = "hello"  # x is now a string

# TYPE CONVERSION 
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

# DATA STRUCTURES
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

# OPERATORS
Operators in Python are symbols or keywords that perform operations on one or more operands (values or variables). 
They allow you to perform tasks like arithmetic calculations, comparisons, logical operations, and more.

Arithmetic Operators: These operators perform arithmetic operations like addition, subtraction, multiplication, division, etc.
	x = 10
	y = 3

	print(x + y)  # Addition
	print(x - y)  # Subtraction
	print(x * y)  # Multiplication
	print(x / y)  # Division
	print(x // y) # Integer Division
	print(x % y)  # Modulus (Remainder)
	print(x ** y) # Exponentiation

Comparison Operators: These operators are used to compare the values of operands and return True or False.
	x = 10
	y = 20

	print(x == y)  # Equal to
	print(x != y)  # Not equal to
	print(x > y)   # Greater than
	print(x < y)   # Less than
	print(x >= y)  # Greater than or equal to
	print(x <= y)  # Less than or equal to

Logical Operators: These operators perform logical operations on Boolean values (True or False).
	x = True
	y = False
	
	print(x and y)  # Logical AND
	print(x or y)   # Logical OR
	print(not x)    # Logical NOT

Assignment Operators: These operators are used to assign values to variables.
	x = 10       # Assigns the value 10 to x
	x += 5      # Adds 5 to the current value of x (Equivalent to x = x + 5)

Membership Operators: These operators are used to test for membership in a sequence (lists, tuples, strings).
```
	x = [1, 2, 3, 4, 5]

	print(3 in x)   # Checks if 3 is in the list x
	print(6 not in x) # Checks if 6 is not in the list x
```

Identity Operators: These operators are used to compare the memory locations of two objects.

```
	x = [1, 2, 3]
	y = [1, 2, 3]
	z = x

	print(x is y)   # Checks if x and y refer to the same object
	print(x is not z) # Checks if x and z do not refer to the same object
```

# CONTROL FLOW 

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

Loops (for, while): Loops allow you to execute a block of code repeatedly.
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

Break and Continue Statements: These statements are used within loops to alter the flow of control.
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

# FUNCTIONS

Functions in Python are blocks of reusable code that perform a specific task. 
They help in organizing code into manageable pieces, making it easier to understand, debug, and maintain. 

Defining Functions: You define a function using the def keyword followed by the function name and parentheses ().

```
	def greet(name):
    	print("Hello, " + name + "!")
```

In this example, greet is the function name, and name is a parameter that the function expects.

Calling Functions: To execute the code inside a function, you "call" the function by using its name followed by parentheses and passing any required arguments.
	greet("Alice")

This line of code calls the greet function and passes the string "Alice" as the name parameter.

Return Statement: Functions can optionally return a value using the return statement. This allows the function to send data back to the caller.

```
	def add(x, y):
    	return x + y
```

In this example, the add function takes two parameters x and y, adds them together, and returns the result.

Function Arguments: Functions can have both positional and keyword arguments. 
Positional arguments are passed based on their position, while keyword arguments are passed with a keyword and a value.
	def greet(name, message="Hello"):
    	print(message + ", " + name + "!")
	
In this modified greet function, message is a keyword argument with a default value of "Hello". 
If no message is provided when calling the function, it will default to "Hello".

Docstrings: Docstrings are documentation strings that describe what the function does. 
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

# Classes and Objects 

In Python, a class is a blueprint for creating objects, and an object is an instance of a class. 

Class: A class is a template or blueprint that defines the attributes (properties) and methods (functions) that all objects of that class will have. 
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

Object: An object is an instance of a class. 
It's a specific realization of the class, with its own unique attributes and methods. 
You create objects from a class using the class name followed by parentheses (). 
	my_dog = Dog("Buddy", 3)

In this example, my_dog is an object (instance) of the Dog class. It has its own name ("Buddy") and age (3).

Attributes: Attributes are variables that hold data associated with a class or an object. 
They represent the state of the object. You access attributes using dot notation (object.attribute).
	print(my_dog.name)  # Output: Buddy
	print(my_dog.age)   # Output: 3

Methods: Methods are functions that are defined within a class and perform operations on the object's attributes. 
They represent the behavior of the object. You call methods using dot notation (object.method()).
```
my_dog.bark()  # Output: Buddy says Woof!
```

Constructor (__init__): The __init__ method is a special method called the constructor. 
It is automatically called when you create a new object of the class and is used to initialize the object's attributes.

```
def __init__(self, name, age):
self.name = name
self.age = age
```

Self: self is a reference to the current instance of the class. It is used to access variables and methods within the class.

Inheritance: Inheritance is a mechanism in which a new class inherits properties and behavior (attributes and methods) from an existing class. 
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

Integers (int): <br>
Integers are whole numbers, meaning they don't have any decimal or fractional parts. <br>
Examples of integers are: -10, 0, 42, 1000, etc. <br>
In Python, integers can be positive, negative, or zero. <br>
You can perform arithmetic operations like addition, subtraction, multiplication, and division on integers. <br>
In Python, integer variables are declared without any decimal point.

```
x = 5    # This is an integer assignment
y = -10  # This is also an integer assignment
```

Floating-Point Numbers (float): <br>
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














