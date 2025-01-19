"""
@author: Maherdeep Chhabra
@email: mchhabr5@asu.edu
"""


#Answer 1
for i in range(2, 27, 2):
    print(f"Generated number: {i}")
print()

#Answer 2
for i in range(3, 0, -1):
    for j in range(1001, 1006):
        print(f"{i};{j}")
print()

#Answer 3
input1 = int(input('Enter an integer number: '))
### Place your code below this line ###
if input1 < 0:
    print("Input1 is negative")
elif input1 == 0:
    print("Input1 is zero")
elif input1 > 0 and input1 <= 20:
    print("Input1 is positive but less than or equal to 20")
else:
    print("Input1 is greater than 20")
### Place your code above this line ###
print()

#Answer 4
j = 0
sum11 = 0
while j < 10:
    sum11 += j * 11
    print(f"j: {j} sum11: {sum11}")
    j += 1
print('')
print('Total sum11 is:', sum11)
print()
#Answer 5
historical = 3, 5, 1, 9, 0, 3, 9, 2, 4, 7
predictiona = 1, 5, 4, 1, 7, 7, 1, 0, 3, 9
predictionb = 6, 0, 4, 3, 4, 4, 8, 4, 3, 7

print('')
print('historical:', historical)
print('predictiona:', predictiona)
print('predictionb:', predictionb)
print('')

### Place your code below this line ###
topresults = zip(historical, predictiona, predictionb)

for hist, pred_a, pred_b in topresults:
    print(f"historical: {hist} prediction a: {pred_a} prediction b: {pred_b}")
### Place your code above this line ###
print()

#Answer 6
### Place your code below this line ###
btcdec1 = [11234, 12475]
btcdec1.append(14560)

btcdec2 = []
btcdec2.append(15630)
btcdec2.append(12475)
btcdec2.append(14972)

btcdec1.extend(btcdec2)
btcdec1.sort()
### Place your code above this line ###
print(btcdec1)
print()

#Answer 7
list1 = [-4, 2, 7, -6, 3, -5, 8, 10, 4, -10]
list2 = [1, 7, 8, -10, 2, 6, -1, 10, -3, -8]
cnt = 0
for item in list1:
    ### Place your code below this line ###
    if item in list2:
        cnt += 1
    ### Place your code above this line ###
print('Number of common items between list1 and list2 is:', cnt)
print()

#Answer 8
import math

growth_rates = [1.03, 0.9, 1.36, 1.23, 1.08, 1.12, 1.55, 1.06, 1.05, 0.92]

### Place your code below this line ###
product = 1
for rate in growth_rates:
    product *= rate

geo_mean = round(math.pow(product, 1 / len(growth_rates)), 2)
### Place your code above this line ###

print('Compounded annual growth rate is:', geo_mean)




















