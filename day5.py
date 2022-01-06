#Python program to Find the size of a Tuple
t = (1,2,3,4,5,6,7)
print("Size of tuple :",len(t))

#Python – Maximum and Minimum K elements in Tuple
k = int(input("Enter the k :"))
t = list(t)
t.sort(reverse=True)
print(t)
print("Max :",t[k-1])
t.sort()
print(t)
print("Min :",t[k-1])

#Create a list of tuples from given list having number and its cube in each tuple
l = [ 1, 2, 3, 4, 5 ]
l = [(i,pow(i,3)) for i in l ]
print(l)

#Python – Adding Tuple to List and vice – versa
l1 = [1,2,3,4,5]
t1 = (6,7,8,9,0)
l1 += t1
print(l1)



