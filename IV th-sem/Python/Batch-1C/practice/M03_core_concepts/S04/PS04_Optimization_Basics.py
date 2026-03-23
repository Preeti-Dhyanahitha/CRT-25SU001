'''
Optimization: It is the process of modifying the code to reduce the time complexity 
Brute Force-->trying of all possible combinations
Optimal Solution--> needs thinking, low complexity

Optimization Basics: Making the solution more efficient
usually we optimize by:
-->reduce time complexity
-->reduce space complexity
-->avoid un-neccessary operations

Programs: 
1) find the sum of numbers in the array
2) find the maximum ele in a list

Common ways to optimize the code:
1.Time Complexity Optimization-->O(n^2) to O(n)
2.Using hashing (set/dict)
3.Avoid repeated calculations
4.Use Built-in-functions
5.List comprehension Optimization

why optimization is important:
-->Improves programs speed
-->Reduces the memory usage
-->avoid nested loops
'''

a=[10,20,30,40,52]
for i in range(len(a)):
    for j in range(len(a)):
        print(a[i] + a[j])    #O(n^2)

a=[10,20,30,40,52]
for num in a:
    print(num + num)      #O(n)

a=[10,20,30,40,52]
sum1=0
for i in range(len(a)):
    sum1+=a[i]
print(sum1)                #O(n)

a=[10,20,30,40,52]
print(sum(a))

a=[]
for i in range(10):
    a.append(i*i)
print(a)

a=print([i*i for i in range(10)])

#2) find the maximum ele in a list