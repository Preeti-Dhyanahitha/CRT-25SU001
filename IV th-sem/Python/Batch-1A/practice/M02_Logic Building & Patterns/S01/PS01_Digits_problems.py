'''
1. Count the number of digits in a number.
2. Find the sum of digits of a number.
3. Reverse a number.
4. Check palindrome number.
5. Check Armstrong number.
6. Count even and odd digits.
7. Find largest digit.
8. Find smallest digit.
9. Count zero digits.
10. Find digital root of a number.
11. Check Spy number.

sample input : 1234
sample output : 4

sample input : 12236
sample output : 5

n = int(input())
count = 0
while n > 0:
    count += 1
    n = n // 10
print(count)

sample input : 1234
sample output : 10

sample input : 12236
sample output : 14

n = int(input())
s = 0
while n > 0:
    s += (n % 10)
    n = n // 10
print(s)
'''
def reverse(num):
    rev = 0
    while num > 0 :
        rev = (rev*10) + (num % 10) 
        num = num // 10
    return rev
'''
n = reverse(int(input()))
while n > 0:
    digit =n % 10
    if digit % 2 == 0:
        print(digit,end=" ")
    n = n // 10
'''
n = int(input())
temp = reverse(n)

print(temp == n)

if temp == n:
    print(True)
else:
    print(False)

print(True) if temp == n else print(False)