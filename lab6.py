#create a python class, called bank account which represent a bank account having attributes, account number, name, balance
#create a constructor with parameters account number, name, balance
#create a deposit method which manages deposit actions
#create a withdrawl method which manages withdrawl actions
#create a bank fees method to apply the bank fees with a percentage of 5% of the balance account
#create a display method to display account details


class BankAccount:
    def __init__(self, accountNo, name, balance):
        self.accountNo = accountNo
        self.name = name
        self.balance = balance
    
    def deposit(self, depositAmount):
        if depositAmount > 100:
            print("Deposit Amount is too large")
        else:
            self.balance = self.balance + depositAmount

    def withdraw(self, withdrawlAmount):
        if withdrawlAmount > self.balance:
            print("Not enough balance in account")
        else:
            self.balance = self.balance - withdrawlAmount

    def bankFees(self):
        fees = self.balance * (5/100)
        print(f"Your bank fees is {fees}")

    def displayDetails(self):
        print(f"Account Number: {self.accountNo}, Account Name: {self.name}, Account Balance: {self.balance}")


account1 = BankAccount(12, "Chirag", 2500)
account1.deposit(50)
account1.bankFees()
account1.displayDetails()

#ques2

class Employee:
    def __init__(self, employeeID, employeeName, employeeSalary):
        self.employeeID = employeeID
        self.employeeName = employeeName
        self.employeeSalary = employeeSalary

    def calculate_salary(self):
        self.employeeSalary = self.employeeSalary + (self.employeeSalary * 0.2) + (self.employeeSalary * 1.5)

    def display(self):
        print(f"Employee Name: {self.employeeName}, Employee ID: {self.employeeID}, Employee Salary: {self.employeeSalary}")

employee1 = Employee(1, "Chirag", 50000)
employee2 = Employee(2, "Aarav", 500)

#ques3

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.marks = marks
        self.roll_no = roll_no

    def display(self):
        print(f"Student Roll No.: {self.roll_no}, Student Name: {self.name}, Student Marks: {self.marks}")

    def grade(self):
        if self.marks >= 40:
            print("Pass")
        else :
            print("Fail")

student1 = Student(1, "Chirag", 100)
student2 = Student(2, "Aarav", 4)
student3 = Student(3, "Moulik", 3)

