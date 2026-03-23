'''Time Complexity:  time required to run an algorithm based upon the input
Big O notation

O(1)-->Constant Time -->Real-World: Accessing of a student with the roll.no in a List
O(n)-->Linear Time--> Real-World: taking Attendance of the class
O(n^2)-->Quadratic Time
O(log n)-->Logarithmic Time 
O(n logn)-->Linearithmic Time
O(2^n)-->Exponential Time
'''
def constant_time(arr):
    return arr[0]
print(constant_time[10,20,30])     #O(1)


def Linear_Time(arr):
    for i in arr:
        print(i)
print(Linear_Time[10,20,30,40,50])    #O(n)


def Quadratic_Time(arr):
    for i in arr:
        for j in arr:
            print(i)
print(Quadratic_Time[10,20,30,40,50])     #O(n^2)

def linearthmic_time(arr):
    return sorted(arr)
print(linearthmic_time[10,20,30,10,50,20])    #O(n logn)

def fibo(n):
    if n<=1:
        return n
    return fibo(n-1)+fibo(n-2)
n =int(input())
print(fibo(n))     #O(2^n)