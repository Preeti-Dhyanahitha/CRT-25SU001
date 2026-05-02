#Lower bound
def Lower_bound(arr,target):
    low,high = 0,len(arr)
    while low < high:
        mid = (low + high) // 2
        if target <= arr[mid]:
            high = mid 
        else:
            low = mid + 1
    return low

print(Lower_bound([2, 3, 7, 10, 11, 11, 25],9))#3
print(Lower_bound([2, 3, 7, 10, 11, 11, 25],11))#4
print(Lower_bound([2, 3, 7, 10, 11, 11, 25],100))#7

#33. Search in Rotated Sorted Array
def search(nums,target):
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
