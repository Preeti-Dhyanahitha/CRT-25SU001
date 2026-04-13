#Leetcode problems
'''
1. Two sum(#1)
2. Contains duplicates(#217)
3. valid Anagram(#242)
4. Happy Number(#202)
5. First unique character in a string(#387)
'''
#Frequecny count
def frequency_count(st):
    d = {}
    for ch in st:
        if ch not in d:
            d[ch] = 1
        else:
            d[ch] += 1
    return d 

print(frequency_count("abcabc"))#{'a':2,'b':2,'c':2}

#Contains duplicates(#217)
def containsDuplicate(nums):
        return len(nums) != len(set(nums))

print(containsDuplicate([1,2,3,1]))#True

#First unique character in a string(#387)
from collections import Counter
def firstUniqChar(self, s: str) -> int:
    d = dict(Counter(s))
    for i,ch in enumerate(s):
        if d[ch] == 1:
            return i
    return -1

# Two sum(#1)
def twoSum(nums,target):
    d = {}
    for i in range(len(nums)):
        compl = target - nums[i]
        if compl in d:
            return [d[compl],i]
        else:
            d[nums[i]] = i
            