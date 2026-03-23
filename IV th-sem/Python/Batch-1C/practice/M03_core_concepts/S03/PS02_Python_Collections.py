'''
Dictionary:
 1) Definition --> stores data in the form of key and value pair 

 2) Creation ({},dict())
 3) Accessing dict items (key[],get())
 4) Adding & Updating dict items (assignment)
 5) Removing dict items (del,pop(),popitem(),clear())
 6) Leetcode Problems on Dictionary(1, 242)




Tuples: 
 1) Definition   it is a orderd and immumutable collection of data 
 ( )
 2) Immutable
 3) Accessing -->index positions +Ve or -ve
 4) Concatenation -->+ 
 5) Nesting of tuples --> tuple inside a tuple
 6) Repetition of tuples
 7) Slicing of tuples
 8) Deleting a tuple
 9) Leetcode Problems on Tuples (349,657)
 
t = (10,23,50,12,45,32,48)
t2=("sai",'kalyani',"krishna")

print(t[0])
print(t[-1])
print(t + t2) 
print(t,t2) 
print(t *5) 
print(t[1:4])
print(t[:5])
print(t[:-1])
del t 
'''
d={"a":'Sai'}
print(d)
d2= dict(a='Sai',b='Kalyani',c='Krishna')
print(d2)
print(d2['a'])
print(d2.get('b'))
print(d2.keys())
print(d2.values())
print(d2={'age':25}) 
'''deleting of dictionary
1) del -->
2) pop()--> removes key returns value 
3)  popitem() --> removes last inserted key value pair and returns it as tuple
4) clear()--> removes entire dict 