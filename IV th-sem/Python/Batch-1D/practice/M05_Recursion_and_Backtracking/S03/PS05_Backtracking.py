def subsets(nums):
        res = []
        def Backtrack(i,subset):
            res.append(subset[:])
            for j in range(i,len(nums)):
                subset.append(nums[j])
                Backtrack(j+1,subset)
                subset.pop()
        Backtrack(0,[])
        return res