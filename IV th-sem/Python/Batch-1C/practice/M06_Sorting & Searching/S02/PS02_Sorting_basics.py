#Bubble sort
def Bubble_sort(nums):
    n = len(nums)
    for i in range(n-1):
        for j in range(n-1-i):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums

print(Bubble_sort([5,1,4,2,3]))#[1,2,3,4,5]

def Selection_sort(nums):
    n = len(nums)
    for i in range(n):
        pos = i
        for j in range(i+1,n):
            if nums[j] < nums[pos]:
                pos = j
        nums[i],nums[pos] = nums[pos],nums[i]
    return nums 

print(Selection_sort([5,1,4,2,3]))#[1,2,3,4,5]

def Insertion_sort(nums):
    n = len(nums)
    for i in range(1,n):
        j = i - 1
        key = nums[i]
        while j >= 0 and nums[j] > key:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key
    return nums

print(Insertion_sort([5,1,4,2,3]))#[1,2,3,4,5]
