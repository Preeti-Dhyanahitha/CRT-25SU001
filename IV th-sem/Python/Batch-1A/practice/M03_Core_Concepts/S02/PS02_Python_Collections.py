'''Python Collections:
1) List:[]-->heterogenous,index,mutable
   1) Creating of list: 
   2) Accessing of list:
   3)  Creating List with Repeated Elements
   4) Adding Elements to a List (append(),insert(), extend())
   5) Removing Elements from List (remove(), pop(), clear())
   6) Leetcode Problems(169,88,217)

2) Sets:{}
 1) Definition -->
 2) Creation -->
 3) Adding -->
 4) Removing-->remove
 5) Set Operations -->
 6) Leetcode Problems on Sets (268,575)

3) Tuples: 
   1) Definition  -->Ordered immutable collection of data ele 
   2) Immutable-->Can not modify,change
   3) Accessing --> 
   4) Concatenation -->
   5) Nesting of tuples -->A tuple inside another tuple
   6) Repetition of tuples
   7) Slicing of tuples
   8) Deleting a tuple
   9) Leetcode Problems on Tuples (349,657)

t=(10,20,30,40,50)
print(t)
t1=tuple((10,20,30,40,50))
print(t1)
print(t[0])
print(t[-1])
print(t + t1)
print(tuple(t,t1))
print(t * 3)
print(t[0:])
print(t1[1:3])
del t                #Error
print(t)
'''

'''
4) Dictionary:
 1) Definition-->Collection of data, stores in the form of key and values pair
 keys are unique
 2) Creation ({},dict())
 3) Accessing dict items 
 4) Adding & Updating dict items (assignment)
 5) Removing dict items (del,pop(),clear())
 6) Leetcode Problems on Dictionary(1, 242)
'''
d={'name':'kalyani','a':'sai','age':23}
print(d)
d1=dict(name='kalyani',a='sai',age=23)
print(d1)
print(d1['name'])
print(d1.get('name'))
print(d1.keys())
print(d1.values())
d1['name']='krishna'
print(d1)

val=d1.pop('a')
print(val)
print(d1)

d1.clear()
print(d1)

#ex: 'sai'  and 'iasa'
'''
# 1) Creating of list: 
a=[10,20,30,40,50]
print(a)
b= list(10,20,312)
print(b)

# 2) Accessing of list:
a=[10,20,30,40,50]
print(a[0])
print(a[-1])

#3)  Creating List with Repeated Elements
a=[10,20,30,40,50]
print(a * 2)

#4) Adding Elements to a List
a=[10,20,30,40,50]
a.append(100)
print(a)
a.insert(1,50)
print(a)

# 5) Removing Elements from List
a=[10,20,30,40,50]
a.remove(40)
print(a)
a.pop()
print(a)

#6) Slicing
a=[10,20,30,40,50]
print(a[0:])
print(a[2:])
#reverse the list using slicing

# 7) Leetcode Problems(169,88,217)

# 2) Set Creation 
a=set([10,20,30,450])
print(a)

#3) Adding
a=set([10,20,30,450])
a.add(80)
print(a)

# 4) Removing-->remove
a=set([10,20,30,450])
a.remove(450)
print(a)

# 5) Set Operation
a=set([10,20,30,450])
b=set([20,30,45,40])
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

#6) Leetcode Problems on Sets (268,575)

'''