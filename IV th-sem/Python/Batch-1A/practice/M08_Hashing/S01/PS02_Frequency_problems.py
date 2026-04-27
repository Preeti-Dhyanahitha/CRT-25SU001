#Count frequency of each element
#[1,2,4,3,1,2,5] ==> {1:2,2:2,3:1,4:1,5:1}
'''
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

from collections import Counter
print(Counter(li)) 

#Find all distinct elements
#[1,2,4,3,1,2,5] ==> [1,2,3,4,5]

li = list(map(int,input().split()))
s = set()
for ele in li:
    if ele not in s:
        s.add(ele)
print(list(s))
'''
#Find the element with maximum frequency
#[1,2,4,3,1,2,5,1] ==> 1
#single element with max frequency
from collections import Counter
li = list(map(int,input().split()))
freq = dict(Counter(li))
print(max(freq,key=freq.get))

#multiple elements with max frequency
max_freq = max(freq.values())
for k in freq:
    if freq[k] == max_freq:
        print(k)

#Majority element
def majorityElement(nums):
    freq = dict(Counter(nums))
    n = len(nums)
    for key,value in freq.items():
        if value > (n//2):
            return key
