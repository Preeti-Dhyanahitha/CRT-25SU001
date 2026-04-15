#Digital root sum
def Digital_sum(n):
    if n < 10:
        return n
    s = sum([int(ch) for ch in str(n)])
    return Digital_sum(s)

print(Digital_sum(386))

#sorted check
def is_SortedArray(nums):
    if len(nums) <= 1:
        return True
    if nums[0] > nums[1]:
        return False
    return is_SortedArray(nums[1:])

print(is_SortedArray([10,20,30,40,50]))#True
print(is_SortedArray([10,2,30,15,50]))#False

#Leetcode problems:
# 231,326,342,486,509,50