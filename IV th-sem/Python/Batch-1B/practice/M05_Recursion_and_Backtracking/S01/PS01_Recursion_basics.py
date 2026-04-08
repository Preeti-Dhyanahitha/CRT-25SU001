# sum of n natural numbers
#Traditional Approach
def natural_sum(n):
    s = 0
    for i in range(n,0,-1):
        s += i
    return s

print(natural_sum(5))
print(natural_sum(10))

#Recursive Approach
def natural_sum1(n):
    if n == 1:
        return 1
    return n + natural_sum1(n-1)

print(natural_sum1(5))
print(natural_sum1(10))
    
#Factorial of a number
def factorial(n):
    f = 1
    for i in range(n,0,-1):
        f = f * i
    return f

print(factorial(5))
print(factorial(4))

def factorial1(n):
    if n < 0:
        return "Factorial does not exist for -ve"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial1(n-1)
    
print(factorial1(5))
print(factorial1(4))   

#Fibonacci series n th term
# 0 1 1 2 3.....
def fibonacci(n):
    if n <= 0:
        return n
    elif n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(5))

def GCD(a,b):
    while b != 0:
        a,b = b,a%b
    return a

print(GCD(4,10))

def GCD1(a,b):
    if b == 0:
        return a
    else:
        return GCD1(b,a%b)
print(GCD1(4,10))
