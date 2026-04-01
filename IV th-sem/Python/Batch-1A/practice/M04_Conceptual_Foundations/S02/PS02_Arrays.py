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


#input : [12,45,36,78,96]
#output : [96,78,36,45,12]
#Traditional
li = [12,45,36,78,96]
res = []
stop = -1 * (len(li)+1)
for i in range(-1,stop,-1):
    res.append(li[i])
print(res)
#List comprehension
res1 = [li[i] for i in range(-1,stop,-1)]
print(res1)

#using swapping technique
li = [12,45,36,78,96]
n = len(li)
print("Before reversing:",li)
for i in range(n//2):
    li[i],li[n-1-i] = li[n-1-i],li[i]
print("After reversing:",li)

li = [12,45,36,78,96]
res = []
for ele in li:
    #res.insert(0,ele)
    res = [ele] + res
print(res)

#Check if an array is sorted 
# input : [12,23,45,56,69,100] ==> output : True
# input : [12,45,36,78,96] ==> output : False
def check_sorted(nums):
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return False
    return True
print(check_sorted([12,45,36,78,96]))
print(check_sorted([12,23,45,56,69,100]))
'''
#Count Frequency of Elements
# input : [1,2,3,4,1,2,5,2,4] 
# output :{1:2,2:3,3:1,4:2,5:1}
li = [1,2,3,4,1,2,5,2,4]
res = {}
for ele in li:
    if ele not in res:
        res[ele] = 1
    else:
        res[ele] += 1
print(res)