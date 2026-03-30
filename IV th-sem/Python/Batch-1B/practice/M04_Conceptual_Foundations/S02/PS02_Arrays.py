'''
Arrays:
1) Reverse the array ele
    a) USing slicing
    b) Using reverese()
    c) Using loop
2) Check if an array is sorted 
3) Find max and min ele?
4) Find Second Largest Element
5) Remove Duplicates from Array
6) Count Frequency of Elements
7) Rotate Array 
8) Leetcode -->724,1822
'''
#Reverse the array elements
'''
input : [12,45,36,78]
output : [78,36,45,12]

#solution-1
li = [12,45,36,78]
stop = -1 * (len(li) + 1)
res = []
for i in range(-1,stop,-1):
    res.append(li[i])

print(res)
#Solution-2
res1 = [li[i] for i in range(-1,stop,-1)]
print(res1)

#Solution-3
li = [12,45,36,78]
res2 = []
for ele in li:
    res2 = [ele] + res2
print(res2)
'''
def check_array_sorted(nums):
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return False
    return True

print(check_array_sorted([12,45,78,96,100]))

'''
nums = [12,45,78,96,100]
True

nums = [121,36,78,200]
False
'''