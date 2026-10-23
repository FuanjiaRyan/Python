class A:
    def f1(self):
        print("F1 works")

    def f2(self):
        print("F2 works")

    def show(self):
        print("in A show")

class B:
    def f3(self):
        print("F3 works")

    def f4(self):
        print("F4 works")

    def show(self):
        print("in B show")

class C(A,B):
    def f5(self):
        print("F5 works")

    # def show(self):
    #     print("in C show")

obj1 = C()

B.show(obj1)

# obj1.show()




