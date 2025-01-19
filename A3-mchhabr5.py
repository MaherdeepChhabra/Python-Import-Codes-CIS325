"""
@author: Maherdeep Chhabra 
@email: mchhabr5@asu.edu
"""
### Answer to Question 1
dict1 = {'e': 2, 'j': 4, 'a': 3, 't': 6, 'q': 1}
### Place your code below this line ###
for key in reversed(sorted(dict1.keys())):
    print(f"key: {key} ; value: {dict1[key]}")
### Place your code above this line ###





### Answer to Question 2
mylist = ['action', 'table', 'tennis', 'apple', 'trap']
# Description of the dictionary setdefault() method:
# (1) What does setdefault() do?
#     setdefault() method returns the value of a key if it is in the dictionary; if not, it inserts the key with a specified value and returns that value.
# (2) Syntax of setdefault():
#     dictionary.setdefault(key, default=None)
# (3) Arguments:
#     key (required): The key to be searched in the dictionary.
#     default (optional): The value to be set if the key is not already in the dictionary. If not provided, default is None.
# Create a dictionary of lists categorized by the first letter of each word
dictA = {}
for word in mylist:
    first_letter = word[0]  # Extract the first letter of the word
    dictA.setdefault(first_letter, []).append(word)  # Use setdefault to ensure a list is available for appending
print('dictA:', dictA)





### Answer to Question 3
A = set(range(2, 21, 2))  # Multiples of 2 between 1 and 20
B = set(range(5, 21, 5))  # Multiples of 5 between 1 and 20
### Place your code below this line ###
# 1. Union of A and B: all unique items from both sets.
U = A.union(B)
# 2. Intersection of A and B: items common to both sets.
I = A.intersection(B)
# 3. Symmetric Difference of A and B: items in either A or B but not both.
S = A.symmetric_difference(B)
### Place your code above this line ###
print('U:', U)
print('I:', I)
print('S:', S)




### Answer to Question 4
def is_prime(num):
   
    if num > 1:  
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    else:
        return False
# Test the function with the provided examples
print(is_prime(1))  # False
print(type(is_prime(1)))  # <class 'bool'>
print(is_prime(5))  # True
print(is_prime(6))  # False
print('Prime' if is_prime(11) else 'Not prime')  # Prime







### Answer to Question 5
lorem = 'ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi aliquip'
lorem_words = lorem.split(sep=' ')
print(lorem_words)
# Description of the string split() method:
# (1) The split() method divides a string into a list by separating the string at each occurrence of a specified delimiter.
# (2) Syntax of split(): string.split(sep=None, maxsplit=-1)
# (3) Arguments:
#     sep (optional): The string delimiter on which the string splits. If sep is not specified or is None, the split is done on all whitespace.
#     maxsplit (optional): The maximum number of splits to do. Default is -1, which means "all occurrences".
# Explanation of how lorem_words got its value:
# lorem_words was created by splitting the string stored in 'lorem' using spaces as delimiters.
# The split() method iterates over the string, cutting at each space and adding each segment as an element in the list lorem_words.
word_len = {}
for word in sorted(lorem_words):
    word_len[word] = len(word)  
keys = list(word_len.keys())
formatted_output = '{'
for i, key in enumerate(keys):
    formatted_output += f"'{key}': {word_len[key]}"
    if i < len(keys) - 1:
        formatted_output += ', '
    if (i + 1) % 6 == 0 and i < len(keys) - 1:
        formatted_output += '\n'
formatted_output += '}'
print(formatted_output)





### Answer to Question 6
def get_char_count_dict(txt):
    # Check if the input is a string
    if not isinstance(txt, str):
        return -1
    txt = txt.lower()
    char_count_dict = {}
    for char in txt:
        if char != ' ':  # Skip whitespace characters
            if char in char_count_dict:
                char_count_dict[char] += 1  # Increment the count of the character if it already exists
            else:
                char_count_dict[char] = 1  # Add new character to the dictionary with a count of 1
    # Return the dictionary containing characters and their counts
    return char_count_dict
# Example function calls and their outputs for correctness checks
print(get_char_count_dict('little'))         # {'l': 2, 'i': 1, 't': 2, 'e': 1}
print(get_char_count_dict('LiTtle'))         # {'l': 2, 'i': 1, 't': 2, 'e': 1}
print(get_char_count_dict(127))              # -1
print(get_char_count_dict(' '))              # {}
print(get_char_count_dict('The only impossible journey is the one you never begin!'))
# {'t': 2, 'h': 2, 'e': 8, 'o': 5, 'n': 5, 'l': 4, 'y': 3, 'i': 4, 'm': 1, 'p': 1, 's': 3, 'b': 2, 'j': 1, 'u': 2, 'r': 2, 'v': 1, 'g': 1, '!': 1}





### Answer to Question 7
# Creating a dictionary A using dictionary comprehension
A = {c: round((9/5) * c + 32, 1) for c in range(36)}  # Range 36 to include 0 through 35
# Print the dictionary A
print(A)






### Answer to Question 8
def sort_by_selected_key(dicts, keyname):
    sorted_dicts = sorted(dicts, key=lambda x: x[keyname])
    for dictionary in sorted_dicts:
        print(dictionary)
employees = [
    {'name': 'John', 'age': 28, 'years': 2.5},
    {'name': 'Lisa', 'age': 24, 'years': 3.1},
    {'name': 'Ella', 'age': 31, 'years': 2.9}
]

# Testing the function with different keys
D = sort_by_selected_key(employees, 'name')  

D = sort_by_selected_key(employees, 'age')  

D = sort_by_selected_key(employees, 'years') 























