#Quick sort
def Partition(arr,low,high):
    pivot = arr[low]
    i,j = low + 1,high
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i],arr[j] = arr[j],arr[i]
        else:
            break
    arr[low],arr[j] = arr[j],arr[low]
    return j

def Quick_sort(arr,low,high):
    if low <= high:
        p = Partition(arr,low,high)
        Quick_sort(arr,low,p-1)
        Quick_sort(arr,p+1,high)
    return arr

print(Quick_sort([54,26,93,17,77,31,44,55,20],0,8))