'''
input : 4
output:
* * * *
* * * *
* * * *
* * * *

n = int(input())
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()


n = int(input())
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()


n = 4
output : 
* * * *
* * *
* *
*

n = int(input())
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

print("------------------")

for i in range(n):
    for j in range(n-i,0,-1):
        print("*",end=" ")
    print()

n = 4
output :
1 
2 3
4 5 6
7 8 9 10

k = 1
n = int(input())
for i in range(1,n+1):
    for j in range(i):
        print(k,end=" ")
        k += 1
    print()

n = 4
output:
A
A B
A B C
A B C D

print(ord('A'))
print(chr(65))
'''
n = int(input())
for i in range(n):
    for j in range(i+1):
        print(chr(65+j),end=" ")
    print()

print("----------------------------")
n = int(input())
k = 65
for i in range(n):
    for j in range(i+1):
        print(chr(k),end=" ")
        k += 1
    print()