#560. Subarray Sum Equals K
def subarraySum(nums,k):
    d = {0:1}
    pref_sum = 0
    count = 0
    for ele in nums:
        pref_sum += ele
        if pref_sum - k in d:
            count += d[pref_sum - k]
        d[pref_sum] = d.get(pref_sum,0)+1
    return count