'''
print(min([1,2,3,4]))
print(max([1,2,3,4]))
print(sum([1,2,3,4]))
print(abs(12))
print(abs(-10))

import math
#print(dir(math))
print(math.factorial(5))

#GCD of two numbers
a = int(input())
b = int(input())
#Solution-1
min_num = min(a,b)

for i in range(1,min_num+1):
    if a % i == 0 and b % i == 0:
        gcd = i
print(gcd)

#Solution-2
while b != 0:
    a,b = b,a%b
print(a)

#LCM
a = int(input())
b = int(input())
import math
lcm = (a*b)//(math.gcd(a,b))
print(lcm)
'''
def check_perfect_number(n):
    s = 0
    for i in range(1,n//2 + 1):
        if n % i == 0:
            s += i
    return "perfect number" if s == n else "not a perfect number"

print(check_perfect_number(6))