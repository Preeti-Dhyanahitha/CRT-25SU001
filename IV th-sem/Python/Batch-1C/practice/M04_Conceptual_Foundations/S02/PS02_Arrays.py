'''
Arrays:
1) Reverse the array ele
    a) USing slicing
    b) Using reverese()
    c) Using loop
2) Check if an array is sorted 
3) Find max and min ele?
4) Find Second Largest Element
5) Remove Duplicates from Array
6) Count Frequency of Elements
7) Rotate Array 
8) Leetcode -->724
'''
a=[10,23,45,65,1,2,3]
a.sort()
print(a[::-1]) 

a=[10,23,45,65,1,2,3]
a.sort()
a.reverse()
print(a)

a=[10,23,45,65,1,2,3]
rev=[]
for i in range(len(a)):
    rev=[i]+rev
print(rev)

#2) Check if an array is sorted 
a=[10,23,45,65,1,2,3]
b=True
for i in range(len(a)-1):
    if a[i] > a[i+1]:
        b=False
print(b)

#3) Find max and min ele?
#4) Find Second Largest Element?
#5) Remove Duplicates from Array?
#6) Count Frequency of Elements
#7) Rotate Array 

a=[10,23,45,65,1,2,3,3,4,7,1,1,2]
d={}
for i in a:
    d[i]=d.get(i,0)+1
print(d)

a=[10,23,45,65,1,2,3,3,4,7,1,1,2]
k=2
rotation=a[k:]+a[:k]
print(rotation)

#8) Leetcode -->724