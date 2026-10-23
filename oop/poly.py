class Laptop:  ##Duck
    def build(self):
        print("Laptop builds")

class Desktop:
    def build(self):
        print("Desktop Builds")

class Tablet:
    def open_pdf(self):
        print("Opening PDF")

class Alien:
    def code(self, machine : Laptop):
        print("Alien Building...")
        machine.build()

UOWAMOU = Laptop()
beast = Desktop()
lenovo_tab = Tablet()

Ryan = Alien()
# Ryan.code(UOWAMOU)
# Ryan.code(beast)
Ryan.code(lenovo_tab)