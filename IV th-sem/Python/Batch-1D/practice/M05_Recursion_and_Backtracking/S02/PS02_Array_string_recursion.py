#Find sum of array elements
def Array_sum(nums):
    s = 0
    for i in range(len(nums)-1,-1,-1):
        s += nums[i]
    return s
print(Array_sum([10,20,30,40]))#100

def Array_Sum_recursion(nums,i):
    if i == -1:
        return 0
    return nums[i] + Array_Sum_recursion(nums,i-1)

print(Array_Sum_recursion([10,20,30,40],3))#100

def Array_Sum_recursion1(nums):
    if len(nums) == 0:
        return 0
    return nums[-1] + Array_Sum_recursion1(nums[:-1])
print(Array_Sum_recursion1([10,20,30,40]))#100

#Reverse array using Recursion
def Reverse_Array(nums,i,j):
    if i >= j:
        return nums
    nums[i],nums[j] = nums[j],nums[i]
    return Reverse_Array(nums,i+1,j-1)

print(Reverse_Array([1,2,3,4,5],0,4))#[5,4,3,2,1]

#Reverse a string using Recursion
def Reverse_String(st):
    if st == "":
        return ""
    return st[-1] + Reverse_String(st[:-1])

print(Reverse_String("abc"))#"cba"

def is_palindrome(st):
    return st == Reverse_String(st)

print(is_palindrome("abc"))
print(is_palindrome("mam"))