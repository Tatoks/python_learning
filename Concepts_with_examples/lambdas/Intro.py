#A lambda in Python is a single expression anonymous function often used as inline function.
#A lambda form #in python does not have statements as it is used to make new function object and then return them at run time.

i=8
j=4

#function to add two variables
def add(x,y):
    return x+y
result=add(i,j)
print(result)

#function to multiply two variables
def mult(x,y):
    return x*y
result=mult(i,j)
print(result)

#function to divide two variables
def div(x,y):
    return x/y
result=div(i,j)
print(result)


#lambda function to add two variables
add_l=lambda x,y: y+x
result =add_l(i,j)
print("lambda function to add ",i,"and", j, "result:",result)

#lambda function to multiply two variables
mult_l=lambda x,y: x*y
result =mult_l(i,j)
print("lambda function to multiply ",i,"and",j, "result:",result)

#lambda function to concatenate two strings
greetings1="hello"
greetings2="world"

concat_l=lambda x,y: x+" "+y
result=concat_l(greetings1,greetings2)
print("lambda function to concatenate ",greetings1,"and",greetings2,"result:",result)

#function to determine max of two numbers
def max(x,y):
    if x>y:
        return x
    else:
        return y
max(10,20)

#function to determine min of two numbers
def min(x,y):
    if x<y:
        return x
    else:
        return y
min(10,20)

#lambda function to determine min of two numbers
i=2
j=3
min = lambda x,y: x if x < y else y
res=min(i,j)
print("lambda function for min of ",i,"and",j, "result:", res)

#lambda function to determine max of two numbers
max = lambda x,y: x if x > y else y
res=max(i,j)
print("lambda function for max of ",i,"and",j, "result:", res)

#LAMBDA FUNCTIONS : MAP, REDUCE AND FILTER. WHEN TO USE WHAT ?
#The rule of thumb you use to determine which method you should use is as follows:
#If you already have a list of values and you want to do the exact same operation on each of the elements in the array and return the same amount of
#items in the list, in these type of situations it is better to use the map method. If you already have list of values but you only want to have items in the
#array that match certain criteria, in these type of situations it is better to use # filter method. If you already have list of values, but you want to use
#the values in that list to create something completely new, in these type of situations it is better to use the reduce method.

#map() function takes in lambda function and a list.
#program with map function : a new list is returned which contains all the lambda modified items
my_list=[1,2,3,4,5,6]
new_list=list(map(lambda x: (x**2),my_list))
print("lambda map function :",my_list, "square of elements :",new_list)

#filter out all the elements of a sequence
#Program to filter out only the even items from a list
my_list=[1,2,3,4,5,6]
new_list=list(filter(lambda x: (x%2==0),my_list))
print("lambda filter function :",my_list,"filter to return even elements :" ,new_list)

#reduce() function takes in a function and a list as argument.
#new reduced result is returned
from functools import reduce
my_list=[1,2,3,4]
sum=reduce((lambda x,y :x+y),my_list)
print("lambda reduce function :",my_list,"sum of elements :",sum)

#reduce() function takes in a function and a list as argument.
#new reduced result is returned
from functools import reduce
my_list=[1,2,3,4]
mul=reduce((lambda x,y :x*y),my_list)
print("lambda reduce function :",my_list,"multiply all elements :",mul)