'''
Recursion
Recursion is when a function calls itself.

Base Case and Recursive Case
Every recursive function must have two parts:
1. A base case - A condition that stops the recursion
2. A recursive case - The function calling itself with a modified argument
Without a base case, the function would call itself forever, causing a stack overflow error.
'''
#Sum of N natural numbers
def Natural_sum(n):
    s = 0
    for i in range(n,0,-1):
        s += i
    return s

print(Natural_sum(5))
print(Natural_sum(10))

def Natural_sum1(n):
    if n == 1:
        return 1
    else:
        return n + Natural_sum1(n-1)
    
print(Natural_sum1(5))
print(Natural_sum1(10))

#Factorial of a number
def Factorial(n):
    f = 1
    for i in range(n,0,-1):
        f *= i
    return f

print(Factorial(5))
print(Factorial(7))

def Factorial1(n):
    if n < 0:
        return "Factorial does not exist for -ve numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * Factorial1(n-1)
    
print(Factorial1(5))
print(Factorial1(7))

