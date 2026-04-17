#Subsets, permutations
#Subsets
def subsets(nums):
    res = []
    n = len(nums)
    stop_value = 2 ** n
    for i in range(stop_value):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(nums[j])
        res.append(subset)
    return res
        
print(subsets([1,2,3]))