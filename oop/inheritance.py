class A:

    def __init__(self):
        print("in A init")

    def f1(self):
        print("F1 works")

class B(A):
    def __init__(self):
        super().__init__()
        print("in B init")

    def f2(self):
        self.f1()
        print("F2 works")

obj1 = B()
obj1.f2()




