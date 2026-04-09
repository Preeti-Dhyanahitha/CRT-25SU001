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
'''
#String ==> Immutable ==> '  ' or "  " single line string
#''' ''' or """ """ ==> multi-line string

s = "python"
s = s.capitalize()
print(s)

#Reverse a string without using Built-in functions and [::-1]
def Reverse_str(s):
    res = ""
    for ch in s:
        res = ch + res
    return res 

print(Reverse_str("abc"))#"cba"
print(Reverse_str("python"))#"nohtyp"

def Reverse_str1(s):
    res = ""
    stop = -1 * (len(s)+1)
    for i in range(-1,stop,-1):
        res = res + s[i]
    return res 

print(Reverse_str1("abc"))#"cba"
print(Reverse_str1("python"))#"nohtyp"

def is_palindrome(s):
    return s == Reverse_str1(s)

print(is_palindrome("abc")) #False
print(is_palindrome("madam")) #True

#check whether the given strings are Anagrams or not
def Frequency_count(s):
    d = {}
    for ch in s:
        if ch not in d:
            d[ch] = 1
        else:
            d[ch] += 1
    return d

#print(Frequency_count("abcabc"))# {'a':2,'b':2,'c':2}

def Anagrams(str1,str2):
    return Frequency_count(str1) == Frequency_count(str2)

print(Anagrams("paces","space"))#True
print(Anagrams("aabbcc","abc"))#False

from collections import Counter
print(Counter("aabbcc"))