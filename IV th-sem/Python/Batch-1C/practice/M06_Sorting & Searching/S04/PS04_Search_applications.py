'''
1. Lower bound 
2. 33. Search in Rotated Sorted Array
3. 912. Sort an Array'''

#Lower bound
def Lower_bound(arr,target):
    low,high = 0,len(arr)-1
    while low <= high:
        mid = (low + high)//2
        if target <= arr[mid]:
            high = mid-1
        else:
            low = mid + 1
    return low
print(Lower_bound([2, 3, 7, 10, 11, 11, 25],9))
print(Lower_bound([2, 3, 7, 10, 11, 11, 25],11))
print(Lower_bound([2, 3, 7, 10, 11, 11, 25],100))