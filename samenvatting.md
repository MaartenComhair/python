# Summary

- [Summary](#summary)
  - [Basic functions \& methods](#basic-functions--methods)
  - [Basic exercise for beginners](#basic-exercise-for-beginners)
  - [Python if else, for loop, and range() Exercises](#python-if-else-for-loop-and-range-exercises)
  - [Python String Exercise](#python-string-exercise)
  - [Python Function Exercise](#python-function-exercise)
  - [Python List Exercise with Solutions](#python-list-exercise-with-solutions)
  - [Python Set Exercise with Solutions](#python-set-exercise-with-solutions)
  - [Redemption arc](#Redemption-arc)
  - [Learnning](#learnning)

  
## Basic functions & methods
```python

https://orgpad.info/s/sbwXdJ9N5wc

list()
str()
int()
float()
bool()
set()
    - verwijdert duplicates
    - maakt van bv. een lijst een set, die niet meer kan veranderd worden
dict()
    - meerder combinaties van keys (string) & values (any type)
tuple()

*
/
+
-
<
<=
>
>=
==
!=
15 % 6 = 3
pow(getal, tot de macht)


print("")
f"{}"
input()
len()

if x > y:
elif x < y:
else:

while x is True:

continue
break

for i in range(1,10)

#str
.lower() 
.upper()
.isdidget()
.split()
    - verwijdert hetgene tussen haakjes & geeft een list als output:
    - ['Maarten'] i.p.v. ['M','a','a','r','t','e','n']
''.join(str_variable)

#list

.sort()
#lijst permanent alfabetisch
#reverse = True

sorted()
#lijst tijdelijk alfabetisch
#reverse = True

.reverse()
#lijst tijdelijk reversed

.append()
#item toevoegen achteraan lijst

.join()
#lijsten samenvoegen

.remove()
#item verwijderen met index

.insert()
#item toevoegen met index

.pop()
#item verwijderen achteraan lijst

#convert str to list
message = "hello there sam"
words = message.split()
print(words)
# Prints: ["hello", "there", "sam"]

#convert list to str
list_of_words = ["hello", "there", "sam"]
sentence = " ".join(list_of_words)
print(sentence)
# Prints: "hello there sam"

len()
#lengte v/d lijst bepalen

del
#lijst verwijderen

range(x,y,z)
#lijst aanmaken van x tot y met z-sprongen

set()
#verwijdert duplicates




#dict
.keys()
#geeft enkel key's weer

.values()
#geeft enkel value's weer

.items()
#geeft keys & value's weer

random.choice()





#str + list
.count()
.replace()
.find()

import random

variabele[::-1]
#leest variabele van achter naar voor


sensei = "Michiel"
print(sensei[-5:-3])
terminal: "ch"
#achterste value in een range is nooit inclusief:


print(i, end = '')
#De hieropvolgende print print op dezelfde regel


list = [1,2,3,4,5,6,7,8,9,10]
print(list[0:2])
#Begint op index 0 tot 2
print(list[:2])
#Begint op index 0 tot 2

print(list[0::2])
#Begint op index 0 & print om de 2 indexen
print(list[::-1])
#Maakt achterwaartse sprongen ter waarde van 1


#Freestyle met Grimvine
x = {"Apple":10, "Peer":2}
y = x.get("Apple")
print(y)
x["Apple"] = 20
print(x)


You can add the letter e or E followed by a positive or negative integer to specify that you're using scientific notation.
print(16e3)
# Prints 16000.0

print(7.1e-2)
# Prints 0.071


You can write an integer in Python using binary syntax using the 0b prefix:
print(0b0001)
# Prints 1

print(0b0101)
# Prints 5



```

## Basic exercise for beginners
```python

#Mimo exercise 1: Rock, paper, scissors
import random
print("Let's play rock, paper & scissors.")
choices = ["rock" , "paper" , "scissors"]
computer_choice = random.choice(choices)
player_choice = input("Make your descision: ").lower()
print(F"Computer chose: {computer_choice}")
if player_choice == ("rock") and computer_choice == ("scissors") or player_choice == ("paper") and computer_choice == ("rock") or player_choice == ("scissors") and computer_choice == ("paper"):
    print("Player wins")
elif player_choice == computer_choice:
    print("Tie")
else:
    print("Computer wins")

#Mimo exercise 2: to do list
todo_list = []

while True:
  if not todo_list:
    print("Your ToDo list is empty")
  else:
    index = 0
    for task in todo_list:
      print(f"{index}. {task}")
      index += 1
  print("Options:")
  print("1)Add Task")
  print("2)Remove Task")
  print("3) Quit")

  choice = input("Enter choice (1 , 2 or 3):")

  if choice == "1":
    print("Adding task)")
    new_task = input("Enter task: ")
    todo_list.append(new_task)
    print(f"Task added: {new_task}")
    
  elif choice == "2":
    task_amount = (len(todo_list))
    print(task_amount)
    if not todo_list:
      print("Todo list is empty")
    else:
      todo_list.pop()

  elif choice == "3":
    print("Quitting")
    break


#freestyle
sterretje = ["*"]
for i in sterretje:
    sterretje.append("*")
    print(i, end = '')
    if len(sterretje) == 3:
        break


sterretje = "*"
for i in range(4):
    print(sterretje * (i+1))


for i in range(1,5):
    print(i*str(i))


for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()






#Exercise 1: Calculate the multiplication and sum of two numbers
number_1 = 200
number_2 = 30
multiplication = number_1 * number_2

if multiplication <= 1000:
    print(multiplication)
else:
    print(number_1 + number_2)



#Exercise 2: Print the Sum of a Current Number and a Previous number
for i in range(10):
    if i == 0:
        print(f"Current number {i} Previous Number {i} Sum: {i}")
    else:
        print(f"Current number {i} Previous Number {i-1} Sum: {i + i - 1}")



#Exercise 3: Print characters present at an even index number
name = "Maarten"
for i in range(len(name)):
    if i % 2 == 0:
        print(name[i])



#Exercise 4: Remove first n characters from a string
name = "Maarten"
times = 3
for i in range(times):
    if i < times:
        name = name.replace(name[0], '')
print(name)



#Exercise 5: Check if the first and last numbers of a list are the same
list = [10,5,6,1,7,6,2]
if list[0] == list[-1]:
    print("the same")
else:
    print("not the same")



#Exercise 6: Display numbers divisible by 5
list = [10, 20, 33, 46, 55]
list_deluxe = []
for i in range(len(list)):
    if list[i] % 5 == 0:
        print(list[i])
        list_deluxe.append(list[i])
print(list_deluxe)



#Exercise 7: Find the number of occurrences of a substring in a string
mottige_zin =  "Emma is good developer. Emma is a writer"
print(mottige_zin.count("Emma"))



#Exercise 8: Print the following pattern
for i in range(5): 
    if i != 0:
        print()
    for j in range(i+1):
        print(i+1, end ='')



#Exercise 9: Check Palindrome Number
#reversed string
number = 12524
reversed_number = str(number)[::-1]

if str(number) == reversed_number:
    print("yup")
else:
    print("nope")



#Exercise 10: Merge two lists using the following condition
#even & odd numbers
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
new_list = []

for i in range(len(list1)):
    if list1[i] % 2 != 0:
        new_list.append(list1[i])

for j in range(len(list2)):
    if list2[j] % 2 == 0:
        new_list.append(list2[j])

print(new_list)



#Exercise 11: Get each digit from a number in the reverse order.
#possibility 1:
nummer = 123456
nummer_str = str(nummer)
addition = "1"

for i in range(len(nummer_str + addition)):
    if i > 0:
        reversed_nummer = (nummer_str[-i])
        print(reversed_nummer, end = '')

#possibility 2:
nummer = 123456
reversed_number = str(nummer)[::-1]
print(reversed_number)



#Exercise 12: Calculate income tax
income = 45000
if income < 10000:
    print("No taxation")
elif income < 20000 and income > 10000:
    tax_value = income * 0.1
    print(tax_value)
else:
    tax_value = 1000 + (income - 20000) * 0.2
    print(f"Total pay: {tax_value}")



#Exercise 13: Print multiplication table from 1 to 10
for i in range(1,11):
    print()
    for j in range(1,11):
        if j == 1:
            print(j*i, end = '     ')
        else:
            print(j*i, end = ' ')



#Exercise 14: Print a downward half-pyramid pattern of stars
for i in range(6):
    for j in range(6-i):
        print("*", end = '')
    print()



#Exercise 15: Get an int value of base raises to the power of exponent
num1 = 2
num2 = 4
print(pow(num1,num2))



```
f## Python Input and Output Exercise
```python



#Exercise 1: Accept numbers from a user
num1 = input("Give a number: ")
while not num1.isdigit():
    print("you stoopid, give a number: ")
    num1 = input("Give a number: ")

num2 = input("Give a number: ")
while not num2.isdigit():
    print("you stoopid, give a number: ")
    num2 = input("Give a number: ")

multiplication = int(num1) * int(num2)
print(multiplication)



#Exercise 5: Accept a list of 5 float numbers as an input from the user
list = []
for i in range(5):
    number = input("Give a number: ")
    list.append(number)
print(list)



#Exercise 6: Write all content of a given file into a new file by skipping line number 5
#https://pynative.com/python/file-handling/



#Exercise 8: Format variables using a string.format() method.
totalMoney = 1000
quantity = 3
price = 450
print(f"I have {totalMoney} dollars so I can buy {quantity} football for {price} dollars")



```
## Python if else, for loop, and range() Exercises
```python



#Exercise 1: Print first 10 natural numbers using while loop
for i in range(1,11):
    print(i)



#Exercise 2: Print the following pattern
for i in range(1,6):
    for j in range(i):
        print(j+1, end = '')
    print()



#Exercise 3: Calculate sum of all numbers from 1 to a given number
    number = int(input("Give a number: "))
sum = 0

for i in range(1, number + 1):
    sum += i
    print(sum)
print(sum)



#Exercise 4: Print multiplication table of a given number
number = int(input("Give a number: "))

for i in range(1,11):
    print(i * number)



#Exercise 5: Display numbers from a list using a loop
    numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    if i > 500:
        break
    elif i > 150:
        continue
    elif i % 5 == 0:
        print(i)



#Exercise 6: Count the total number of digits in a number
number = 75869
print(len(str(number)))



#Exercise 7: Print the following pattern
y = 5
x = 6
for i in range(y):
    print()
    x -= 1
    for j in range(y-i):
        print(x-j, end = '')



#Exercise 8: Print list in reverse order using a loop
list1 = [10, 20, 30, 40, 50]
for i in range(1,len(list1)+1):
        print(list1[-i])



#Exercise 9: Display numbers from -10 to -1 using for loop
x = 11
for i in range(1,x):
    print(i-x)



#Exercise 10: Display a message “Done” after the successful execution of the for loop
x = 5
for i in range(x):
    print(i)
    if i == x - 1:
        print("Done!")



#Exercise 12: Display Fibonacci series up to 10 terms
list = [0,1]
for i in range(10):
    if len(list) == 2:
        print(list[i])
    x = list[i]+list[i+1]
    list.append(x)
    print(x)



#Exercise 13: Find the factorial of a given number
x = 5
for i in range(1, x):
    x = x * i
print(x)



#Exercise 14: Reverse a integer number
integer = 76542
for i in range(1, len(str(integer)) + 1):
    x = print(str(integer)[-i], end = '')



#Exercise 15: Print elements from a given list present at odd index positions
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in range(len(my_list)):
    if i % 2 != 0:
        print(my_list[i])



#Exercise 16: Calculate the cube of all numbers from 1 to a given number
current_number = 6

for i in range(1, current_number + 1):
    print(f"Current number is: {i} and the cube is {i*i*i}")



#Exercise 17: Find the sum of the series up to n terms
n = 5
x = 2
sum = 0

for i in range(1, n + 1):
    sum += x
    x = x * 10 + 2

print(sum)



#Exercise 18: Print the following pattern
x = "*"
for i in range(1,6):
    print()
    for j in range(i):
        print(x, end = '')
        x += "*"
        x = "*"

for k in range(1,5):
    print()
    for l in range(5-k):
        print("*", end = '')



```
## Python String Exercise
```python



#Exercise 1A: Create a string made of the first, middle and last character
name = input("what is your name? ")
print(name[0], end = '')
print(name[int(len(name)/2)], end = '')
print(name[int(len(name)-1)])



#Exercise 1B: Create a string made of the middle three characters
name = "Maarten"
i = int(len(name)/2)
print(name[i-1])
print(name[i])
print(name[i+1])




#Exercise 2: Append new string in the middle of a given string
s1 = "Ault"
s2 = "Kelly"

first_halve_s1 = s1[:int(len(s1)/2)]
second_halve_s1 = s1[int(len(s1)/2):]
sum = first_halve_s1 + s2 + second_halve_s1
print(sum)



#Exercise 3: Create a new string made of the first, middle, and last characters of each input string
s1 = "America"
s2 = "Japan"

first_s1 = s1[0]
middle_s1 = s1[int(len(s1)/2)]
last_s1 = s1[-1]

first_s2 = s2[0]
middle_s2 = s2[int(len(s2)/2)]
last_s2 = s2[-1]

result = first_s1 + first_s2 + middle_s1 + middle_s2 + last_s1 + last_s2
print(result)



#Exercise 4: Arrange string characters such that lowercase letters should come first
str1 = "PyNaTive"
lower = []
upper = []
for i in range(len(str1)):
    if str1[i].islower():
        lower.append(str1[i])
    else:
        upper.append(str1[i])

combination = ''.join(lower + upper)
print(combination)



#Exercise 5: Count all letters, digits, and special symbols from a given string
str1 = "P@#yn26at^&i5ve"
digits = 0
symbols = 0
chars = 0

for i in range(len(str1)):
    if str1[i].isnumeric():
        digits += 1
    elif str1[i].isalpha():
        chars += 1
    else:
        symbols += 1

print(f"Digits: {digits}")
print(f"Symbols: {symbols}")
print(f"chars: {chars}")



#Exercise 6: Create a mixed String using the following rules
#Solution 1:
s1 = "Abc"
s2 = "Xyz"
list_1 = []
for i in range(len(s1)):
    list_1.append(s1[i])
    list_1.append(s2[len(s2)-1-i])


list_to_string = ''.join(list_1)
print(list_to_string)



#Solution 2:
s1 = "Abc"
s2 = "Xyz"
s3 = ""

length = len(s1) if len(s1) > len(s2) else len(s2)
#zodat de grootste string als lengte wordt gebruikt

s2 = s2[::-1]
#zodat s2 achterstevoren wordt toegevoegd

for i in range(length):
    if i < len(s1):
        s3 = s3 + s1[i]
    if i < len(s2):
        s3 = s3 + s2[i]
    
print(s3)



#Exercise 7: String characters balance Test
s1 = "Yn"
s2 = "PYnative"
counter = 0
for i in range(len(s1)):
    if s1[i] in s2:
        counter += 1

if counter == len(s1):
    print("True")
else:
    print("False")



#Exercise 8: Find all occurrences of a substring in a given string by ignoring the case
str1 = "Welcome to USA. usa awesome, isn't it?"

upper = str1.count("USA")
lower = str1.count("usa")
sum = upper + lower
print(sum)



#Exercise 9: Calculate the sum and average of the digits present in a string
str1 = "PYnative29@#8496"
som = 0
count = 0
for i in range(len(str1)):
    if str1[i].isdigit():
        som += int(str1[i])
        count += 1
    
print(som)
average = som / count
print(average)



#Exercise 10: Write a program to count occurrences of all characters within a string
#Eigen oplossing:
str1 = "Apple"
z = []
for i in range(len(str1)):
    count = str1.count(str1[i])
    z.append(f"{str1[i]}:{count}")

x = list(set(z))
x.sort()
print(x)



#Exercise 11: Reverse a given string
str1 = "PYnative"

print(str1[::-1])



#Exercise 12: Find the last position of a given substring
str1 = "Emma is a data scientist who knows Python. Emma works at google."

x = str1.rfind("Emma")
print(x)



#Exercise 13: Split a string on hyphens
#My solution
str1 = "Emma-is-a-data-scientist"

for i in range(len(str1)):
    if str1[i] == '-':
        print()
    else:
        print(str1[i], end = '')

#Solution
str1 = "Emma-is-a-data-scientist"
x = str1.split("-")
for i in x:
    print(i)



#Exercise 14: Remove empty strings from a list of strings
#solution 1:
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
lijst2 = []
for i in range(len(str_list)):
    if type(str_list[i]) == type(str()) and len(str_list[i]) > 0:
        lijst2.append(str_list[i])

print(lijst2)

#shortened solution 1:
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
lijst2 = []
for name in str_list:
    if type(name) == type(str()) and len(name) > 0:
        lijst2.append(name)

print(lijst2)



#Exercise 16: Removal all characters from a string except integers
str1 = 'I am 25 years and 10 months old'

for i in str1:
    if i.isdigit():
        print(i, end = '')



# Exercise 17: Find words with both alphabets and numbers
str1 = "Emma25 is Data scientist50 and AI Expert"
split_str1 = str1.split()

for item in split_str1:
        if any(char.isdigit() for char in item) and any(char.isalpha() for char in item):
            print(item)
        else:
            continue



#Exercise 18: Replace each special symbol with # in the following string
import re
str1 = "/*Jon is @developer & musician!!"
new_str1 = re.sub('[^a-zA-Z0-9 \n\.]', '#', str1)
print(new_str1)


    
```
## Python Function Exercise
```python



#Exercise 1: Create a function in Python
def demo(name, age):
    print(name, age)

demo("Maarten Comhair", 24)



#Exercise 2: Create a function with variable length of arguments
def func1(*args):
    for i in args:
        print(i)

print("Printing values")
func1(20,40,60,80,100)



#Exercise 3: Return multiple values from a function
def calculation(a, b):
    print(f"{a + b}, {a - b}")

calculation(40,10)



#Exercise 4: Create a function with a default argument
def showEmployee(name, salary):
    print(f"Name: {name} salary: {salary}")

showEmployee("Maarten", 2500)



#Exercise 5: Create an inner function to calculate the addition in the following way
def outer_function(a,b):
    def inner_function(a,b):
        return a + b
    sum = inner_function(a,b)
    return sum + 5

result = outer_function(2,3)
print(result)



#Exercise 6: Create a recursive function
def addition (n):
    if n:
        return n + addition(n - 1)
    else:
        return 0

solution = addition(10)
print(solution)



#Exercise 8: Generate a Python list of all the even numbers between 4 to 30
print(list(range(4,30,2)))



#Exercise 9: Find the largest item from a given list
x = [4, 6, 8, 24, 12, 2]
print(max(x))



```
## Python List Exercise with Solutions
```python



#Exercise 1: Reverse a list in Python
#My solution:
list1 = [100, 200, 300, 400, 500]
reversed_list1 = list1[::-1]
print(reversed_list1)



#Alternative solution:
list1 = [100, 200, 300, 400, 500]
list1.reverse()
print(list1)



#Exercise 2: Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = []

for i in range(len(list1)):
    list3.append(list1[i] + list2[i])
    
print(list3)



#Exercise 3: Turn every item of a list into its square
numbers = [1, 2, 3, 4, 5, 6, 7]
numbers_square = []

for i in range(len(numbers)):
    numbers_square.append(numbers[i] * numbers[i])

print(numbers_square)



#Exercise 4: Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3 = []

for i in range(len(list1)):
    for j in range(len(list2)):
        list3.append(list1[i] + list2[j])
    
print(list3)



#Exercise 5: Iterate both lists simultaneously
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for i in range(len(list1)):
    print(list1[i], end = ' ')
    print(list2[len(list2)-i-1])



#Exercise 6: Remove empty strings from the list of strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

for item in list1:
    if item == "":
        list1.remove(item)

print(list1)



#Exercise 7: Add new item to list after a specified item
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

list1[2][2].append(7000)
    
print(list1)



#Exercise 8: Extend nested list by adding the sublist
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]

list1[2][1][2].extend(sub_list)

print(list1)



#Exercise 9: Replace list’s item with new value if found
list1 = [5, 10, 15, 20, 25, 50, 20]

for i in range(len(list1)):
    if list1[i] == 20:
        list1[i] = 200
        break

print(list1)



#Exercise 10: Remove all occurrences of a specific item from a list.
list1 = [5, 20, 15, 20, 25, 50, 20]

for item in list1:
    if item == 20:
        list1.remove(item)

print(list1)



```
## Python Set Exercise with Solutions
```python



#Exercise 1: Add a list of elements to a set
sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]

for item in sample_list:
    sample_set.add(item)

print(sample_set)



#Exercise 2: Return a new set of identical items from two sets
#my solution:
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = {None}

for item in set1:
    if item in set2:
        set3.add(item)

set3.pop()
print(set3)


#solution 2:
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.intersection(set2))



#Exercise 3: Get Only unique items from two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set2.union(set1))



#Exercise 4: Update the first set with items that don’t exist in the second set
set1 = {10, 20, 30}
set2 = {20, 40, 50}

set1.difference_update(set2)
print(set1)



#Exercise 5: Remove items from the set at once
set1 = {10, 20, 30, 40, 50}
set2 = {10, 20 ,30}

set1.difference_update(set2)
print(set1)



#Exercise 6: Return a set of elements present in Set A or B, but not both
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set3 = set1.symmetric_difference(set2)
print(set3)



#Exercise 8: Update set1 by adding items from set2, except common items
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set1.symmetric_difference_update(set2)
print(set1)



#Exercise 9: Remove items from set1 that are not common to both set1 and set2
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set1.intersection_update(set2)
print(set1)


```
## Redemption arc
```python



def become_warrior(full_name, power):
    title = (F"{full_name} The warrior")
    level_increase = power + 1
    return title, level_increase

naam, nummer = become_warrior("Maarten Comhair", 10)
print(nummer)
print(naam)


###


def get_hurt(current_health, damage):
    dmg = damage
    health = current_health
    health -= dmg
    return dmg, health

x = input("How much hp did you have left?")
y = input("How hard did you get wacked?")
hp = get_hurt(int(x),int(y))

if x >= y:
    print("You died.")
else:
    print(f"You got wacked for a {hp[0]} and still have {hp[1]} hitpoints left")


###


def player_status(health):
    if health <= 0:
        print("You ded")
    elif health <= 5:
        print("You limpin")
    else:
        print("You a healthy boi")
    return None
x = player_status(6)
print(x)


###


def check_high_score(player_name, high_scoring_player_name, low_scoring_player_name):
    if player_name == high_scoring_player_name:
        print("High")
    elif player_name == low_scoring_player_name:
        print("Low")
    else:
        print("neither")

x = check_high_score("Maarten", "Maarten", "Dieter")
print(x)


###


def combat_evaluation(player_power, enemy_defense):
    advantage, disadvantage, evenly_matched = False, False, False

    if player_power > enemy_defense:
        advantage = True
    elif player_power == enemy_defense:
        evenly_matched = True
    else:
        disadvantage = True

    return advantage, disadvantage, evenly_matched

x = combat_evaluation(10,9)
print(x)


###


def sum_of_odd_numbers(end):
    total = 0
    for i in range(1, end, 2):
        total += i
        print(i)
    return total

x = sum_of_odd_numbers(10)
print(x)


###


def regenerate(current_health, max_health, enemy_distance):
    while current_health < max_health and enemy_distance > 3:
        current_health += 1
        enemy_distance -= 2
    return current_health, enemy_distance

x = regenerate(10, 99, 30)
print(x)


###


def award_enchantments(start, end, step):
    counter = 0
    for quest_number in range(start, end, step):
        counter = counter + 1
        
        if counter == 3:
            enchantment_strength = quest_number * 5
            print(
                f"Enchantment of strength {enchantment_strength} awarded for completing {quest_number} quests!"
            )
            counter = 0
        else:
            continue

x = award_enchantments(1,11,1)
print(x)


###


def countdown_to_start():
    for i in range(10,0,-1):
        if i == 1:
            print("1... Fight!")
            break
        else:
            print(F"{i}...")

countdown_to_start()


###


def calculate_experience_points(level):
    total_xp = 0
    for i in range(1,level):
        xp_per_level = i * 5
        total_xp = total_xp + xp_per_level
    print(total_xp)

x = calculate_experience_points(6)
print(x)


###


def meditate(mana, max_mana, num_potions):
    while mana < max_mana and num_potions > 0:
        mana += 1
        num_potions -= 1
    print(f"You have {mana} mana and {num_potions} potions left")

x = meditate(30,99,15)
print(x)


###


inv = [
    "Healing Potion",
    "Leather Scraps",
    "Iron Helmet",
    "Bread",
    "Shortsword",
    ]
def get_last_index(inventory):
    return inventory[len(inventory)-1]

x = get_last_index(inv)
print(x)


###


inventory = ["Leather", "Iron Ore", "Healing Potion"]

def smelt_ore(inventory):
    if inventory[1] == "Iron Ore":
        inventory[1] = "Iron Bar"

    return inventory

smelt_ore(inventory)
print(inventory)


###


def generate_user_list(num_of_users):
    player_ids = []

    for i in range(0, num_of_users):
        player_ids.append(i)

    return player_ids

x = generate_user_list(10)
print(x)


###


def clear_inventory():
    inventory = [
        "Healing Potion",
        "Iron Bar",
        "Kite Shield",
        "Shortsword",
        "Leather Scraps",
        "Tattered Cloth",
    ]

    print(f"inventory: {inventory}")

    # don't touch above this line

    for i in range(0, len(inventory)):
        item = inventory.pop()

        # don't touch below this line
        print(f"Selling: {item}")
        print(f"inventory: {inventory}")


def test():
    clear_inventory()
    print("=====================================")


def main():
    test()


main()


###


items = ["potion", "sword", "Leather scraps", "cape"]

def contains_leather_scraps(items):
    found = False

    # don't touch above this line

    for item in items:
        if item == "Leather scraps":
            print(F"{item} found in inventory")
            found = True
            break
        print(item)

    # don't touch below this line

    return found

contains_leather_scraps(items)


###


def check_character_levels():
    old_character_levels = [1, 42, 43, 53, 12, 3, 32, 34, 54, 32, 43]
    new_character_levels = [1, 42, 45, 54, 12, 3, 32, 38, 54, 32, 42]

    # don't touch above this line

    for i in range(0, len(old_character_levels)):
        if new_character_levels[i] > old_character_levels[i]:
            print(i)
        


# don't touch below this line


def test():
    print("Character level increased at indexes:")
    check_character_levels()
    print("=====================================")


def main():
    test()


main()


###


nums = [100, 10, 22, 107]

def find_max(nums):
    max_so_far = float("-inf")
    for number in nums:
        if len(nums) == 0:
            break
        else:
            max_so_far = max(nums)
    return max_so_far

x = find_max(nums)
print(x)


###


num = [1,2,3,4,5,6,7,8,9,]
def get_odd_numbers(num):
    odd_numbers = []

    for i in range(0, len(num)):
        # don't touch above this line
        if num[i] % 2 != 0:
            odd_numbers.append(num[i])


    # don't touch below this line

    return odd_numbers

x = get_odd_numbers(num)
print(x)


###


champs = ["Thrundar", "Morgate", "Gandolfo", "Thraine", "Norwad", "Gilforn"]

def get_champion_slices(champions):
    value_1 = champions[::2]
    print(champions)
    value_2 = champions[0:-1]
    return value_1, value_2

get_champion_slices(champs)


###


items = [1,2,3]

def get_first_item(items):
    if len(items) > 0:
        return items[0]           
    else:
        return "ERROR"


x = get_first_item(items)
print(x)


###


lijst_1 = [1,2,3]
lijst_2 = ['a', 'b', 'c', 'd']

def reverse_list(lijst_1):
    new_lijst_1 = []
    new_lijst_1 = lijst_1[::-1]
    
    return new_lijst_1

x = reverse_list(lijst_1)
print(x)


###


#filter messages

cases = [
            "well dang it",
            "dang the whole dang thing",
            "kill that knight, dang it",
            "get him!",
            "donkey kong",
            "oh come on, get them",
            "run away from the dang baddies",
        ]

def filter_messages(messages):

    filtered_messages = []
    counts_dang_removed = []

    sentence = " ".join(cases)
    words = sentence.split()

    good_words = []
    dang_words = []
    
    for word in words:
        if word == "dang":
            dang_words.append(word)
        else:
            good_words.append(word)
    
    good_words_string = " ".join(good_words)
    
    filtered_messages.append(good_words_string)

    counts_dang_removed.append(len(dang_words))

    return filtered_messages, counts_dang_removed

x,y = filter_messages(cases)
print(x)
print(y)


###


players = [
            "Harry",
            "Hermione",
            "Ron",
            "Ginny",
            "Fred",
            "Neville",
            "Draco",
            "Luna",
            "Cho",
            "Gregory",
            "Lee",
            "Michael",
            "Lavender",
            "Frank",
            "Anthony",
            "Allan",
        ]


def split_players_into_teams(players):
    team_even = []
    team_odd = []
    for i in range(0,len(players)):
        if i % 2 == 0:
            team_even.append(players[i])
        else:
            team_odd.append(players[i])
    
    return team_even, team_odd

team_a, team_b = split_players_into_teams(players)
print(team_a)
print(team_b)


###


players = [
            "Harry",
            "Hermione",
            "Ron",
            "Ginny",
            "Fred",
            "Neville",
            "Draco",
            "Luna",
            "Cho",
            "Gregory",
            "Lee",
            "Michael",
            "Lavender",
            "Frank",
            "Anthony",
            "Allan",
        ]

def split_players_into_teams(players):
    even_team = players[:len(players):2]
    odd_team = players[1:len(players):2]
    return even_team, odd_team

team_a, team_b = split_players_into_teams(players)
print(team_a)
print(team_b)
print(players)


###

#Alchemy Ingredients
recipe = ["Dragon Scale", "Unicorn Hair", "Phoenix Feather", "Troll Tusk"]
ingredients = ["Dragon Scale", "Phoenix Feather", "Troll Tusk", "Troll Tusk"]

def check_ingredient_match(recipe, ingredients):

    correct_ingredients = []
    ingredients_left = []

    for ingredient in ingredients:
        for item in recipe:
            if ingredient == item and ingredient not in correct_ingredients:
                correct_ingredients.append(ingredient)
            elif item not in ingredients and item not in ingredients_left:
                ingredients_left.append(item)
            else:   
                continue

    percentage = len(correct_ingredients) / len(recipe)           

    return percentage, ingredients_left

percentage, ingredients_left = check_ingredient_match(recipe, ingredients)
print(f"you have {percentage}% of the required ingredients in your bagg.")
print(f"You still need the following ingredients: {ingredients_left}")


###

#Counting Practice dictionaries
enemy_names = [
            "jackal",
            "kobold",
            "jackal",
            "kobold",
            "soldier",
            "kobold",
            "soldier",
            "soldier",
            "jackal",
            "jackal",
            "gremlin",
            "jackal",
            "jackal",
        ]

def count_enemies(enemy_names):
    enemies_dict = {}
    for word in enemy_names:
        enemies_dict[word] = enemies_dict.get(word, 0) + 1

    return enemies_dict

x = count_enemies(enemy_names)
print(x)


###

#Sets
spells = [
            "fireball",
            "eldritch blast",
            "fireball",
            "eldritch blast",
            "chill touch",
            "eldritch blast",
            "chill touch",
            "chill touch",
            "fireball",
            "fireball",
            "shocking grasp",
            "fireball",
            "fireball",
        ]



def remove_duplicates(spells):
    set_spells = set(spells)
    list_unique_spells = list(set_spells)
    return list_unique_spells

unique_spells = remove_duplicates(spells)
print(f"Your have unlocked following spells: {unique_spells}")


```
## Learnning
```python

frameworks: Flask, FastAPI, Django
Kubernetes, Docker, CI/CD pipelines
databases: SQL-, no SQL
tools: GIT
Github
AWS cloud services & Linux
NodeJS
Essensium real time Positioning System for forklifts (EPS)
Spark (PySpark)
SysOps AWS infrastructure
JIRA basedµ
Rest, API, JsonWebsockets, MySQL, Postgres, SQL, AWS stack (S3, EC2, Lambdas, Redshift, Cloudwatch…), Docker, Kubernetes, Git
Spark, NoSQL DBs, Kafka, ML
Slack workflows
SDK's
threading, multi-processing and asynchronous programming
functional and object oriented programming
bus technologies (kafka, rabbit MQ)
relational and non-relational DB (Postgres, Oracle, MongoDb …)
DevOps (Jenkins, OpenShift), docker containers and version control
version control tools, such as Git, Gitlab or SVN
Azure OpenAI
Proof of Concepts (POC's)
windows = macos = linux
Python, MySQL, Airflow, Minio, Apache spark, Open Metadata, Atlassian Bamboo, Docker
Hive, Flink, Kafka, R, AWS en streaming data
