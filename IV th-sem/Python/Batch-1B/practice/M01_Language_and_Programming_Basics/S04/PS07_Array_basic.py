'''
import array
arr = array.array('i',[])
print(arr,type(arr))
arr.append(10)
arr.append(20)
print(arr)
arr.append(12.45)
'''
'''
List:
1. use [] to create  a list
2. List is Mutable
3. List allows duplicate values
4. List is heterogenous
5. List is indexed 
'''
li = [12,25.4,6+5j,"Hello",12,25.4]
print(li,type(li))
print(li[3])
print(li[3:6:1])
print(li[::-1])
print(len(li))
li.append(100)
print(li) 
li.insert(2,"World")
print(li)
li.insert(-20,"python")
print(li)

# Read a number from the user and display no.of digits in that number
input : 1234
output : 4 
