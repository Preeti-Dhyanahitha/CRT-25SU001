'''1. Square Star Pattern
n=4
Output:
* * * *
* * * *
* * * *
* * * *

n = int(input())
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()

2. Right Angle Triangle
n=4
Output:
*
* *
* * *
* * * *

n = int(input())
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()

3. Inverted Triangle
n=4
Output:
* * * *
* * *
* *
*
'''
n = int(input())
for i in range(n):
    for j in range(n-i,0,-1):
        print("*",end=" ")
    print()

'''
4. Number Triangle
n=4
Output:
1
1 2
1 2 3
1 2 3 4

5. Repeated Number Pattern
n=4
Output:
1
2 2
3 3 3
4 4 4 4

6. Alphabet Triangle
n=4
Output:
A
A B
A B C
A B C D


7. Floyd Triangle
n=4
Output:
1
2 3
4 5 6
7 8 9 10

8. Hollow Square
n=4
Output:
* * * *
*     *
*     *
* * * *
'''
