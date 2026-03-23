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
'''
a=[10,20,87,15,98,12,3,2,45,100]
print(max(a))

s=input("Enter a string")
if s == "".join(reversed(s)):
    print("palindrome")
else:
    print("Not Palindrome")

#3) Count Even Numbers (Using filter()) 
a=[10,20,87,15,98,12,3,2,45,100]
res=list(filter(lambda x:x%2 ==0 ,a))
print(res)
print(len(res))

#4) Remove Duplicates (Using set())
a=[10,20,87,15,98,12,3,2,45,100,1,2,10]
print(set(a))

#5) Sum of Digits (Using sum())
n=12345
res=sum(int(digit) for digit in str(n))
print(res)

#6) Sort Words Alphabetically (Using sorted()) 
a=["kalyani",'sai','ram','Apple']
print(sorted(a))

#7) Find Common Elements (Using set())
a=[1,2,3,3,45,5]
b=[2,3,3,4,5,10]
res=set(a) & set(b)
print(res)
print(tuple(res))

#8) Index with Value (Using enumerate()) 
a=["kalyani",'sai','ram','Apple']
for index,val in enumerate(a):
    print(index,val)

#9) Pair Two Lists (Using zip()) 
a=[1,23,45,6,7]
b=[2,8,5,9,4,5]
print(zip(a,b))

#10) Find Second Largest Number (Using sorted())  
b=[2,8,5,9,4,5]
b.sort()
print(a[-2])