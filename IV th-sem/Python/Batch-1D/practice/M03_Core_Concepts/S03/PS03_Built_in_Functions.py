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
a=[1,2,5,8,9,832,15,63]
print(max(a))

#2) Check Palindrome (Using reversed() & join())
s=input("enter a string")
if s == "".join(reversed(s)):
    print("Palindrome")
else:
    print("Not Palindrome")

#3) Count Even Numbers (Using filter())
a=[1,2,5,8,9,832,15,63]
res=list(filter(lambda x:x%2==0,a))
print(res)
print(len(res))

#4) Remove Duplicates (Using set())   
#5) Sum of Digits (Using sum())
n=12345
res=sum(int(digit) for digit in str(n))
print(res)

#6) Sort Words Alphabetically (Using sorted()) 
a=['kalyani','apple','cat','sai']
print(list(sorted(a)))

#7) Find Common Elements (Using set())
a=[1,2,5,8,9,832,15,63]
b=[1,2,5,8,10,12,13]
print(set(a) & set(b))
print(a.intersection(b))

#8) Index with Value (Using enumerate())  
#9) Pair Two Lists (Using zip())    
#10) Find Second Largest Number (Using sorted())