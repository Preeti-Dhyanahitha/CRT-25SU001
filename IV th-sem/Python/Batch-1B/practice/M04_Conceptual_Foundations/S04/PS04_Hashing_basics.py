#Hashing ==> Set,Dictionary
#d = {1:'a',2:'b',3:'c',1:'z'}
'''
def twoSum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

print(twoSum([3,2,4],6))

def twoSum1(nums,target):
    d = {}
    for i in range(len(nums)):
        comp = target - nums[i]
        if comp in d:
            return [d[comp],i]
        d[nums[i]] = i

print(twoSum1([3,2,4],6))       
'''
from collections import Counter

c = Counter("abcabc")

print(c,type(c))

d = dict(c)
print(d)