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


#string: Collection of characters enclosed ' ', " ",'''  ''',""" """
s = "python"
print(s[2])
print(s[1:])

print(s.capitalize())
print(s)

#s[0] = 'P'
s = s.replace("p","P")
print(s)

#Reverse a string without using built-in functions and slice operator

st = input()
#Solution-1
res = ""
stop = -1 * (len(st)+1)
for i in range(-1,stop,-1):
    res = res + st[i]
print(res)

#Solution-2
res1 = ""
for ch in st:
    res1 = ch + res1
print(res1)


def Reverse_String(st):
        res1 = ""
        for ch in st:
                res1 = ch + res1
        return res1

def is_palindrome(st):
        return st == Reverse_String(st)

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

#print(frequency_count("abcabc")) # {'a':2,'b':2,'c':2}

def is_Anagarams(st1,st2):
        return frequency_count(st1) == frequency_count(st2)

print(is_Anagarams("space","paces")) #True
print(is_Anagarams("abc","abcabc")) #False