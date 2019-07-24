import os

# File path handling

os.chdir("C:/Users")  # Changes the current folder
print(os.path.dirname("C:/Users")) # returns the path's directory name
print(os.path.split("C:/Users/asanne")) # returns tuple
print(os.path.join("foo", "panda")) # returns concatenated path
calc = "C:\\Windows\\System32\\calc.exe" # path to windows calculator
print(os.path.sep)  # Returns the separating slash symbol for current OS
print(calc.split(os.path.sep))

# Read and write 