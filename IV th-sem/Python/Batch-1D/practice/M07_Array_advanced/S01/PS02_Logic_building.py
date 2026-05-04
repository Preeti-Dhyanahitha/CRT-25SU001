#Move zeros
from typing import List
def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i] = nums[j]
            i += 1
    for k in range(i,len(nums)):
        nums[k] = 0

#Missing number
def missingNumber(self, nums: List[int]) -> int:
    n = len(nums)
    s1 = (n*(n+1)) // 2
    s2 = sum(nums)
    return s1 - s2