# A string is a list of characters in order
# In Python String is immutable

# creating a string
s1 = "hi,"
s2 = "how are you doing?"

print(s1)
print(s2)

# accessing a string using index
print(s1[0])
print(s2[0])

# slice a string
print(s1[0:3])
print(s2[0:3])

# string is immutable, str object does not support item deletion
del s1[3]

# string is immutable, str object does not support item modification
s1[3] = 'a'

# concatenate strings
s = s1 + ' ' + s2
print(s)

# length of a string
print(len(s))

# iterate a string
for i in s1:
    print(i)

for i in s1 + s2:
    print(i)

# assignment : string palindrome : write a program to check whether a given string is palindrome or not?

# program for string reverse
s = "hello world"
reverse_s = ""
for i in s:
    reverse_s = i + reverse_s

print("--------------")
print(reverse_s)
print("--------------")

# reverse a string
s = "hello world"
for i in reversed(s):
    print(i)

print("--------------")

##reverse of string using pop() method
s = "hello world"
s_list = list(s)
i = len(s_list)
while i > 0:
    print(s_list.pop())
    i = i - 1

# convert string to list
s = "hello world"
print(list(s))

# string comparison
s1 = "hello"
s2 = "hello"
if (s1 == s2):
    print("s1==s2")
else:
    print("s1!=s2")

# sort words in a string
s = "hello buddy how are you doing"
words = s.split(" ")
for word in sorted(words):
    print(word)

# string join()
# Create a single string from all the elements in list
greetings = ["Hello", "World", "My Name Is John"]
print(" ".join(greetings))

# string split()
# split() method returns a list of strings after breaking the given string by the specified
separator.

text = 'hello techie world'
# splits at space

print(text.split())

word = 'hello,techie,world'
# splits at ','

print(word.split(', '))

word = 'hello:techie:world'
# splitting at ':'

print(word.split(':'))  