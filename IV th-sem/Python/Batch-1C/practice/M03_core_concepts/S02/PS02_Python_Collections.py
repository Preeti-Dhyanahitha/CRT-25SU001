'''Set:
1. use {} to create a set
2. set does not allow duplicates
3. set unindexed
4. set is unordered
5. set is heterogenous
6. set is mutable
s = {1,True,10,12.45,10,9+5j}
print(s,type(s))
print(s[3])

#Adding elements
A = {1,2,3}
B = {3,4,5}
A.add(4)
B.update({6,7})
print(A,B)

#Removing elements
A.pop()
print(A)
print(help('set'))

268: Missing number

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
 
Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation:
n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
Example 2:
Input: nums = [0,1]
Output: 2
Explanation:
n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation:
n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
 
Constraints:
n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.
'''
nums = [3,0,1]
n = len(nums)
res = set(range(n+1))
res = res - set(nums)
print(res.pop())

s = (n * (n+1))//2
print(s - sum(nums))