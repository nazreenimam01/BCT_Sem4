a=int(input("Enter a number="))
r=(lambda a:1 if a==0 else a*r(a-1))
print("Factorial=",r(a))
