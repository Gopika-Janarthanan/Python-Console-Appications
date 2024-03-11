class Bank_Account:
    def __init__(self, name, savings, account_number, branch_name):
        self.name = name
        self.savings = savings
        self.account_number = account_number
        self.branch_name = branch_name

    def deposit(self, deposited_amount):
        if deposited_amount == 0:
            print("You have to deposit money")
        else:
            print("Your previous savings :",self.savings)
            print("You deposited {} Rupees".format(deposited_amount))
            self.savings = self.savings + deposited_amount
            print("Your current savings {}".format(self.savings))

    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.savings:
            print("Insufficient savings")
        elif withdraw_amount == 300:
            print("You've only minimum savings")
        elif withdraw_amount < self.savings:
            self.savings = self.savings - withdraw_amount
            print("Your withdrew amont {}".format(withdraw_amount))
            print("Your current savings {} rupees".format(self.savings))

    def display_balance(self, current_savings):
        print("Your Account details ")
        print("Name : ",self.name)
        print("BranchName:", self.branch_name)
        print("Account Number:", self.account_number)
        print("Savings:", self.savings)

a1 = Bank_Account("Gopika J", 0, 12345, "GRpet")
a1.deposit(500)
a1.withdraw(250)
a1.display_balance(0)

---------------------------------------------------------------------------
Output:

Your previous savings : 0
You deposited 500 Rupees
Your current savings 500
Your withdrew amont 250
Your current savings 250 rupees
Your Account details 
Name :  Gopika J
BranchName: GRpet
Account Number: 12345
Savings: 250
