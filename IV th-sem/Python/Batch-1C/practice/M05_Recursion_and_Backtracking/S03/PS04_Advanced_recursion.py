# Sorted check
def is_SortedArray(nums):
    if len(nums) <= 1:
        return True
    if nums[0] > nums[1]:
        return False
    return is_SortedArray(nums[1:])

print(is_SortedArray([10,20,30,40,50]))#True
print(is_SortedArray([10,2,30,14,50]))#False
