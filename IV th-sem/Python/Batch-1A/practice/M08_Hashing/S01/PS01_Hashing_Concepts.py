#set
'''
s = set()
#union,intersection,difference
#print(dir(s))

d = {}
#Adding entry to the dictionary
#statement
d[1] = 'a'
print(d)

d.update({2:'b',3:'c'})
print(d)

d.update({1:'z'})
print(d)

d.setdefault(4,'d')
print(d)

d.setdefault(2,'y')
print(d)

print(d.keys())
print(d.values())
print(d.items())
'''
d = {1: 'z', 2: 'b', 3: 'c', 4: 'd'}
#fetch value
print(d[1])
#print(d[100])

print(d.get(1))
print(d.get(100,0))