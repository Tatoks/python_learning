i = 10
j = 20

k = j + 1  # k is assigned the value of j

# c += a is equivalent to c = c + a
m = 5
m += j
print('Add AND ', m)

# c -= a is equivalent to c = c - a
m = 5
m -= j
print('Subtract AND ', m)

# c *= a is equivalent to c = c * a
m = 5
m *= j
print('Multiply AND ', m)

# c /= a is equivalent to c = c / a.  c /= a is equivalent to c = c / a
m = 5
m /= j
print('Divide AND ', m)

# c %= a is equivalent to c = c % a
m = 5
m %= j
print('Modulus AND ', m)

# c **= a is equivalent to c = c ** a
m = 5
m **= j
print('Exponent AND ', m)

# c //= a is equivalent to c = c // a
m = 5
m //= j
print('Floor Division AND ', m)
