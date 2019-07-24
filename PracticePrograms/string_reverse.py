# Without recursion
def reverse(greetings):
    rev = ''
    for i in greetings:
        rev = i + rev
    return rev
    # end of function reverse


# Reverse String using Recursion
def rev_string(mystring):
    if len(mystring) == 0:
        return mystring
    else:
        return rev_string(mystring[1::]) + mystring[0]


print('Hello')
print(rev_string('Hello'))
print(reverse('Hello'))

print('---------------------------------------------')

string = "Hello"
# Print string in normal order
for i in range(len(string)):
    print(string[i], end="")

print()

# Print string in reverse order using for loop
for i in range(1, len(string) + 1):
    print(string[-i], end="")
print()

# for loop using index
rev = ""
for i in string:
    rev = rev + i
print(rev)

# Reverse using simple for loop using index and temp var
rev = ""
for i in string:
    rev = i + rev
print(rev)

# Pythonic code to reverse a string
print(string[::-1])
