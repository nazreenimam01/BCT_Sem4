class Test:
    def __init__(self):
        self.a = 10
        self.b = 20
    def f1(self):
        print("Hello")

t1 = Test()
t2 = Test()
t3 = Test()
t1.f1()
Test().f1()
print(t1.a, t1.b)
print(t2.a, t2.b)
print(t3.a, t3.b)