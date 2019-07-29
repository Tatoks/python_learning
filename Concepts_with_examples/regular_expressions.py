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



#regex or regular expression is to search for a given pattern in a string
#import re
#syntax: match = re.search(pat, str)
#re.search() method returns an match object

#regular expression methods?
#re.findall() method returns a list containing all matches
#re.search() method returns a Match object if there is a match anywhere in the string
#re.split() method returns a list where the string has been split at each match
#re.sub() method replaces one or many matches with a string

#re.search() Vs re.match()
#re.search() ⇒ find something anywhere in the string and return a match object.
#re.match() ⇒ find something at the beginning of the string and return a match object.

#A special sequence is a \ followed by one of the characters in the list below:
#A Returns a match if the specified characters are at the beginning of the string
"\AThe"
#\b Returns a match where the specified characters are at the beginning or at the end of a word
r"\bain"
#\B Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
r"\Bain"
#\d Returns a match where the string contains digits (numbers from 0-9)
"\d"
#\D Returns a match where the string DOES NOT contain digits
"\D"
#\s Returns a match where the string contains a white space character
"\s"
#\S Returns a match where the string DOES NOT contain a white space character
"\S"
#\w Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
"\w"
#\W Returns a match where the string DOES NOT contain any word characters
"\W"
#\Z Returns a match if the specified characters are at the end of the string
"Spain\Z"

import re
my_str='hello world'

#search for "world" in "hello world"
m=re.search("(world)",my_str)
if m:
    #print(m)
    #print(type(m))
    print("search:",m.group())
    print(m.span())

#search for 'oo' in 'google'
match=re.search(r'oo','google')
print(match.group())

#search for digits in string
match=re.search(r'\d\d\d','p123g')
print(match.group())

#search for email address in a given string
str='purple aliceinwonderland@google.com '
match=re.search(r'\w+@\w+\.(\w+)',str)
if match:
    print(match.group())

#re.match() ⇒ find something at the beginning of the string and return a match object.
m = re.match(r"(?P<int>\w+)\.(\d*)", '3.143')
print(m.group())

#re.match() ⇒ find something at the beginning of the string and return a match object.
#re.match for "world" in "hello world"
my_str='hello world'
m=re.match("(world)",my_str)
if m:
    print(m)
    print(type(m))
    print("search:",m.group())
    print(m.span())

#re.match() if string starts in digit
message='22466678'
match=re.match(r'^\d+',message)
if match:
    print(match.group())

# re.match() if two words starting with letter d.
list=['dog dot','do dont','dumb-dumb','no match','dumb-kitty']
for element in list:
    m=re.match("(d\w+)\W(d\w+)",element)
    if m:
        print(m.group())

#re.findall() returns a list containing all matches.
str='The rain started pouring'
x=re.findall('ai',str)
print(x)

#re.findall() returns a list containing all matches.
str='The rain started pouring in india'
x=re.findall('india',str)
print(x)

#re.split() returns a list where the string has been split at each match:
value='one 12 two 22 three 333'
result=re.split('\D+',value)
for element in result:
    print(element)