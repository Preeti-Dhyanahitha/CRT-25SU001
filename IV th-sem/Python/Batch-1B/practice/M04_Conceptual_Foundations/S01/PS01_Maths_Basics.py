
'''
Math Basics in Python:
1. Basic Arithmetic Operators(+,-,*,/,//,**,%)
2. Important Built-in Math Functions(abs(),round(),min(),max(),sum(),pow())
3. Using the math Module(sqrt(),ceil(),floor(),pi,factorial())

Programs:
1. Find the GCD (using math module and Using Euclidean method)
2. Find the LCM
3. Write a Python Code to check a num is Perfect number or not

Leetcode-->412

#1. Find the GCD
a = int(input())
b = int(input())
#solution-1
import math
print(math.gcd(a,b))
#solution-2
min_val = min(a,b)
gcd = 1
for i in range(1,min_val+1):
    if a % i == 0 and b % i == 0:
        gcd = i
print(gcd)
#solution-3
while b !=0 :
    a,b = b,a%b
print(a)

#LCM:
a = int(input())
b = int(input())
x,y = a,b
while y !=0 :
    x,y = y,x%y
gcd = x

lcm = (a*b)//gcd

print(lcm)
'''
#perfect number
n = int(input())
s = 0
for i in range(1,n//2 + 1):
    if n % i == 0:
        s += i
print("perfect number" if n == s else "not perfect number")