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

def Merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    sorted_left = Merge_sort(left)
    sorted_right = Merge_sort(right)

    return Merge(sorted_left,sorted_right)
print(Merge_sort([14,7,3,12]))