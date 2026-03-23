'''
Optimization:it is the process of modifying the code to get more efficient
Efficient:
-->to reduce time complexity
-->to reduce space complexity
-->to reduce memory usage
-->to avoid un-neccessary Operations
Real-World Ex:

Brute force-->step by step execution,easy to implement for less input
Optimal Solution-->reduce the time complexity

'''
a=[10,20,30,40,50]
target=30
for i in range(len(a)):
    if a[i]==target:
        print("Ele Found")

a=[10,20,30,40,50]
if 30 in a:
    print("Ele Found")

#write the python code to print the sum of ele in list
a=[10,20,30,40,50]
sum1=0
for i in range(len(a)):
    sum1 +=a[i]
print(sum1)           #Brute Force


a=[10,20,30,40,50]
res=sum(a)
print(res)

#Two Sum
a=[2,7,11,15]
target=9
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j] == target:
            print(i,j)                  #O(n^2)-->Brute Force

a=[2,7,11,15]
target=9
d={}
for i in range(len(a)):
    res=target-a[i]
    if res in d:
        print([d[res],i])
    d[a[i]]=i                   #O(n)-->Optimal Solution

'''Common ways to get Optimization:
1)Reducing the time complexity optimization (Ex:O(n^2) to O(n))
2)hashing(use set/dict)
3)Avoid un-neccessary calculations
4)Use Built-in_functions
5)List Comprehension Optimization
'''
a=[]
for i in range(10):
    a.append(i*i)
print(a)

a=[i*i for i in range(10)]
print(a) 

#write the python code to print the max ele using for loop?