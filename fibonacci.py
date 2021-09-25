
    n = int(input("Enter the Number of values to be printed"))
    a = 0
    b = 1
    s = 0
    count = 1
    print("Fibonacci Series :")
    while(count <= n):
        print(s)
        count += 1
        a = b
        b = s
        s = a+b
