"""
@author: Maherdeep Chhabra
@email: mchhabr5@asu.edu
"""
# Answer to Question 1
import random
# The randint() function from the random package generates a random integer within a specified range.
# Syntax: randint(a, b)
# Arguments:
#   - a (required): The start of the range (inclusive).
#   - b (required): The end of the range (inclusive).
# The function returns a random integer N such that a <= N <= b.
def lottery(n=6):
    """Generator function that yields n random integers between 1 and 40."""
    for _ in range(n):
        yield random.randint(1, 40)
# Test the generator by printing out random numbers
for i in lottery(4):
    print('Random number:', i)
'''
 The difference between a generator function that uses "yield" and an ordinary
 function with "return" is that the former may pause execution, maintaining its
 state, then resume from where it stopped on subsequent calls. That makes it 
 ideal for producing sequences of data without loading everything into memory
 at once, unlike regular functions, which terminate and return a single value
 or a complete set of values after execution.
'''
print()



# Answer to Question 2
import random
# Example 1: Converting a string to an integer where the string is not a valid integer
try:
    int("abc")
except ValueError as e:
    print("Example 1:", e)
# Example 2: Using an invalid start index with 'str.index' method
try:
    'hello'.index('z')
except ValueError as e:
    print("Example 2:", e)
# Example 3: Passing an invalid value to the split() method of a string
try:
    "hello,world".split(',')
    "hello world".split('')  # Empty separator is invalid
except ValueError as e:
    print("Example 3:", e)
# Example 4: Specifying an invalid base for integer conversion
try:
    int("101", 1)  # Base must be between 2 and 36, inclusive
except ValueError as e:
    print("Example 4:", e)
# Example 5: Creating a datetime object with an invalid day
try:
    from datetime import datetime
    datetime.strptime('30-02-2020', '%d-%m-%Y')
except ValueError as e:
    print("Example 5:", e)
print()
    


# Answer to Question 3
# Example 1: Adding a string to an integer
try:
    'hello' + 5
except TypeError as e:
    print("Example 1:", e)
# Example 2: Trying to iterate over a non-iterable (integer)
try:
    for i in 123:
        print(i)
except TypeError as e:
    print("Example 2:", e)
# Example 3: Attempting to call a non-callable object
try:
    a = 10
    a()
except TypeError as e:
    print("Example 3:", e)
# Example 4: Passing an argument of the wrong type to a function
try:
    def increment(x):
        return x + 1
    increment("one")
except TypeError as e:
    print("Example 4:", e)
# Example 5: Accessing an item in a list with a slice instead of an integer
try:
    my_list = [1, 2, 3]
    my_list['1:2']
except TypeError as e:
    print("Example 5:", e)
print()



# Answer to Question 4
def break_modules(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "All numbers must be greater than zero."
    except TypeError:
        return "Unknown error, please check your numbers." 
print(break_modules(5, 2))  # Outputs 2.5
print(break_modules(7, 0))  # Outputs "All numbers must be greater than zero."
print(break_modules(7, 'ten'))# Outputs "Unknown error, please check your numbers."
print(" ")
    


# Answer to Question 5    
class myfirstclass:
    def __init__(self, num):
        if num <= 1:
            raise ValueError("The number must be greater than one.")
        self.num = num

    def methoda(self):
        return self.num ** 2  # Raise the number to the power of 2

    def methodb(self):
        return self.num ** 3  # Raise the number to the power of 3
myobj = myfirstclass(4)
print(myobj.methoda())  # This will output 16 to the console
print(myobj.methodb())  # This will output 64 to the console
print()



# Answer to Question 6
class parentclass:
    def __init__(self, num):
        if num <= 1:
            raise ValueError("The number must be greater than one.")
        self.num = num

    def methoda(self):
        return self.num ** 2

class childclass(parentclass):
    def methodb(self):
        return self.num ** 3

    def methodc(self):
        return self.num ** 4
# Creating an instance of childclass
myobj1 = childclass(10)
print(myobj1.methoda())  # This will output 100 to the console
print(myobj1.methodb())  # This will output 1000 to the console
print(myobj1.methodc())  # This will output 10000 to the console


