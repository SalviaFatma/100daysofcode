#Python Program to find sum of array
arr = [1,2,3,4,5]
sum1 =0
for i in arr:
    sum1+=sum1+1
print("Sum of Array :",sum1)

#Python Program to find largest element in an array
max1 = arr[0]
for i in range(1,len(arr)):
    if arr[i]>max1 :
        max1 = arr[i]
print("Maximum Value :",max1)

