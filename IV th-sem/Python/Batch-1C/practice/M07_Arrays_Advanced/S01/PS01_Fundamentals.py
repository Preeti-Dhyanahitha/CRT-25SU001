'''
189. rotate array
179. Largest number
missing number'''

#missing number
def missingNumber(nums):
    '''
    res = len(nums)

    for i in range(len(nums)):
        res += i - nums[i]
    
    return res
    '''
    n = len(nums)
    res = (n * (n+1))//2
    return res - sum(nums)

#189. rotate array
def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in range(k):
        p = nums.pop()
        nums.insert(0,p)

#179. Largest number