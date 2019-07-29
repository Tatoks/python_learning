# Class or static variables are shared by all objects. Instance or non-static variables are different for different objects (every object has a copy of it).
# In C++ and Java, static keyword helps to make a variable as class variable. The variables which don’t have preceding static keyword are instance variables.
# The Python doesn’t require a static keyword. All variables which are assigned a value in class declaration are class variables.
# And variables which are assigned values inside class methods are instance variables.

class BankAccount:
    # class(static) variable
    bankName = "ABC INTERNATIONAL BANK"

    def __init__(self, acct_id, acct_type, cust_id, cust_name, amount, credit_line):

        # instance variables
        self.acct_id = acct_id
        self.acct_type = acct_type
        self.cust_id = cust_id
        self.cust_name = cust_name
        self.amount = amount
        self.credit_line = credit_line

    def displayAccount(self):
        print("----------------------------------------------------------------")
        print(self.acct_id, self.acct_type, self.cust_id, self.cust_name, self.amount, self.credit_line)

    def deposit(self, amount):
        self.amount = self.amount + amount

    def withdraw(self, amount):
        if (self.amount + self.credit_line >= amount):
            self.amount = self.amount - amount
            self.displayAccount()
        else:
            print("insufficient funds")

    def intRateCalc(self):
        pass


class SavingAccount(BankAccount):

    def __init__(self, acct_id, acct_type, cust_id, cust_name, amount, credit_line):
        BankAccount.__init__(self, acct_id, acct_type, cust_id, cust_name, amount, credit_line)

    def intRateCalc(self):
        pass


class CheckingAccount(BankAccount):

    def __init__(self, acct_id, acct_type, cust_id, cust_name, amount, credit_line):
        BankAccount.__init__(self, acct_id, acct_type, cust_id, cust_name, amount, credit_line)

    def intRateCalc(self):
        pass


sa = SavingAccount(5000124, "SAVING", 1244, "SIRI", 5000000, 100000)
ca = CheckingAccount(5000126, "CHECKING", 1244, "SIRI", 4000000, 50000)

print("---------------------")
print(BankAccount.bankName)
print(sa.bankName)
print(ca.bankName)

# In Python a class(static) variable cannot be changed using an instance
# in this case it creates a new instance variable in the saving account object
sa.bankName = "XYZ INTERNATIONAL BANK"
print("---------------------")
print(sa.bankName)
print(BankAccount.bankName)

# In Python a class(static) variable can be changed only using the class name
BankAccount.bankName = "XYZ INTERNATIONAL BANK"
print("---------------------")
print(BankAccount.bankName)
print(ca.bankName)
print(sa.bankName)
print("---------------------")