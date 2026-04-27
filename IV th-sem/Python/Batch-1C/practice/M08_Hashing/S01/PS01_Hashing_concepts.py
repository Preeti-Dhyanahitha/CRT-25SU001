#Set ==> dulicates are not allowed
s = set()
print(type(s))

#Dictionary:
d = {}
#Adding entries
d[1] = 'a'
d.update({2:'b',3:'c'})
d.setdefault(4,'d')

#Fetch the value
d.get(3)
d.get(100,0)

d.keys()
d.values()
d.items()