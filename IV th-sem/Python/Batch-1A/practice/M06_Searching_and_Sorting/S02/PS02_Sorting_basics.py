#Bubble sort
def Bubble_sort(nums):
    n = len(nums)
    for i in range(n-1):
        for j in range(n-1-i):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums

print(Bubble_sort([12,23,45,20,1,36,5]))#[1,5,12,20,23,36,45]

#Selection sort
def Selection_sort(nums):
    pass

print(Selection_sort([12,23,45,20,1]))#[1,12,20,23,45]