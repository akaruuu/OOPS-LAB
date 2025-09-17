#a school maintain student grades in three subjects. write a function that return the average marks. show how default parameters could be use if a student has missed the test. assume missing marks = 0
#a cafe allow customer to order multiple items. write a function totalBill (* items) where each item is given as a tuple (name, price). this function should return the total total bill
#in an e-commerce system applyDiscount(price, discount) is frequently used. management asked to reduce repeatitive function definition
#write a function which calculate area. if both length and breadth are provided return rectangle area, if only length is provided return square area
#write a function bonus(salary, rate = 0.10) that calculates the new salary after applying the bonus rate. call the function once using positional arguments and once using keyboard argument. show a case where incorrect mixing of positional and keyboard arguments showing a error
#design a function studentRecord(course, *subjects, **details) that stores the course name, store multiple subjects using star argument, store detail like name age grade using keyword arguments. write a program that demonstrates all three cases in one function call


#ques1

# def avgMarks(marks1 = 0, marks2 = 0, marks3 = 0):
#     markSum = marks1 + marks2 + marks3
#     avg = markSum / 3
#     return avg

# subject1 = int(input("Input marks for first subject: "))
# subject2 = int(input("Input marks for second subject: "))
# subject3 = int(input("Input marks for third subject: "))

# average_marks = avgMarks(subject1, subject2, subject3)
# print(f"Average marks: {average_marks}")

#ques2

# def totalBill(*items):
#     total = 0
#     for item in items:
#         total = total + item[1]
#     return total

# n = int(input("Enter number of items: "))

# items_list = []

# for i in range(n):
#     name_price = input("Enter name and price of the item seperated by a space: ")
#     item_name = name_price.split()[0]
#     item_price = float(name_price.split()[1])
#     items_list.append((item_name, item_price))

# items = tuple(items_list)

# total = totalBill(*items)
# print(f"Total Bill: {total}")

#ques3 

# applyDiscount = lambda price, discount : price * (1 - discount)

# print(applyDiscount(100, 0.1))

#ques4

# def area(length, breadth = 0):
#     if breadth == 0:
#         return length*length
#     else:
#         return length*breadth
    
# square_area = area(2)
# rect_area = area(2,4)

# print(square_area)
# print(rect_area)

#ques5

# def bonus(salary, rate = 0.10):
#     return salary + (salary * rate)

# salary1 = bonus(5000, 0.2)
# print(f"Called using positional arguments: {salary1}")

# salary2 = bonus(salary = 5000, rate = 0.2)
# print(f"Called using keyword arguments: {salary2}")

# salary3 = bonus(salary = 5000, 0.3) #mixing will produce error

#ques6

def studentRecord(course, *subjects, **details):
    # print(f"Course: {course}")

    # print("Subjects: ")
    # for subject in subjects:
    #     print(subject)

    # print("Details: ")
    # for key,value in details.items():
    #     print(f"{key} : {value}")

    record = {
        'course' : course,
        'subjects' : list(subjects),
        'details' : {
            'name' : details['name'],
            'age' : details['age'],
            'grade' : details['grade']
        }    
    }
    return record


student_record = studentRecord(
    "CSE",
    "STATS", "DSA", "OOPS",
    name = "chirag", age = 20, grade = "A"
)

print(student_record)





