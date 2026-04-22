# Two searching techniques
'''
1. Sequential search(Linear search)
best case ==> O(1)
Average case ==> O(n)
Worst case ==> O(n)

2. Interval search
'''
def Linear_Search(nums,target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

li = list(map(int,input().split()))
target = int(input())

print(Linear_Search(li,target))

def Binary_Search(nums,target):
    low,high = 0,len(nums)-1
    while low <= high:
        mid = (low + high) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

li = list(map(int,input().split()))
target = int(input())

print(Binary_Search(li,target))