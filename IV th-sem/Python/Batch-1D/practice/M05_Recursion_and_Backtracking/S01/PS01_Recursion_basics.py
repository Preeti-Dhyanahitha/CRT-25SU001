#sum of n natural numbers
#Traditional Approach
def sum_of_N(n):
    s = 0
    for i in range(n,0,-1):
        s += i
    return s

print(sum_of_N(5))#15
print(sum_of_N(10))#55

#Recursive Approach
def sum_of_N1(n):
    if n == 0:
        return 0
    return n + sum_of_N1(n-1)

print(sum_of_N1(5))#15
print(sum_of_N1(10))#55

#Factorial of a number
def Factorial(n):
    if n < 0:
        return "no factorial -ves"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * Factorial(n-1)

print(Factorial(5))#120
print(Factorial(3))#6