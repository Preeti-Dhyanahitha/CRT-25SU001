'''
Arithmetic series:
input : 1   2
output : 1 3 5 7 9 11 13 15 17 19
 
a = int(input())
d = int(input())
for i in range(10):
    print(a + i * d,end=" ")

Geometric series:
a = int(input())
r = int(input())
for i in range(10):
    print(a*(r ** i) ,end=" ")

Fibonacci Series:
n = 5
0 1 1 2 3

n = int(input())
a = 0
b = 1
for i in range(n):
    print(a,end=" ")
    a,b = b,a+b

print()

li = [0,1]
for i in range(2,n):
    li.append(li[i-2] + li[i-1])
print(li)
'''
n = int(input())
if n < 0:
    print("No factorial for -ve")
elif n == 0 or n == 1:
    print(1)
else:
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    print(fact)