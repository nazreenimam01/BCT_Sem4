num=int(input("Enter a number= "))
n1=0
n2=1
c=0
print(n1)
print(n2)
while c<num-2:
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3
    c+=1

