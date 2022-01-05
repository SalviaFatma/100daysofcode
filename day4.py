#Python program to find N largest elements from a list
l = [4,5,6,1,8,4,9,0,3,6]
l = list(set(l))
print("List is :",l)
l.sort(reverse = True)
print(l)
n = int(input("Enter the nth number :"))
print("Nth largest number :",l[n-1],"\n") if n <= len(l) else print("Index number out of bound","\n")

#Python program to print even and odd numbers in a list
even = []
odd = []
for i in range(0,len(l)-1):
    if l[i]%2 == 0:
        even.append(l[i])
    else:
        odd.append(l[i])
print("Even :",even,"\n")
print("Odd :",odd,"\n")

#Remove multiple elements from a list in Python
l1 = [2,4,1,6,9,4,0,1,5,344,7,3,8,9]
print("list :",l1)
del l1 [3:7]
print("After deletion :",l1,"\n")

#Python – Remove empty List from List
lists = [[1,2,3],[],[4],[],[6,7,8]]
print("list :",lists)
lists = list(filter(None , lists))
print("List after removal :",lists,"\n")
    
#Python | Cloning or Copying a list
new = l.copy()
print("List after copying :",new,"\n")

#Python | Count occurrences of an element in a list
l2 = [1,1,1,2,3,4,4,5]
print(l2)
m = int(input("Enter the number whose ocurrence to be found :"))
print("Ocurrence :",l2.count(m))

