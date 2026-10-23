class A:
    def show(self):
        print("in a show")

class B(A):
    def show(self):
        print("in b show")

obj1 = B()
obj1.show()