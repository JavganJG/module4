def factorial(num):
    factorial = 1
    for x in range(1,num+1):
        factorial= factorial * x
    return factorial

num = int(input("Factorial of: "))
print(factorial(num))



