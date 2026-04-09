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