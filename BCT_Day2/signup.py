L=[]
def signup():
    email=input("Enter your email:")
    password=input("Enter your password:")
    a={"Email:":email,"Password:":password}
    L.append(a)
    print("SignUp successful.")
    print(L)
    return

def check():
    em=input("Enter your email:")
    p=input("Enter your password:")
    for i in range(len(L)):
        if L[i]['Email:']==em:
            if L[i]['Password:']==p:
                print("Login successful.")
                return 
            else:
                print("Incorrect password.")
                return
        
    print("Email is not registered, please SignUp first.")
    return
           
def main():
    while True:
        c=str(input("Do you want to SignUp? (Yes/No):"))
        if(c.lower()=="yes"):
            signup()
        d=str(input("Do you want to SignIn? (Yes/No):"))
        if(d.lower()=="yes"):
            check()

if __name__=="__main__":
    main()
