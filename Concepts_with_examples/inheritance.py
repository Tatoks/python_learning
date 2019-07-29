class bankAccount:

    def __init__(self, acct_id, acct_type, cust_id, cust_name, balance, credit_line):
        self.acct_id = acct_id
        self.acct_type = acct_type
        self.cust_id = cust_id
        self.cust_name = cust_name
        self.balance = balance
        self.credit_line = credit_line

    def deposit(self, amount):
        print("----------------------")
        self.displayAccount()
        print("DEPOSIT TRANSACTION INITIATED FOR AMOUNT : ", amount)
        print("\n")
        self.balance = self.balance + amount
        self.displayAccount()
        print("----------------------")

    def withdraw(self, amount):

        print("----------------------")
        self.displayAccount()
        print("WITHDRAWAL TRANSACTION INITIATED FOR AMOUNT: ", amount)
        print("\n")

        if (self.balance + self.credit_line >= amount):
            self.balance = self.balance - amount
            self.displayAccount()
        else:
            print("insufficient funds")
        print("----------------------")

    def intRateCalc(self):
        pass

    def displayAccount(self):
        print("current acct id:", self.acct_id)
        print("current acct type:", self.acct_type)
        print("current cust id:", self.cust_id)
        print("current cust name:", self.cust_name)
        print("current balance:", self.balance)
        print("current credit line:", self.credit_line)
        print("\n")


# Inheritance ISA relationship
# savingAccount inherits bankAccount
# savingAccount class can have its own methods extending base class functionality
# savingAccount can override parent methods

class savingAccount(bankAccount):

    def __init__(self, acct_id, acct_type, cust_id, cust_name, balance, credit_line):
        # super key word to call parent class constructor
        super().__init__(acct_id, acct_type, cust_id, cust_name, balance, credit_line)

    # method overriding
    def intRateCalc(self):
        pass


# Inheritance ISA relationship
# checkingAccount inherits bankAccount
# checkingAccount can have its own methods extending base class functionality
# checkingAccount can override parent methods

class checkingAccount(bankAccount):

    def __init__(self, acct_id, acct_type, cust_id, cust_name, balance, credit_line):
        # super key word to call parent class constructor
        super().__init__(acct_id, acct_type, cust_id, cust_name, balance, credit_line)

    # method overriding
    def intRateCalc(self):
        pass


# create savingAccount object
sa = savingAccount(5000124, "SAVING", 1244, "SIRI", 500000, 100000)

# create checkingAccount object
ca = checkingAccount(5000126, "CHECKING", 1244, "SIRI", 400000, 50000)

sa.deposit(20000)
ca.deposit(60000)

sa.withdraw(600000)
ca.withdraw(500000)

print(type(sa))
print(type(ca))