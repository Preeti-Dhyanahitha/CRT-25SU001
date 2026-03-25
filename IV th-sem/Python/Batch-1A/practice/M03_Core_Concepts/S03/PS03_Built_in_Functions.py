'''
1) Find Largest Number (Using max())
2) Check Palindrome (Using reversed() & join())   
3) Count Even Numbers (Using filter())   
4) Remove Duplicates (Using set())   
5) Sum of Digits (Using sum())   
6) Sort Words Alphabetically (Using sorted())    
7) Find Common Elements (Using set())
8) Index with Value (Using enumerate())  
9) Pair Two Lists (Using zip())    
10) Find Second Largest Number (Using sorted())   


#1) Find Largest Number (Using max())
#input : [12,78,32,54,69,100]
# output : 100
li = list(map(int,input().split()))
max_num = li[0]
for ele in li:
    if ele > max_num:
        max_num = ele
print(max_num)
print(max(li))
print(min(li))

#Check Palindrome (Using reversed() & join())
s = input()
print("palindorme" if s == s[::-1] else "not palindrome")

print("".join(reversed(s)))

print(list(reversed([1,2,3,4,5])))

#Count Even Numbers (Using filter()) 
li = [1,2,3,4,5]
res = list(filter(lambda n : n%2 == 0,li))
print(res)

#Remove Duplicates (Using set())  
li = [1,2,1,3,4,5,1,2,3,4]
print(li)
print(list(set(li)))

#Sum of Digits (Using sum())   
n = int(input())
res = [int(ch) for ch in str(n)]
print(sum(res))

#Sort Words Alphabetically (Using sorted())
li = ['preeti','mujeeb','kalyani','dinesh','suresh']
print(sorted(li))

#Index with Value (Using enumerate()) 
li = ['preeti','mujeeb','kalyani','dinesh','suresh']
for index,value in enumerate(li):
    print(index,"==>",value)

li1 = [1,2,3,4,5]
li2 = [10,20,30,40,50]
#res = [11,22,33,44,55]
res = [li1[i]+li2[i] for i in range(len(li1))]
print(res)

res1 = [x+y for x,y in zip(li1,li2)]
print(res1)
'''
#Find Second Largest Number (Using sorted())  
li = [10,20,30,50,100,50,60,70,100]
print(list(sorted(list(set(li))))[-2])