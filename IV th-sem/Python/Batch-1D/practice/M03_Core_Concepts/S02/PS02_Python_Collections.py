'''Python Collections:
1) List:[] -->mutable,heterogeneous,index based
   1) Creating of list: 
   2) Accessing of list:
   3) Creating List with Repeated Elements
   4) Adding Elements to a List (append(),insert(), extend())
   5) Removing Elements from List (remove(), pop(), clear())
   6) Leetcode Problems(169,88,217)

2) Tuples: 
   1) Definition   it is a orderd and immumutable collection of data 
      ( )
   2) Immutable
   3) Accessing --> 
   4) Concatenation -->
   5) Nesting of tuples -->
   6) Repetition of tuples
   7) Slicing of tuples
   8) Deleting a tuple
   9) Leetcode Problems on Tuples (349,657)

3) Sets:{}
 1) Definition --> 
 2) Creation -->
 3) Adding -->
 4) Removing-->remove
 5) Set Operations -->
 6) Leetcode Problems on Sets (268,575)
 
4) Dictionary:
 1) Definition --> stores data in the form of key and value pair 
 2) Creation ({},dict())
 3) Accessing dict items (key[],get())
 4) Adding & Updating dict items (assignment)
 5) Removing dict items (del,pop(),clear())
 6) Leetcode Problems on Dictionary(1, 242)


#1) Creating of list: 
a=[1,23,45,68]
print(a)
b=list((1,23,4,5,7,98))
print(b)

#2) Accessing of list: Index 0 , -1
a=[1,23,45,68]
print(a[1])
print(a[2])
print(a[-1])

#3) Creating List with Repeated Elements
a=[1,2,3]
print(a*2)
 
# 4) Adding Elements to a List
a=[1,2,3]
a.append(50)
a.insert(1,20)
print(a)

#5) Removing Elements from List 
b=list((1,23,4,5,7,98))
print(b)
b.remove(7)
print(b)
b.pop()
print(b)
b.clear()
print(b)


#2) Creation of Set:
a={1,2,3,4,5,6}
print(a)
b=set([1,2,3,45,5])
print(b)

#3) Adding ele in set:
b=set([1,2,3,45,5])
b.add(50)
print(b)

#4) Removing
b=set([1,2,3,45,5])
b.remove(45)
print(b)

# 5) Set Operations:
a={1,2,3,5,6}
b={10,2,3,5,60}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

#6) Leetcode Problems on Sets (268,575)

t=(1,23,45,50)
print(t)

#3) Accessing  of Tuples:
t=(1,23,45,50)
print(t[0])
print(t[3])
print(t[-1])

#4) Concatenation:
t1=(1,23,45,50)
t2=(1,2,87,9,6)
print(t1 + t2)

#5) Nesting of tuples 
t1=(1,23,45,50)       #t1=(1,2,(3,5),58,79)
t2=(1,2,87,9,6)
print(t1 , t2)

#6) Repetition of tuples
t1=(1,23,45,50)
print(t1 *3)

#7) Slicing of tuples:
t1=(1,23,45,50)
print(t1[1:])
print(t1[0:3])
print(t1[:-1])

#8) Deleting a tuple:
t1=(1,23,45,50)
del t1

#9) Leetcode Problems on Tuples (349,657)
'''

#2) Creation ({},dict())
d={'name':'Kalyani','age':23}
print(d)
d=dict(name='kalyani',age=23)
print(d)

#3) Accessing dict items (key[],get()):
d={'name':'Kalyani','age':23}
d.key['name']
print(d)
d.get('name')
print(d)

#4) Adding & Updating dict items (assignment)
d={'name':'Kalyani','age':23}
d['phn']=8453168563
print(d)

#5) Removing dict items (del,pop()-->remove key but return value,clear()-->empty dict)
d={'name':'Kalyani','age':23}
del d['age']
d.pop('name')
print(d)
d.clear()
print(d)

# 6) Leetcode Problems on Dictionary(1, 242)