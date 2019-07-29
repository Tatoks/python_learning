Class:  A


class is a collection of objects which have common properties.A class is a template or blueprint from which objects are created.It is a logical entity.It can't be physical. A class in Python can contain: Fields, Methods & Constructors


Object:  object is one
of
instances
of
the


class . which can perform the functionalities which are defined in the class.An entity that has state and behavior is known as an object e.g.chair, bike, marker, pen, table, car etc.An object can be physical or logical (tangible and intangible).


self:  self
represents
the
instance
of
the


class .  "self" keyword helps to access the attributes and methods of the class in python.


__init__:      "__init__" is a
reserved
method in python
classes.It is known as a
constructor in object
oriented
concepts.This
method
called
when
an
object is created
from the


class .  __init__ method allow the class to initialize the attributes of a class.__init__ method receives parameters and assigns fields to the new class instance.


class bankAccount:
    def __init__(self, custId, custName, acctId, balance, acctType, creditLine):
        self.custName = custName
        self.custId = custId
        self.acctId = acctId
        self.acctType = acctType
        self.balance = balance
        self.creditLine = creditLine

    def deposit(self, depositAmount):
        self.balance += depositAmount
        print(self.balance)

    def withdraw(self, withdrawAmount):
        print("Amount requested for withdrawal:", withdrawAmount)
        if (self.balance + self.creditLine >= withdrawAmount):
            self.balance = self.balance - withdrawAmount
            print("Total Balance After Withdrawal:", self.balance)
        else:
            print(
                "Insufficient funds in your account and it surpassed the credit line limit,please check your account balance")

    def accountStatement(self):
        print("Customer Name:", self.custName)
        print("Customer Id:", self.custId)
        print("Account Id:", self.acctId)
        print("Account Type:", self.acctType)
        print("Account Balance:", self.balance)


# end of class Account

# main program. create different types of accounts saving and checking for customer "Vijay" with cust_id=1234
savingAccount = bankAccount(1234, "John", 23423245678, 100000, "SAVING", 50000)
savingAccount.accountStatement()
savingAccount.withdraw(10000)

checkingAccount = bankAccount(1234, "John", 3695287421, 200000, "CHECKING", 50000)
checkingAccount.accountStatement()
checkingAccount.withdraw(15000)

# we have created two different types of account objects with the same class.
# while creating the saving account object we passed arguments  (1234,"John",23423245678,100000,"SAVING",50000 ) these arguments will pass to #"__init__" method  to initialize the object.
# while creating the checking account object we passed arguments  (1234,"John",3695287421,200000,"CHECKING",50000)these arguments will pass to #"__init__" method  to initialize the object.

# Keyword "self"  represents the instance of the class. It binds the attributes with the given arguments.
# Keyword "self" in class is to access the methods and attributes