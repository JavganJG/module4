def factorial_rec(num):
    if num == 1:
        return 1
    return num*factorial_rec(num-1)
    


num = int(input("Factorial of: "))
print(factorial_rec(num))


