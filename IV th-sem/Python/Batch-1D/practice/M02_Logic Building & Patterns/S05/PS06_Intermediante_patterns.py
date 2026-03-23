'''Intermediante patterns
1. Pyramid
n = 4
Output:
   *
  * *
 * * *
* * * *

2. Inverted Pyramid
n=4
Output:
* * * *
 * * *
  * *
   *

3. Diamond
n=4
Output:
   *
  * *
 * * *
* * * *
 * * *
  * *
   *
4. Number Pyramid
n=4
Output:
   1
  1 2
 1 2 3
1 2 3 4

5. Palindrome Pattern
n=4
Output:
1
212
32123
4321234

6. Reverse Number Triangle
n=4
Output:
1 2 3 4
1 2 3
1 2
1

7. Binary Triangle
n=4
Output:
1
0 1
1 0 1
0 1 0 1

8. Cross Pattern
n=5
Output:
*       *
  *   *
    *
  *   *
*       *

9. Hollow Diamond
n=4
Output:
   *
  * *
 *   *
*     *
 *   *
  * *
   *

10. Hollow Pyramid
n=4
Output:
   *
  * *
 *   *
*******

li = [1,2,3,4,5]
#output : [1,4,9,16,25]
res = []
for i in li:
    res.append(i ** 2)
print(res)

ans = [i**2 for i in li]
print(ans)

li = [1,2,3,4,5]
res = []
for i in li:
    if i % 2 == 0:
        res.append(i)
print(res)

print([i for i in li if i % 2 == 0])

li = ['a','b','c']
#'a b c'
res = ""
for ch in li:
    res = res + ch +" "
print(res)

print(" ".join(li))

1. Pyramid
n = 4
Output:
   *
  * *
 * * *
* * * *

n = int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)


3. Diamond
n=4
Output:
   *
  * *
 * * *
* * * *
 * * *
  * *
   *

n = int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
for i in range(n-1,0,-1):
    print(" "*(n-i)+"* "*i)

n = 4
output:
   1
  1 2
 1 2 3
1 2 3 4

n = int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(1,i+1):
        print(k,end=" ")
    print()

#n = int(input())
for i in range(1,n+1):
        print(" "*(n-i)+" ".join([str(k) for k in range(1,i+1)]))
    
n = 4
output:
   1
  2 2
 3 3 3
4 4 4 4
'''
n = int(input())
for i in range(1,n+1):
        print(" "*(n-i)+" ".join([str(i) for k in range(1,i+1)]))
 