#ques1 wap to check the type of the variables

a = 12
print(type(a))
b = 3.14
print(type(b))
c = True
print(type(c))
d = "hello"
print(type(d))

#ques2 wap to add two int numbers, a int and a float, and two string

int1 = 2
int2 = 4
print(int1 + int2)
float1 = 3.14
print(int1+ float1)
string1 = "hello"
string2 = "world"
print(string1 + string2)

#ques3 wap to swap two numbers without using a third variable

num1 = 2
num2 = 10
print(f"before swapping: {num1} and {num2}")
a = a+b
b = a-b
a = a-b
print(f"after swapping: {num1} and {num2}")

#ques4 wap to define diff ways of defining varriable names

swap = 1
Swap = 2
SWAP = 3
print("swap is equal to ", swap)
print("Swap is equal to ", Swap)
print("SWAP is equal to ", SWAP)

#ques5 wap to perform all basic arithmetic operations

a = 10
b = 2
print("result of addition: ", a+b)
print("result of subtraction: ", a-b)
print("result of multiplication: ", a*b)
print("result of division: ", a/b)
print("result of modulo: ", a%b)

#ques6 wap to calc area and circumference of a circle

radius = int(input("Enter radius of the circle"))
pi = 3.14

area = pi*radius*radius
circumference = 2*pi*radius

print(f"Area and circumference respectively: {area} and {circumference}")