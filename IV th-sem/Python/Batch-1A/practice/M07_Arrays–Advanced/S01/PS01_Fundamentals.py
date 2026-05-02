#Largest Number
from functools import cmp_to_key
def largestNumber(nums):
    s=[str(x) for x in nums]
    def cmp(x, y):
        return -1 if x+y>y+x else 1
    s.sort(key=cmp_to_key(cmp))
    ans="".join(s)
    return '0' if ans[0]=='0' else ans

print(largestNumber([10,2]))
print(largestNumber([3,30,34,5,9]))

#rotate array
def rotate(nums,k):
    pass

print(rotate([1,2,3,4,5,6,7],3))
