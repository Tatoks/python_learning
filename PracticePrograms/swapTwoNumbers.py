print("---------Continue---------")
# without temp variable
i=10
j=11
print(i,j)
i=i+j
j=i-j
i =i-j
print(i,j)

print("---------Continue---------")
# with temp variable
i=10
j=11
print(i,j)
temp = j
j = i
i = temp
print(i,j)

print("---------Continue---------")
# With Python, optimized code
i=10
j=11
print(i,j)
i,j = j, i
print(i, j)
