#Rotate array
from typing import List
def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in range(k):
        p = nums.pop()
        nums.insert(0,p)

#Largest number
from collections import cmp_to_key
def largestNumber(nums: List[int])-> str:
        s=[str(x) for x in nums]
        def cmp(x, y):
            return -1 if x+y>y+x else 1
        s.sort(key=cmp_to_key(cmp))
        ans="".join(s)
        return '0' if ans[0]=='0' else ans