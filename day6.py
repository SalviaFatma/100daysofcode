#Python – Join Tuples if similar initial element
t1 = ( 1,2,3,4,5 )
t2 = ( 5,2,3,4,5 )
if t1[0] == t2[0] :
    t=t1+t2
    print(t)
else : print("Not similar initial element\n")


