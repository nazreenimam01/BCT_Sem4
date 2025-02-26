# PrettyTable and endswith() function is included in the login interface program

from prettytable import PrettyTable
table=PrettyTable()
L=[]
def signup():
    email=input("Enter your email:")
    password=input("Enter your password:")
    if(email.endswith("gmail.com")):
        a={"Email:":email,"Password:":password}
        L.append(a)
        print("SignUp successful.")
        return
    else:
        print("Email format is not valid. Please enter correct email.")
        return

def check():
        em=input("Enter your email:")
        p=input("Enter your password:")
        for i in range(len(L)):
            if(em.endswith("gmail.com")):
               if(L[i]['Email:']==em):
                    if(L[i]['Password:']==p):
                       print("Login successful.")
                       return
                    else:
                       print("Incorrect password.")
                       return
            else:
                print("Email format is not valid. Please enter correct email.")
                return
        print("Email is not registered, please SignUp first.")
        return

def show():
    table.field_names = ["Email", "Password"]
    for i in range(len(L)):
        e=L[i]['Email:']
        p=L[i]['Password:']
        table.add_row([e,p])
    print(table)
    table.clear()


def main():
    while True:
       c=str(input("Do you want to SignUp? (Yes/No):"))
       if(c.lower()=="yes"):
          signup()
       d=str(input("Do you want to SignIn? (Yes/No):"))
       if(d.lower()=="yes"):
          check()
       e=str(input("Do you want to see database? (Yes/No):"))
       if(e.lower()=="yes"):
          show()

if __name__=="__main__":
    main()
