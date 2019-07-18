import os

# os.makedirs('D:/pythonProgramCreatedDirectory')  # In case you want to create directory

f = open('D:/TestDigitalAssets/sample.txt', 'w')  # File opened in write mode
# if specified file does not exist, then it creates a new file
print("Write using 'w' mode:")
f.write('This is a test file')
f.write('\nThis is a new line')
f.close()  # Opened in write mode 'w', you cannot read

# READ file contents - Entire file is fetched
f = open('D:/TestDigitalAssets/sample.txt', 'r')  # File opened in read mode
print('--------------READ ENTIRE FILE AND PRINT-------------')
print(f.read())
f.close()

# READLINE - read one line at a time
f = open('D:/TestDigitalAssets/sample.txt', 'r')  # File opened in read mode
print('--------------READ LINE BY LINE-------------')
for line in f.readlines():
    # read lines one by one as a list instead of whole file
    print('Line: ', line, end="")
f.close()
print()
# you can read + write when file opened in w+ mode
# w+ -> creates a file if it does not exits
print("--------------WRITE + READ in 'w+' MODE----------------")
f = open('D:/TestDigitalAssets/sample1.txt', 'w+')
print("Write using 'w' mode:")
f.write('This is READ and WRITE mode')
print(f.read())
f.close()

# APPEND mode, to add lines to existing file contents at end
print("--------------APPEND FILE in 'a' MODE----------")
f = open('D:/TestDigitalAssets/sample.txt', 'a')
f.write('\nAPPEND')
f.close()
f = open('D:/TestDigitalAssets/sample.txt', 'r')
print(f.read())
f.close()

print("--------------APPEND FILE in 'a+' MODE----------")
# APPEND+ mode, to add lines to existing file contents at end and read
f = open('D:/TestDigitalAssets/sample.txt', 'a+')
f.write('\nAPPEND+')
f.seek(0)  # go to begining of file, the current pointer will be at EOF
print('\nAPPEND using A+:', f.read())
f.close()


# Write and read binary mode
print("-----------WRITE BINARY 'wb' MODE---------")
f = open('D:/TestDigitalAssets/binary.txt', 'wb')
num = [5,10]
arr = bytearray(num)
print('Writing binary text: ', arr)
f.write(arr)
f.close()
print("-----------READ BINARY 'rb' MODE---------")
f = open('D:/TestDigitalAssets/binary.txt', 'rb')
num = list(f.read())
print(num)
f.close()