'''
@author: Maherdeep Chhabra
@email: mchhabr5@asu.edu
'''
#Answer 1
# Assign values to two integer objects and one float object
integer1 = 5
integer2 = 10
float1 = 3.5
# Sum the three variables and assign the result to a variable named results1
results1 = integer1 + integer2 + float1
# Output the value of results1
print("Value of results1:", results1)
# Output the type of results1
print("Type of results1:", type(results1))
print()



# Answer 2
# Assign the multi-line string to a variable named string1
string1 = """Success is not the key to happiness. 
Happiness is the key to success. 
If you love what you are doing, 
you will be successful."""
# Use the count method to count the occurrences of 's' in the string
s_count = string1.count('s')
# Output the count
print("s_count")
print()



#Asnwer 3
import math
# Assign the value of π to a variable named var1
var1 = math.pi
# Round the value of var1 to three decimal places
rounded_var1 = round(var1, 3)
# Output the rounded value
print("The value of π rounded to three decimal places is:", rounded_var1)
print()



#Answer 4
var1 = int(input('Enter a var1 number: '))
var2 = int(input('Enter a var2 number: '))
### Place your code below this line ###
var3 = var1 * var2
### Place your code above this line ###
print('')
print('The result of the multiplication of var1 and var2 is:', var3)



#Answer 5
numerator1 = '32000'
denominator1 = '1000'
### Place your code below this line ###
# Convert strings to integers and perform division to produce a float result
var3 = float(int(numerator1) / int(denominator1))
### Place your code above this line ###
print('')
print('The result of dividing numerator1 by denominator1 is:', var3)
print()



#Answer 6
year = 1991
author = 'Guido van Rossum'
### Place your code below this line ###
# Create the variable text1 using concatenation
text1 = "Python is a general-purpose programming language released in " + str(year) + " by " + author
### Place your code above this line ###
print(text1)
print()



#Answer 7
sunny = True
warm = False
print('Is it True or False that I should go out for ice cream?:', (sunny and warm))
# I expect the result to be False because the expression uses the "and" operator.
# The "and" operator returns True only when both variables are True.
# Since warm is False, the whole expression evaluates to False.
print()



#Answer 8 
# Add correct import statement
from datetime import datetime, timedelta
# Initialize the dt variable
dt = datetime(2021, 9, 6, 18, 51, 17)
### Place your code below this line ###
# Subtract 4 weeks (28 days) from dt
dt2 = dt - timedelta(days=28)
# Format dt2 into a string as "08/09/2021"
dt2_str = dt2.strftime("%m/%d/%Y")
### Place your code above this line ###
print('dt2_str date is:', dt2_str)




















