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
