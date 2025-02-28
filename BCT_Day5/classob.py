class Test:
    i = 10

    def __init__(self):
        print("init")

    def f1(self):
        print("Hello")

print(Test.i)
t1 = Test()
t2 = Test()
t3 = Test()
t1.f1()
Test().f1()
