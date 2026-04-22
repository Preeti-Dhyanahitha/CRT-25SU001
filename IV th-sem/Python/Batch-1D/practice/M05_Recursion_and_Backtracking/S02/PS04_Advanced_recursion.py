#Digital root
def Digital_root(n):
    if n <= 9:
        return n
    s = sum([int(i) for i in str(n)])
    return Digital_root(s)

print(Digital_root(456))#6

def is_Sorted_Array(nums):
    pass

print(is_Sorted_Array([10,20,30,40,50]))#True
print(is_Sorted_Array([10,2,30,15,50]))#False