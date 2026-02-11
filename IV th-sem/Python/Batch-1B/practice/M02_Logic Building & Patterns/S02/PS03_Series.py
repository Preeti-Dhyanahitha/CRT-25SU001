'''Fibonacci series:
'''
n = int(input())
f1,f2 = 0,1
for i in range(n):
    print(f1,end=" ")
    f1,f2 = f2,f1+f2 
print()
#using list
fib = [0,1]
for i in range(2,n):
    fib.append(fib[i-1] + fib[i-2])
for i in fib:
    print(i,end=" ")