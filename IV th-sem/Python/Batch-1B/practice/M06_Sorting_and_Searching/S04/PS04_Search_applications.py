'''
1. Lower bound
2. 189. Rotate Array 
3. 33. Search in Rotated Sorted Array
4. 912. Sort an Array'''

#Lower bound
def Lower_bound(li,x):
    low,high = 0,len(li)-1
    while low < high:
        mid = (low + high) // 2
        if li[mid] < x:
            low = mid + 1
        else:
            high = mid 
    if low == len(li) - 1:
        return low + 1
    return low

print(Lower_bound([10,15,23,27,30,35,36],25))#3
print(Lower_bound([10,15,23,27,30,35,36],33))#5
print(Lower_bound([10,15,23,27,30,35,36],40))#7

#33. Search in Rotated Sorted Array
def search(nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1
print(search([4,5,6,7,0,1,2],0))