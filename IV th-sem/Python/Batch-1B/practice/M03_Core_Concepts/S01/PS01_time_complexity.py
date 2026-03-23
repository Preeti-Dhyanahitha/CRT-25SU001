#O(1) ==> constant time complexity
li = [10,20,30,40,50]
print(li[2])

li.append(60)

li.insert(0,100)

n = int(input())
for i in range(n):
    for j in range(n):
        print(i,j,end=" ")

def Linear_search(li,target):
    for i in range(len(li)):
        if li[i] == target:
            return i
    return -1

Linear_search([12,45,78,69,32,45],12)
Linear_search([12,45,78,69,32,45],78)
Linear_search([12,45,78,69,32,45],45)
Linear_search([12,45,78,69,32,45],100)