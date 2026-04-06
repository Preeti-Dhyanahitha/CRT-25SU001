#Hashing basics
def frequency_count(s):
    d = {}
    for ch in s:
        if ch not in d:
            d[ch] = 1
        else:
            d[ch] += 1
    return d 

print(frequency_count("aabbcc")) #{'a':2,'b':2,'c':2}

#Leetcode problems
'''
1. Two sum(#1)
2. Contains duplicates(#217)
3. valid Anagram(#242)
4. Happy Number(#202)
5. First unique character in a string(#387)
'''
#Two sum
def twoSum(nums,target):
    d = {}
    for i in range(len(nums)):
        compl = target - nums[i]
        if compl in d:
            return [d[compl],i]
        else:
            d[nums[i]] = i
            
print(twoSum([2,7,11,15],9))