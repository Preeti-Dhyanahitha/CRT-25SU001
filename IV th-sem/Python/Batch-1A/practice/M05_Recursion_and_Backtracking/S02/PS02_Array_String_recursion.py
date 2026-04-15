#Sum of array elements
#Traditional Approach
def Array_sum(nums):
    s = 0
    for i in range(len(nums)-1,-1,-1):
        s += nums[i]
    return s
print(Array_sum([1,2,3,4,5])) #15

#Recursive Approach-1
def Array_sum1(nums,index):
    if index == -1:
        return 0
    return nums[index] + Array_sum1(nums,index-1)
    
print(Array_sum1([1,2,3,4,5],4)) #15

#Recurive Approach-2
def Array_sum2(nums):
    if len(nums) == 0:
        return 0
    return nums[-1] + Array_sum2(nums[:-1])

print(Array_sum2([1,2,3,4,5])) #15

#Reverse an Array
def Reverse_Array(nums,i,j):
    if i >= j:
        return nums
    nums[i],nums[j] = nums[j],nums[i]
    return Reverse_Array(nums,i+1,j-1) 

print(Reverse_Array([1,2,3,4,5],0,4))#[5,4,3,2,1]

# Reverse a string
def Reverse_String(st):
    if len(st) == 0:
        return ""
    return st[-1] + Reverse_String(st[:-1])

print(Reverse_String("abc"))#"cba"

def is_palindrome(st):
    return st == Reverse_String(st)

print(is_palindrome("abc"))
print(is_palindrome("abcba"))