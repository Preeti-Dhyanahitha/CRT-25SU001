#Two sum, Kadane, majority 
#53. Maximum Subarray
from typing import List
def maxSubArray(nums: List[int]) -> int:
    s1 = nums[0] #current sum
    s2 = nums[0] #maximum sum
    for i in range(1,len(nums)):
        s1 = max(nums[i],s1+nums[i])
        s2 = max(s1,s2)
    return s2

#169. Majority element
from collections import Counter
def majorityElement(self, nums: List[int]) -> int:
    d = dict(Counter(nums))
    n = len(nums)
    for key,val in d.items():
        if val > (n//2):
            return key
        
#1. Two sum
def twoSum(self, nums: List[int], target: int) -> List[int]:
    d = {}
    for i in range(len(nums)):
        compl = target - nums[i]
        if compl in d:
            return [d[compl],i]
        else:
            d[nums[i]] = i
                