#find area of circle
r=int(input("Enter the radius :"))
print("Area of circle is :",3.14*r*r,"\n")

#print all the prime number in the interval
x=int(input("Enter the opening interval :"))
y=int(input("Enter the closing interval :"))
l=[]
for i in range(x+1,y):
    flag=False
    for j in range(2,i):
        if i%j==0:
            flag=True
            break
    if flag==False : l.append(i) 
print(l)

#check number is prime or not
a=int(input("Enter the number :"))
flag=False
for j in range(2,a):
    if a%j==0:
        flag=True
        break
print("Is prime",'\n') if flag==False else print("Is not prime",'\n')

#fibonacci number
b=int(input("Enter the number :"))
first=0
sec=1
if b==1:
    print(first)
elif b==2:
    print(first ,"," ,sec)
else:
    l2=[first,sec]
    for i in range(3,b+1):
        num=first+sec
        l2.append(num)
        first=sec
        sec=num
print(l2)

        


        
