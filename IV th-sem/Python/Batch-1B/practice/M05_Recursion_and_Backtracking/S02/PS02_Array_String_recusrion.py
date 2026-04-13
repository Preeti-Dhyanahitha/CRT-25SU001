#Array sum
#Traditional Approach
def Array_sum(nums):
    s = 0
    for i in range(len(nums)-1,-1,-1):
        s += nums[i]
    return s

print(Array_sum([1,2,3,4,5]))#15

#Recursive Approach
def Array_sum1(nums,i):
    if i == 0:
        return 0
    return nums[i-1] + Array_sum1(nums,i-1)

print(Array_sum1([1,2,3,4,5],5))#15

def Array_sum2(nums):
    if len(nums) == 0:
        return 0
    return nums[-1] + Array_sum2(nums[:-1])

print(Array_sum2([1,2,3,4,5]))#15

li = [12,0,45,78,6,9]
print(li)
print(li[:-1])

#Reverse an array
def Reverse_array(nums,i,j):
    if i >= j:
        return nums
    nums[i],nums[j] = nums[j],nums[i]
    return Reverse_array(nums,i+1,j-1) 

print(Reverse_array([1,2,3,4,5],0,4))#[5,4,3,2,1]

def Reverse_String(st):
    if st == "":
        return ""
    return st[-1] + Reverse_String(st[:-1])

print(Reverse_String("abc")) #"cba"

def is_palindrome(st):
    return st == Reverse_String(st)

print(is_palindrome("abc"))#False
print(is_palindrome("madam"))#True
