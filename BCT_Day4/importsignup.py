import signup_modify
def main():
    while True:
       c=str(input("Do you want to SignUp? (Yes/No):"))
       if(c.lower()=="yes"):
          signup_modify.signup()
       d=str(input("Do you want to SignIn? (Yes/No):"))
       if(d.lower()=="yes"):
          signup_modify.check()
       e=str(input("Do you want to see database? (Yes/No):"))
       if(e.lower()=="yes"):
          signup_modify.show()

if __name__=="__main__":
    main()