import re

pattern = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
password = input("Enter string to test: ")
result = re.findall(pattern, password)
if result:
    print("Valid password")
else:
    print("Password not valid")
