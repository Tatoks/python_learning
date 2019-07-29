# Python file object provides basic methods to manipulate files such as open, read, write, append & close methods
# file object = open(file name[, access mode][, buffersize])
# files can be opened in read mode, write mode or append mode

# file read methods
# read()  #return one big string
# readline #return one line at a time
# readlines #returns a list of lines

# file write methods
# write () #used to write a fixed sequence of characters to a file
# writelines()   #writelines to write a list of strings

# file close method
# close() #release all the system resources

# to create a file you have to use open function with any of the mode w, a, w+ and a+
# w write mode (if the file doesn’t exist create it and open it in write mode)
# a append mode (if the file doesn’t exist create it and open it in append mode)
# w+ create a file – if it doesn’t exist and open it in write mode
# a+ create a file – if it doesn’t exist and open it in append mode


import os

dirName = "C:/temp"

# create target directory if don't exist
if not os.path.exists(dirName):
    os.mkdir(dirName)
    print("directory created:", dirName)
else:
    print("directory exists already :", dirName)

fileName = dirName + "/" + "mytext.txt"
file_exists = os.path.isfile(fileName)

f = None
# create file if it does not exist
if file_exists:
    print("file exists already:", fileName)
else:
    # to create a file you have to use open function with any of the mode w, a, w+ and a+
    f = open(fileName, 'w')
    if (f):
        print("file created :", fileName)

# write a fixed sequence of characters to a file
f = None

try:
    f = open("C:/TEMP/mytext.txt", 'w')
    f.write("HELLO WORLD")
except (FileNotFoundError, IOError) as e:
    print(e)
finally:
    if (f):
        f.close()

# to read file as one big string
f = None

try:
    f = open("C:/TEMP/mytext.txt", 'r')
    print(f.read())
except (FileNotFoundError, IOError) as e:
    print(e)
finally:
    if (f):
        f.close()

# to read one line at a time
f = None

try:
    f = open("C:/TEMP/mytext.txt", 'r')
    print(f.readline())
except (FileNotFoundError, IOError) as e:
    print(e)
finally:
    if (f):
        f.close()

# to read line from list of lines
f = None

try:
    f = open("C:/TEMP/mytext.txt", 'r')
    for file in f.readlines():
        print(file)
        # print(type(file))
except (FileNotFoundError, IOError) as e:
    print(e)
finally:
    if (f):
        f.close()

# reading file using for Loop
f = None

try:
    f = open("C:/TEMP/mytext.txt", 'r')
    for line in f:
        print(line)
except (FileNotFoundError, IOError) as e:
    print(e)
finally:
    if (f):
        f.close()

# write a fixed sequence of characters to a file
f = None

try:
    f = open("C:/TEMP/mytext.txt", 'w')
    f.write("HELLO WORLD, HOW ARE YOU DOING?")
except (FileNotFoundError, IOError) as e:
    print(e)
finally:
    if (f):
        f.close()

# write a fixed sequence of characters to a file
f = None

try:
    f = open("C:/TEMP/mytext.txt", 'w')
    f.write("HELLO\n")
    f.write("HOW ARE YOU DOING\n")
except (FileNotFoundError, IOError) as e:
    print(e)
finally:
    if (f):
        f.close()

# writelines can write a list of strings
# w+ #write to file and read file
f = None

try:
    f = open("C:/TEMP/mytext.txt", 'w+')
    fruits = ['Apples\n', 'Bananas\n', 'Oranges\n']
    f.writelines(fruits)
    f.seek(0)
    print(f.read())
except (FileNotFoundError, IOError) as e:
    print(e)
finally:
    if (f):
        f.close()

# append to the file without overwriting it.
f = None

try:
    f = open("C:/TEMP/mytext.txt", "a")
    f.write("Hello World again")
except (FileNotFoundError, IOError) as e:
    print(e)
finally:
    if (f):
        f.close()

# append to the file and then read file
f = None

try:
    f = open("C:/TEMP/mytext.txt", 'a+')
    f.write("\nYou are about to reach in 5 seconds \n")
    f.write("Please follow the queue to exit door \n")
    f.write("Collect your luggage here")
    f.seek(0)
    print(f.read())
except (FileNotFoundError, IOError) as e:
    print(e)
finally:
    if (f):
        f.close()

# pattern search for a given string in file
f = None

try:
    f = open("C:/TEMP/mytext.txt", 'r')
    if 'Apple' in f.read():
        print('Applle found')
except (FileNotFoundError, IOError) as e:
    print(e)
finally:
    if (f):
        f.close()

# work with file objects using with statement
f = None

with open(“testfile.txt”) as f:
    for line in f:
        print line

# binary files
##file wb  access mode opens a file for writing only in binary format.
f = None

try:
    f = open("C:/TEMP/mytext.txt", "wb")
    num = [5, 10, 15, 20, 25]
    arr = bytearray(num)
    f.write(arr)
except (FileNotFoundError, IOError) as e:
    print(e)
finally:
    if (f):
        f.close()

# binary files
# file rb access mode opens a file for reading
f = None

try:
    f = open("C:/TEMP/mytext.txt", "rb")
    num = list(f.read())
    print (num)
    f.close()
except (FileNotFoundError, IOError) as e:
    print(e)
finally:
    if (f):
        f.close()