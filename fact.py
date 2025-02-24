num=int(input("Enter a number= "))
c=1
for i in range(1,num+1):
    c*=i
    i+=1
print("Factorial of",num,"=",c)