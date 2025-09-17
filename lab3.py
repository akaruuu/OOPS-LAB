#ques1 write a program to display the multiplication table of a number entered by the user

num = int(input("Enter a number: "))
i = 1
while i < 10:
    table = num*i
    print(table)
    i = i+1

#ques2 wap to print inverted pyramid of numbers

for i in range(5,0,-1):
    for j in range(5,5-i,-1):
        print(j, end="")
    print("")

#ques3 wap to check if a input no by user is prime or not using loop

num = int(input("enter a number: "))
count = 0

for i in range(1, num+1,1):
    if num%i==0:
        count = count + 1

if count > 2:
    print("number is not a prime")
else:
    print("number is a prime")

#ques4 wap to calculate sum of digits

num = int(input("enter a number: "))
sum = 0
while num != 0:
    last_digit = num%10
    sum = sum + last_digit
    num = num / 10

print(sum)

#ques5 print numbers 1 to 50. if the number is divisble by 3 print "Fizz". if divisible by 5 print "buzz" and if divisble by both print "fizzbuzz"

i = 1
while i <= 50:
    if i%3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    i = i + 1
