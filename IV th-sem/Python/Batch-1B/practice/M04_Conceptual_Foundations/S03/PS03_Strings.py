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

s = "python programming"
print(s.capitalize())
print(s.title())
s = s.title()
print(s)

print(s.replace("on","ON"))
print(s)

# Reverse a string without using Built-in functions & slice
# input : "abc"  ==> output : "cba"

def Reverse_string(s):
    stop = -1 * (len(s)+1)
    res = ""
    for i in range(-1,stop,-1):
        res += s[i]
    return res

print(Reverse_string("abc"))


s = "abc"
print("".join(reversed(s)))

def Reverse_string1(s):
    res = ""
    for ch in s:
        res = ch + res
    return res

def is_palindrome(s):
    return Reverse_string1(s) == s

print(is_palindrome("abc"))
print(is_palindrome("madam"))
'''
def frequency_count(s):
    d = {}
    for ch in s:
        if ch not in d:
            d[ch] = 1
        else:
            d[ch] += 1
    return d

def Anagrams(s1,s2):
    return frequency_count(s1) == frequency_count(s2)

print(Anagrams("paces","space")) #True
print(Anagrams("abc","aabbcc")) #False

import collections
print(collections.Counter("aabbcc"))

def Anagrams1(s1,s2):
    return collections.Counter(s1) == collections.Counter(s2)

print(Anagrams1("paces","space")) #True
print(Anagrams1("abc","aabbcc")) #False

# input : "orange" ==>
#output : "puboif"

# advika ==> beajob