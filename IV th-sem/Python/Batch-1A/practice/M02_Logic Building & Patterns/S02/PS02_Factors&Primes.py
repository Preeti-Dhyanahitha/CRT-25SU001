'''Print all the factors of a given number
input : 12
output : 1 2 3 4 6 12
n = int(input("Enter a number: "))
for i in range(1,n//2+1):
    if n % i == 0:
        print(i,end=" ")
print(n)

Count the factors of a given number
input : 12  
output : 6

n = int(input("Enter a number: "))
counter = 0
for i in range(1,n//2+1):
    if n % i == 0:
        counter += 1
print(counter+1)

n = int(input("Enter a number: "))
counter = 0
for i in range(2,n//2+1):
    if n % i == 0:
        counter += 1
print("prime" if counter == 0 else "not prime")

start = int(input())
end = int(input())
for n in range(start,end+1):
    counter = 0
    for i in range(2,n//2+1):
        if n%i == 0:
            counter += 1
    if counter == 0:
        print(n,end=" ")

n = int(input())
fact = 1
for i in range(1,n+1):
    fact = fact * i
print(fact)
'''

n = int(input())
if n<0:
    n = -1 * n
    rev = int(str(n)[::-1])
    print(-1 * rev)
else:
    print(int(str(n)[::-1]))
