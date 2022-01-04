#Python program to interchange first and last elements in a list
l = [1,2,3,4,5]
print("list ",l)
a = l[0]
l[0] = l[-1]
l[-1] = a
print ( "After exchange " , l ,"\n")

#Python program to swap two elements in a list
l1 = [1,2,3,4,5]
print("list ",l1)
x = int(input( "Enter the index no. to be swapped :" ))
y = int(input( "Enter the index no. to be swapped :" ))
temp = l1[x]
l1[x] = l1[y]
l1[y] = temp
print("After exchange ",l1,"\n")

#Python | Ways to find length of list
print(l)
print("length of list :",len(l),"\n")

#Python | Ways to check if element exists in list
r = input( "Enter the element to be found :" )
l3 = [1,2,"abc",True]
flag = False
for i in range(0,len(l3)):
    if l3[i] == r:
        flag = True
        break
print("found","\n") if flag == True else print("Not found","\n")

#Different ways to clear a list in Python
l4 = [ "a",1,3,0,"bg"]
print("list :",l4)
l4.clear()
print("list after clear :",l4,"\n")

#Python | Reversing a List
list1 = [1,2,3,4,5]
print(list1)
list1.reverse()
print("Reversing the list :",list1,"\n")

#Python program to find sum , mul, small , large of elements in list
print(list1)
sum1 = 0
mul = 1
small = list1[0]
large = list1[0]
for i in range(0,len(list1)):
    sum1 = sum1+list1[i]
    mul = mul * list1[i]
    if list1[i] < small : small = list1[i]
    if list1[i] > large : large = list1[i]
print("sum of list :",sum1,"\nMultiplication of all number :",mul,"\nSmallest number :",small,"\nLargest number :",large)
