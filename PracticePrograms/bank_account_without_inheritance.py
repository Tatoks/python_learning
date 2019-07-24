# Without inheritance

class BankAccount:

    def __init__(self, custId, custName, custPhone, custEmail, accType, accBal, accNumber):
        self.id = custId
        self.name = custName
        self.phone = custPhone
        self.email = custEmail
        self.accType = accType
        self.bal = accBal
        self.accNum = accNumber

    def balanceEnquiry(self):
        print("Customer Id: ", self.id)
        print("Customer name: ", self.name)
        print("Customer phone: ", self.phone)
        print("Customer email: ", self.email)
        print("Customer accType: ", self.accType)
        print("Customer bal: ", self.bal)
        print("Customer accNum: ", self.accNum)

    def deposit(self, amount):
        self.bal = self.bal + amount
        print("New updated balance is:", self.bal)

    def withdraw(self, amount):
        if self.bal > amount:
            self.bal = self.bal - amount;
            print("Updated balance amount is: ", self.bal)
        else:
            print('Insufficient Balance:', self.bal)

    def savingsAccount(bankAccount):
        print("Rate of interest : 6.8%")
        print("Daily deposit amount limit: 100000/-")
        print("Daily withdrawal amount limit: 20000/-")
        print("Minimum balance: 3000/-")

    def currentAccount(bankAccount):
        print("Rate of interest : 0.0%")
        print("Daily deposit amount limit: No Limit")
        print("Daily withdrawal amount limit: No Limit")
        print("Minimum balance: 100000/-")


# custId, custName, custPhone, custEmail, accType, accBal, accNumber
cust1 = BankAccount(1001, 'Abhilash', 920930929, 'abhi@inno,com', 'saving', 10000, 13898298398)
cust1 = BankAccount(1002, 'Sanne', 920930928, 'san@inno,com', 'current', 10000, 13898298398)

cust1.balanceEnquiry()
cust1.currentAccount()
