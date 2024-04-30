INTRODUCTION	

# THE ZEN OF PYTHON 
	
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

# VARIABLES AND TYPES
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
	x = [1, 2, 3, 4, 5]

	print(3 in x)   # Checks if 3 is in the list x
	print(6 not in x) # Checks if 6 is not in the list x

Identity Operators: These operators are used to compare the memory locations of two objects.
	x = [1, 2, 3]
	y = [1, 2, 3]
	z = x

	print(x is y)   # Checks if x and y refer to the same object
	print(x is not z) # Checks if x and z do not refer to the same object

# CONTROL FLOW 

Control flow in Python refers to the order in which statements are executed in a program. 
It allows you to make decisions, execute code conditionally, and repeat code based on certain conditions. 

Conditional Statements (if, elif, else): Conditional statements allow you to execute different blocks of code based on specified conditions.
	x = 10

	if x > 0:
    	print("x is positive")
	elif x == 0:
    	print("x is zero")
	else:
    	print("x is negative")

In this example, the if, elif, and else statements check the value of x and execute different print statements accordingly.

Loops (for, while): Loops allow you to execute a block of code repeatedly.
	For Loops: Used to iterate over a sequence (like lists, tuples, or strings) or to execute a block of code a specific number of times.
		fruits = ["apple", "banana", "cherry"]

		for fruit in fruits:
    		print(fruit)
	While Loops: Continuously executes a block of code as long as a specified condition is true.
		x = 0

		while x < 5:
    		print(x)
    		x += 1
Break and Continue Statements: These statements are used within loops to alter the flow of control.
	Break: Terminates the loop prematurely when a certain condition is met.
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
Exception Handling (try, except, finally): Allows you to handle errors or exceptional situations gracefully without crashing the program.
	try:
    		x = 10 / 0
	except ZeroDivisionError:
    		print("Error: Division by zero")
	finally:
    		print("This block always executes")

In this example, the try block attempts to execute the code inside it, and if an exception occurs, the except block catches the exception and handles it. 
The finally block always executes, regardless of whether an exception occurred or not.
Understanding control flow is essential for writing programs that can make decisions, iterate over data, and handle errors effectively. 
It gives you the flexibility to create complex logic and solve a wide range of problems in Python.





