#Searching Techniques
'''
1. Linear search(sequential search):
Best case ==> O(1)
Average case ==> O(n)
Worst case ==> O(n)

2. Binary search(Interval search)
'''
def Linear_Search(nums,target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

li = list(map(int,input().split()))
target = int(input())
print(Linear_Search(li,target))

target1 = int(input())
print(Linear_Search(li,target1))

#Binary Search
def Binary_Search(nums,target):
    nums.sort()
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1
    

li = list(map(int,input().split()))
target = int(input())

print(Binary_Search(li,target))
