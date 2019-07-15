# Dynamic Type Casting

print('--------Dynamic type casting----------')
i=100
j='Hello World'
print(j)
print(type(j))
j=99.5
print(j)
print(type(j))
j=i
print(j)
print(type(j))


# Static type casting
print('-----------Static Type Conversions--------')

num=100
dec=5.6
word='Hello'
print(num, dec, word)
print(type(num), type(dec), type(word))
dec = int(333.33)
word = float(22)
num = str('example')
print(type(num), type(dec), type(word))
print(num, dec, word)
