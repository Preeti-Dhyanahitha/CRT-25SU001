'''
Strings:
   1) String Creation
   2) Accessing Characters
   3) Slicing
   4) Immutable
   5) Concatenation
   6) String Repetition
   7) String Functions(len(),upper(),lower(),strip(),replace(),split())
   8) Membership Operator
   9) Programs:
        1. Reverse a string
        2. Palindrome or not
        3. Anagram

#string is a collection of characters enclosed in quotes
#string is immutable

s = 'python'
s1 = "Python"
s2 = """
python
is 
interesing"""
print(s + s1)#concatenation
print(s1 * 2)#Repitition
print("on" in s1)

s[1] = 'z'

# Built-in functions
s = 'python'
print(len(s))
print(max(s))
print(min(s))
print(max("abc123ABC"))

#Built-in methods

s = "python"
s = s.replace("y",'Y')
print(s)

#print(dir(str))
print(s.find("on"))
print(s.find("xyz"))

#Reverse a string without using slice range
s = input()
res = ""
stop = -1 * (len(s)+1)
for i in range(-1,stop,-1):
    res += s[i]
print(res)

rev = ""
for i in s:
    rev = i + rev
print(rev)

print("palindrome" if s == rev else "not palindrome")
'''
from collections import Counter
s1 = input()
s2 = input()
#print(Counter(s1))
print("Anagrams" if Counter(s1) == Counter(s2) else "not Anagrams")