class Component:

    def __init__(self):
        print("Stworzenie komponentu")

    def mcomp(self):
        print("Metoda klasy Component")

class Composite:

    def __init__(self):
        self.com1 = Component()
        print("Został stworzony obiekt klasy Component")

    def mcompos(self):
        print("Metoda mcompos uruchomiona")
        self.com1.mcomp()


pr = Composite()
pr.mcompos()
pr.com1.mcomp()