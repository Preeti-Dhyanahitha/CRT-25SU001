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

'''
#write python code to print all the arithmetic operators(+,-,*,/,//,**,%)?
#Important Built-in Math Functions:
print(abs(-54))
print(round(5.478))
print(min([10,20,30,40,54,2]))
print(max([10,20,30,40,54,2]))
print(sum([10,20,30,40,54,2]))
print(pow(2,5))

import math
print(math.sqrt(81))
print(math.ceil(4.2))
print(math.floor(4.2))
print(math.pi)
print(math.factorial(6))

#1. Find the GCD (using math module and Using Euclidean method)
a=int(input("Enter a num"))
b=int(input("Enter a num"))
while b != 0:
    a,b=b, a%b
print(a)

import math
a=int(input("Enter a num"))
b=int(input("Enter a num"))
print(math.gcd(a,b))

#2. Find the LCM
import math
a=int(input("Enter a num"))
b=int(input("Enter a num"))
gcd=math.gcd(a,b)
lcm=(a*b)//gcd
print(lcm)

#3. Write a Python Code to check a num is Perfect number or not
n=int(input("Enter a num"))
sum1=0
for i in range(1, n):
    if n % i ==0:
        sum1 += i
if sum1 ==n:
    print(n,"is a perfect num")
else:
    print(n,"is not a perfect num")