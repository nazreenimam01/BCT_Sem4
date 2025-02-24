num=int(input("Enter a number= "))
sum=0
temp=num
l=len(str(num))
print("Length=",l)
while temp>0:
    digit=temp%10
    sum=sum+(digit*(10**(l-1)))
    temp=temp//10
    l-=1
if num==sum:
    print(num, "is a pallindrome number")
else:
    print(num, "is not a pallindrome number")

