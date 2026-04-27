#Frequency of each element in the array
#[1,2,4,5,2,3,1,1] ==> {1:3,2:2,3:1,4:1,5:1}
li = list(map(int,input().split()))
d = {}
for ele in li:
    if ele not in d:
        d[ele] = 1
    else:
        d[ele] += 1
print(d)

d1 = {}
for ele in li:
    d1[ele] = d1.get(ele,0) + 1
print(d1)

#Find the element with max frequency
#[1,2,4,5,2,3,1,1] ==> 1
from collections import Counter
li = list(map(int,input().split()))
freq = dict(Counter(li))
print(max(freq,key=freq.get))