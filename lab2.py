#ques1 compute distance between wto points taking input from user

import math
x1 = int(input("Enter x coordinate for first point: "))
x2 = int(input("Enter x coordinate for second point: "))
y1 = int(input("Enter y coordinate for first point: "))
y2 = int(input("Enter y coordinate for second point: "))
distance = math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))
print("Distanc betweem the two points: ", distance)

#ques2 take two numbers as command line args and print its sum

import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
print("sum is: ", a+b)

#ques3 reverse a string entered by user

str = input("Enter a string: ")
rev_str = str[::-1]

print("Reversed string: ", rev_str)

#ques4 count number of vowels in a string

str = input("enter a string: ")
vowels = 0

for char in str:
    if char == a or char == e or char == i or char == o or char == u:
        vowels= vowels + 1

print("no. of vowels in string entered: ", vowels)

#ques5 check if string is palindrome

str = input("enter string")
rev = str[::-1]

if str == rev:
    print("the string is a palindrome")
else:
    print("the string is not a palindrome"
    )

#ques6 replace all spaces in a sentence with python

str = input("enter a string: ")
result = str.replace("","-")
print("after replacement: ", result)

#ques7 convert the first letter of each word to uppercase

str = input("enter a string: ")
res = str.title()
print(str)