#Merge sort
def Merge(left,right):
    i,j = 0,0
    res = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1 
    res.extend(left[i:])
    res.extend(right[j:])
    return res

def Merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]
    left_sorted = Merge_sort(left)
    right_sorted = Merge_sort(right)
    return Merge(left_sorted,right_sorted)

print(Merge_sort([14,7,3,12]))

#Quick sort
#Identify pivot element index
def Partition(arr,low,high):
    pivot = arr[low]
    i,j = low+1,high
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i],arr[j] = arr[j],arr[i]
        else:
            break
    arr[low],arr[j] = arr[j],arr[low]
    return j

def Quick_sort(arr,low,high):
    if low < high:
        p = Partition(arr,low,high)
        Quick_sort(arr,low,p-1)
        Quick_sort(arr,p+1,high)
        return arr
    
print(Quick_sort([14,7,3,12],0,3))