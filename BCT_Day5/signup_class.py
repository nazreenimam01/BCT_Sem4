from prettytable import PrettyTable
L=[]
class Signupinterface:
    
    def __init__(self,e,p):
         self.email=e               #this makes email global to the entire class
         self.password=p
         self.table=PrettyTable()

    def signup(self):
        if(self.email.endswith("gmail.com")):
            a={"Email:":self.email,"Password:":self.password}
            L.append(a)
            print("SignUp successful.")
            return
        else:
            print("Email format is not valid. Please enter correct email.")
            return

    def check(self):
        for i in range(len(L)):
            if(self.email.endswith("gmail.com")):
                if(L[i]['Email:']==self.email):
                    if(L[i]['Password:']==self.password):
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

class Details:
    table=PrettyTable()

    def show(self):
        self.table.field_names = ["Email", "Password"]
        for i in range(len(L)):
           e=L[i]['Email:']
           p=L[i]['Password:']
           self.table.add_row([e,p])
        print(self.table)
        self.table.clear()


while True:
    c=str(input("Do you want to SignUp? (Yes/No):"))
    if(c.lower()=="yes"):
        email=input("Enter your email:")
        password=input("Enter your password:")
        t1=Signupinterface(email,password)
        t1.signup()
    d=str(input("Do you want to SignIn? (Yes/No):"))
    if(d.lower()=="yes"):
        email1=input("Enter your email:")
        password1=input("Enter your password:")
        t2=Signupinterface(email1,password1)
        t2.check()
    e=str(input("Do you want to see database? (Yes/No):"))
    if(e.lower()=="yes"):
        s=Details()
        s.show()
        