'''
n = int(input())
count = 0
for i in range(1,n+1):
    if n % i == 0:
        count += 1
        print(i,end=" ")
print(count)

n = int(input())
if n >= 0:
    print(int(str(n)[::-1]))
else:
    n = -1 * n
    print(-1 * int(str(n)[::-1]))

n = int(input())
if n < 0:
    n = -1 * n
print(-1 * int(str(n)[::-1]))
'''
#Check whether the given number is prime or not