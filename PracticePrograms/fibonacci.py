def print_fibonacci(n):
    if n == 1:
        print(0, end = " ")
    elif n == 2:
        print(0,1, end = "")
    else:
        print(0,1, end=" ")
        a = 0
        b = 1
        while n > 2:
            print(a+b, end = " ")
            a, b = b, a+ b
            n = n -1
        return 0


for i in range(1, 20):
    print_fibonacci(i)
    print()