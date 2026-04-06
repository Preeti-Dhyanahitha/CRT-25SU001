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
#List
# min(),max(),len(),sum(),reversed(),list()
# + ==> concatenation,* ==> Repitition

def Reverse_list(li):
    res = []
    for ele in li:
        res.insert(0,ele)
    return res

    '''Solution-1
    res = []
    stop = -1 * (len(li) + 1)
    for i in range(-1,stop,-1):
        res.append(li[i])
    return res

    Solution-2
    
    stop = -1 * (len(li) + 1)
    res = [li[i] for i in range(-1,stop,-1)]
    return res

    Solution-3
    
    n = len(li)
    for i in range(0,n//2):
        li[i],li[n-1-i] = li[n-1-i],li[i]
    return li
    
    Solution-4
    
print(Reverse_list([1,2,3,4])) #[4,3,2,1]

def is_sorted(nums):
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return False
    return True

print(is_sorted([12,23,45,56,78])) # True
print(is_sorted([45,20,36,78,1])) # False
'''

#Count Frequency of Elements
'''
input : [1,2,3,2,4,3,1,5]
output : {1:2,2:2,3:2,4:1,5:1}
'''
li = [1,2,3,2,4,3,1,5]
d = {}
for i in li:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d)

li = [1,2,3,2,4,3,1,5]
d = {}
for i in li:
    d[i] = d.get(i,0) + 1
print(d)

print(d.get(2))
print(d.get(10,0))
