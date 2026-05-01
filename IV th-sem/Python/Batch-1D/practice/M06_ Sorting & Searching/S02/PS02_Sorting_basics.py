#Bubble sort
def Bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

print(Bubble_sort([5,1,4,2,8]))#[1,2,4,5,8]

#Selection sort
def Selection_sort(arr):
    n = len(arr)
    for i in range(n):
        pos = i
        for j in range(i+1,n):
            if arr[j] < arr[pos]:
                pos = j
        arr[i],arr[pos] = arr[pos],arr[i]
    return arr

print(Selection_sort([1,10,23,-2]))#[-2,1,10,23]

#Insertion sort
def Insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

print(Insertion_sort([23,1,10,5,2]))