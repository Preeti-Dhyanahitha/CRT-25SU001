'''
Brute Force-->trying of all possible combinations
Optimal Solution--> needs thinking, low complexity

Optimization Basics: Making the solution more efficient
usually we optimize by:
-->reduce time complexity
-->reduce space complexity
-->avoid un-neccessary operations

Programs: 
1) find the sum of numbers from 1 to n
2) find the maximum ele in a list

Common ways to optimize the code:
1.Time Complexity Optimization
2.Using hashing
3.Avoid repeated calculations
4.Use Built-in-functions
5.List comprehension Optimization



input : [1,2,3,4,5,1]
output : True

input : [1,2,3]
output : False
'''
def check_duplicates_bruteforce(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

print(check_duplicates_bruteforce([1,2,3,4,5,1]))

def check_duplicates_optimal(nums):
    s = set()
    for ele in nums:
        if ele in s:
            return True
        s.add(ele)
    return False

print(check_duplicates_optimal([1,2,3,4,5,1]))
