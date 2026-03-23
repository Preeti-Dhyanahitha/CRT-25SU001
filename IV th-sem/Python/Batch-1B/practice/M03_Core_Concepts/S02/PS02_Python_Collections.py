''' 
Sets:
 1) Definition -->unordereed,unique collection of data { }
 2) Creation -->
 3) Adding -->
 4) Removing-->remove,discard
 5) Set Operations -->Union,intersection,difference 
 6) Leetcode Problems on Sets (268,575)

Tuples: 
 1) Definition --> It is a orderd and immumutable collection of data 
 ( )
 2) Immutable-->can not change the elem once it is created
 3) Accessing --> 
 4) Concatenation --> 
 5) Nesting of tuples --> 
 6) Repetition of tuples
 7) Slicing of tuples
 8) Deleting a tuple
 9) Leetcode Problems on Tuples (349,657)

Dictionary:
 1) Definition --> stores data in the form of key and value pair 
 2) Creation ({},dict())
 3) Accessing dict items (key[],get())
 4) Adding & Updating dict items (assignment)
 5) Removing dict items (del,pop(),popitem(),clear())
 6) Leetcode Problems on Dictionary(1, 242)

a=set([10,20,30,40,50]) #hash(value%5)
print(a)
a.add(78)
a.add(50)
print(a)
a.remove(20)
print(a)
a.discard(30)
print(a)
b=set([20,30,40,70,80])
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

t=(1,2,3,45,50)
print(t)

#3) Adding & Updating dict items
t=(1,2,3,45,50)
t[0]=10
print(t[0])     #Error

#4) Concatenation of tuple:
t=(1,2,3,45,50)
t2= (2,3,547,8)
print(t + t2)

#5) Repetition of tuples
t=(1,2,3,45,50)
print(t * 3)

#6)Nesting of tuples
t=(1,2,3,45,50)    #t=(1,2,(3,4,5),8)
t2= (2,3,547,8)
print(t,t2)

#7) Slicing of tuples
t=(1,2,3,45,50)
print(t[1:])
print(t[0:3])

#8)Deleting a tuple:
t=(1,2,3,45,50)
del t
print(t)

#9) Leetcode Problems on Tuples (349,657)
'''

#2) Creation ({},dict())
d={"name":"kalyani",'age':23}
print(d)
d1=dict(name='kalyani',age=23)
print(d1)

#3) Accessing dict items:
d={"name":"kalyani",'age':23}
print(d.get('name'))
print(d.keys())
print(d.values())

#4) Adding & Updating dict items
d={"name":"kalyani",'age':23}
d['phn']=46432
print(d)
d['name']='sai'
print(d)

#5) Removing dict items (del,pop(),popitem(),clear())
d={"name":"kalyani",'age':23}
del d['age']
print(d.pop('name'))
print(d.popitem())
d.clear()

#6) Leetcode Problems on Dictionary(1, 242)
