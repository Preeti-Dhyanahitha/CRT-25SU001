#Searching techniques
'''
1. Linear search(sequential)
2. Binary search(Interval)
'''
def Linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

li = list(map(int,input().split()))
target = int(input())
print(Linear_search(li,target))#-1

target1 = int(input())
print(Linear_search(li,target1))#0

#Binary search
def Binary_search(arr,target):
    low,high = 0,len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

print(Binary_search([2,5,7,8,10,20,36,45],7))#2