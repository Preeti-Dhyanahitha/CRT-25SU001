#560. Subarray Sum Equals K
def subarraySum(nums, k):
    freq = {0:1}
    pref_sum = 0
    count = 0
    for ele in nums:
        pref_sum += ele
        if (pref_sum - k) in freq:
            count += freq[pref_sum - k]
        freq[pref_sum] = freq.get(pref_sum,0) + 1
    return count