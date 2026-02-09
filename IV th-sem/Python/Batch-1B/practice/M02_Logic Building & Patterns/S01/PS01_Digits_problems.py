'''
sample input : 1234
sample output : 4

sample input : 455786
sample output : 6 

sample input : 45
sample output : 2

n = int(input())
count = 0
while n > 0:
    count += 1
    n = n // 10
print(count)

print(len(str(n)))

n = int(input())
temp = n
s = 0
while n > 0:
    s += (n%10)
    n //= 10
print(s)

print(sum(map(int,str(temp))))

n = int(input())
even = odd = 0
while n > 0:
    if (n % 2) == 0:
        even += 1 
    else:
        odd += 1
    n //= 10
print(even,odd)
'''
n = int(input())

while n > 9:
    n = sum(map(int,str(n)))
print(n)