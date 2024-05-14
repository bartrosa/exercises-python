

numbers = [1, 2, 3, 4, 5]

###############################################################################
# C

# Comprehensions -  concise way to create containers such as lists, 
# dictionaries, sets, and even generators. They provide a readable and 
# expressive way to create new sequences based on existing sequences, applying 
# a specific condition or operation to each element

squares = [x**2 for x in range(10)]  # List
square_dict = {x: x**2 for x in range(5)} # Dictionary
unique_squares = {x**2 for x in [-1, 1, 2]}  # Set

squares_gen = (x**2 for x in range(10)) # Generator
for square in squares_gen:
    print(square)

# Context manager - a programming construct that provides explicit support for 
# the with statement, ensuring that resources are properly managed. For example, 
# when working with files, a context manager guarantees that the file will be 
# properly closed after its block of code is executed, regardless of whether an 
# error occurs during file processing. This pattern is very useful for managing 
# resources such as file handles, network connections, or locks that need to be 
# explicitly acquired and released.

with open('example.txt', 'r') as file:
    data = file.read()

#

class ManagedFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'r')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


with ManagedFile('example.txt') as file:
    data = file.read()

# 

from contextlib import contextmanager

@contextmanager
def managed_file(filename):
    try:
        f = open(filename, 'r')
        yield f
    finally:
        f.close()

with managed_file('example.txt') as file:
    data = file.read()

###############################################################################
# D

# Decorators -  tool that allows you to modify the behavior of a function or a 
# class. It is a higher-order function that takes another function or a class 
# as an argument and returns a function or a class. 

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

#

def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")

greet("Alice")

#

class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print("Hello!")

say_hello()
say_hello()

#

from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper function"""
        print("Something is happening before the function is called.")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def say_hello():
    """Greets the user"""
    print("Hello!")

print(say_hello.__name__)  # Outputs: 'say_hello'
print(say_hello.__doc__)   # Outputs: 'Greets the user'

#

def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Database:
    pass

###############################################################################
# G

# Generator -   a type of iterable, like a list or a tuple, but unlike lists, 
# generators don't store all their values in memory at once. Instead, they 
# generate values on the fly as needed, which allows them to be more 
# memory-efficient when dealing with large datasets or complex sequences of data.

def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

counter = count_up_to(5)
for num in counter:
    print(num)



###############################################################################
# M

# map()         function applies a specified function to each item of an 
# iterable (like list or tuple) and returns an iterator that  provides the 
# results. This function is often used for transforming data. 

def square(x):
    return x ** 2

squared_numbers = map(square, numbers)
print(list(squared_numbers))

###############################################################################
# R

# reduce()      used to apply a given function cumulatively to the items of an 
# iterable, optionally starting with an initial value, to reduce the iterable 
# to a single value. This function is useful for performing computations that 
# cumulatively combine all elements of a list into a single result. 

from functools import reduce

def add(x, y):
    return x + y

result = reduce(add, numbers)
print(result)

###############################################################################
# T

# Type hints -  a way of explicitly specifying the expected data types of 
# variables, function parameters, and function return values. 

def greet_th(name: str) -> str:
    return 'Hello, ' + name

