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

#Fibonacci series ==> 0,1,1,2,3,5,8,...
def Fibonacci(n):
    if n <= 0:
        return n
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

print(Fibonacci(5))#3
print(Fibonacci(7))#8

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