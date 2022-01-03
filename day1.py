#program to add two number
a=int(input("Enter the first number :"))
b=int(input("Enter the second number :"))
print("Sum :",a+b,"\n")

#maximum of two numbers
a1=int(input("Enter the first number :"))
b1=int(input("Enter the second number :"))
print(max(a1,b1),"\n")

#find factorial of number
a2=int(input("Enter the number :"))
fact=1
for i in range(1,a2+1):
    fact=fact*i
print("Factorial is :",fact,"\n")

#Simple interest
a3=int(input("Enter the principle amount :"))
b3=int(input("Enter the time :"))
c3=int(input("Enter the I :"))
print("Simple interest :",a3*b3*c3,"\n")

#Armstrong number
a4=int(input("Enter the number :"))
m=n=a4
j=0
while n>0:
    n=n//10
    j=j+1
num=0
while m>0:
    r=m%10
    num=num+r**j
    m=m//10
print("Yes,Armstrong number","\n") if num==a4 else print("No","\n")

