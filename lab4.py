#wap to input 10 integers in a list and print the largest and the smallest number
#wap to input 5 names into a list and print them in sorted order
#wap to reverse a list without using the reverse function
#given a list of marks, wap to find the average of marks and display students whose score is above average
#wap to print all the items of a list using while loop by going thru all the index members

#ques1

# li = []
# for x in range(0,10,1):
#     element = int(input(f"Enter element {x+1}: "))
#     li.append(element)

# smallest = min(li)
# largest = max(li)

# print(f"Smallest number in list: {smallest}")
# print(f"Largest number in list: {largest}")

#ques2

# li = []

# for x in range(0,5,1):
#     element = input(f"Enter {x+1} name: ")
#     li.append(element)

# li.sort()

# print(f"Sorted List: {li}")

#ques3

# li = []
# size = int(input("Enter Size of li"))

# for x in range(0,size,1):
#     element = int(input(f"Enter element {x+1}"))
#     li.append(element)

# reversed_li = []

# for x in range(0,size,1):
#     last_element = li[size-1]
#     li.pop()
#     reversed_li.append(last_element)
#     size = size - 1

# print(f"Reversed List: {reversed_li}")

#ques4

# li = []
# size = int(input("Enter size of list:"))

# sum = 0

# for x in range(0,size,1):
#     element = int(input(f"Enter element {x+1}"))
#     sum = sum + element
#     li.append(element)

# avg = sum / size

# li_aboveavg = []

# for x in li:
#     if x > avg:
#         li_aboveavg.append(x)

# print(f"Students with marks above average: {li_aboveavg}")

#ques5

# li = []
# size = int(input("Enter size of list:"))

# for x in range(0,size,1):
#     element = int(input(f"Enter element {x+1}:"))
#     li.append(element)

# i = 0

# while i < size:
#     print(f"{i+1} element: {li[i]}")
#     i = i+1


#wap to convert a tuple into a list and add a new element
#wap to input a tuple of numbers and print only the prime numbers
#wap to check whether a given element exist in a tuple or not
#wap to swap the value of two variables using a tuple w/o using a temp. variable
#wap to count how many times a particular element appears in a tuple using loop

#ques1

# tup = (1,2,3,4)

# li_tup = list(tup)
# li_tup.append(5)
# tup_li = tuple(li_tup)

# print(tup_li)

#ques2

# li = []
# size = int(input("Enter Size of tuple: "))

# for x in range(0,size,1):
#     element = int(input(f"Enter element {x+1}: "))
#     li.append(element)

# tup = tuple(li)

# for element in tup:
#     count = 0
#     for x in range(1, element+1, 1):
#         if element % x == 0:
#             count = count + 1
#     if count == 2:
#         print(element)




    
