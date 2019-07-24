# regex is to search for a given pattern in a string
# syntax: match = re.search(pat, str)
# In Python regular expression supports various things like Modifiers, Identifiers, and White space characters

#           RegEx Functions
# Function                  Description
# findall	        Returns a list containing all matches
# search	        Returns a Match object if there is a match anywhere in the string
# split             Returns a list where the string has been split at each match
# sub               Replaces one or many matches with a string

# \d matches decimals [0-9]
# \D matches anything other than decimals [0-9]

# all regEx in python of form \x (Includes cases) and \X (Not includes cases) are opposite

import re
my_str = 'Hello world'
m = re.search("(world)", my_str)
if m:
    print(m)
    print(type(m))
    print("search:", m.group())
    print(m.span())

message = '984799287'
match = re.match(r'\d', message)
if match:
    print(match.group())
    print(match)
match = re.match(r'\d+', message)  # Parse more than one digit
if match:
    print(match.group())
    print(match)

listd = ['dog', 'dog group', 'dog dog', 'dodge']
for element in listd:
    m = re.match("(d\w+)\s(d\w+)", element)
    print(m)
    no_spaces = re.match("(d\w+)\S(d\w+)", element)

values ='02873-409-204'
for m in re.finditer('\d+', values):
    print(m.group())

values = "one 22 two-232 56 fffff"
result = re.split('\D', values)
for element in result:
    print(element, end=",")