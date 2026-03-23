'''Time Complexity: the amount of time taken by an algorithm to run as a function of the length of the input.
O(1)-->constant time complexity
O(n)-->linear time complexity
O(n^2)-->quadratic time complexity
O(log n)-->logarithmic time complexity
O(n log n)-->linearithmic time complexity
O(2^n)-->exponential time complexity
O(n!)-->factorial time complexity

'''
print("Time Complexity:")   #O(1) 

arr =[1,2,3,45]
for i in arr:
    print(i)  #O(n)

arr=[1,2,3,45]
for i in arr:
    for j in arr:
        print(i,j)  #O(n^2)

''' Brute Force-->step by step execute, high complexity,neglects the efficiency
    Optimal Solution--> needs thinking,low complexity
    

def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
print(linear_search([10,20,30,58,46],10))
print(linear_search([10,20,30,58,46],46))
print(linear_search([10,20,30,58,46],30))
'''

def binary_Search(arr,target):
    left, right=0,len(arr)-1
    while left <= right:
        mid =(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]< target:
            left =mid+1
        else:
            right=mid-1
    return -1

print(binary_Search([1,3,5,7,9],5))
