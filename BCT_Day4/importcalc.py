import calculator

def main():
  while True:
    print("Select operation:")
    print("1.ADD")
    print("2.SUBTRACT")
    print("3.MULTIPLY")
    print("4.DIVIDE")
    print("5.QUOTIENT")
    c=int(input("Enter your choice:"))
    a=int(input("Enter number 1:"))
    b=int(input("Enter number 2:"))
    if c==1:
        print(a,"+",b,"=",calculator.add(a,b))
    elif c==2:
        print(a,"-",b,"=",calculator.subtract(a,b))
    elif c==3:
        print(a,"*",b,"=",calculator.multiply(a,b))
    elif c==4:
        print(a,"/",b,"=",calculator.divide(a,b))
    elif c==5:
        print(a,"//",b,"=",calculator.quotient(a,b))
    else:
        print("Choose Valid Operation.")
    next=str(input("Do you want to do next calculation? (Yes/No):"))
    if(next.lower()=="yes"):
        continue
    else:
        break
if __name__=="__main__":
   main()
