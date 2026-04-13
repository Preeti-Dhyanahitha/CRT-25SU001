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