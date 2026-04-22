#Linear Search
# Best case ==> O(1)
# Average case and Worst case ==> )(n)
def Linear_search(nums,target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

li = list(map(int,input().split()))
target1 = int(input())

print(Linear_search(li,target1))#1

target2 = int(input())
print(Linear_search(li,target2))#-1

def Binary_search(nums):
    pass

    