#############################################################
# PYTHON MATH MODULE
import math

# square root(sqrt) function in math module
print(math.sqrt(36))

# pi function contained in math module
print(math.pi)

# Sine of 2 radians
print(math.sin(2))

# Cosine of 0.5 radians
print(math.cos(0.5))

# Tangent of 0.23 radians
print(math.tan(0.23))

# ceiling value
print(math.ceil(5.5667))

# floor value
print(math.floor(6.879))

# power function
print(math.pow(2, 4))

# factorial(5)=1 * 2 * 3 * 4 *5 = 120
print(math.factorial(5))

# logarithm of a given number
print(math.log(10))

# base-10 logarithm of a given number
print(math.log10(10))

#############################################################
# PYTHON RANDOM MODULE
import random

# generate random integer between specified integers
print(random.randint(0, 10))

# generate random floating point number between 0.0 and 1.0
print(random.random())

# generate random number between 0 and 5
print(random.random() * 5)

num_list = [2, 3.5, "hello world", [12, 36]]

# choose random element from the list
print(random.choice(num_list))

# randomly shuffle the list
random.shuffle(num_list)
print(num_list)

# randomly selected element from the range created by the start, stop and step arguments.
# The value of start is 0 by default. Similarly, the value of step is 1 by default.
print(random.randrange(1, 10))
print(random.randrange(1, 10, 2))

#############################################################
# PYTHON DATE AND TIME MODULES
import datetime

# get current date and time
currentTime = datetime.datetime.now()
print(currentTime)

# get current date in YYYY-MM-DD format
today = datetime.date.today()
print(today)

# get current date in format DD-MM-YYYY
today = datetime.date.today().strftime("%d-%m-%Y")
print(today)

# get current time
currentTime = datetime.datetime.now().time()
print(currentTime)

# get date from timestamp
from datetime import date

timestamp = date.fromtimestamp(1326244364)
print("Date =", timestamp)

# get current(today) month, day and year
from datetime import date

# date object of today's date
today = date.today()
print("Current year:", today.year)
print("Current month:", today.month)

# python date time object
from datetime import datetime

# datetime(year, month, day)
a = datetime(2018, 11, 28)
print(a)

# time object to represent time

from datetime import time

# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)

# time(hour, minute and second)
b = time(11, 34, 56)
print("b =", b)

# time(hour, minute and second)
c = time(hour=11, minute=34, second=56)
print("c =", c)

# time(hour, minute, second, microsecond)
d = time(11, 34, 56, 234566)
print("d =", d)

# datetime(year, month, day, hour, minute, second, microsecond)
b = datetime(2017, 11, 28, 23, 55, 59, 342380)
print(b)
print("Current day:", today.day)

# datetime.timedelta
# A timedelta object represents the difference between two dates or times.
# Difference between two dates and times

from datetime import datetime, date

t1 = date(year=2018, month=7, day=12)
t2 = date(year=2017, month=12, day=23)
t3 = t1 - t2
print("t3 =", t3)

t4 = datetime(year=2018, month=7, day=12, hour=7, minute=9, second=33)
t5 = datetime(year=2019, month=6, day=10, hour=5, minute=55, second=13)
t6 = t4 - t5
print("t6 =", t6)

print("type of t3 =", type(t3))
print("type of t6 =", type(t6))
#############################################################