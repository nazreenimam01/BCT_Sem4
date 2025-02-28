a=int(input("Enter first number="))
b=int(input("Enter second number="))
try:
    z=a/b
    print("Division result=",z)
except Exception as e:
    print(e)
print("This is the last line.")