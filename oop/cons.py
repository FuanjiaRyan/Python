class abc:

    def __new__(cls):
        print("constructor called")
        return super(abc, cls).__new__(cls)

    def __init__(self):
        print("init called")

    def show(self):
        print("in show")

obj1 = abc()
obj1.show()

obj2 = abc.__new__(abc)
obj2.__init__()
obj2.show()