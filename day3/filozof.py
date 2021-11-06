pytanie = input("Czy Ziemia jest płaska? Chcesz znać odpowiedź? (t/n)")
if pytanie.lower() == "t":
    required = True
else:
    required = False

def odpowiedz(self,*args):
    return "tak, Ziemia jest płaska."

def odpowiedz_new(self,*args):
    return "Nie! Ziemia jest okrągła."

#definicja metaklasy

class SednoOdpowiedzi(type):

    def __init__(cls,clsname,superclasses,attribdict):
        if required:
            cls.odpowiedz = odpowiedz
            cls.odpowiedz_new = odpowiedz_new

class Arystoteles(metaclass=SednoOdpowiedzi):
    pass

class Platon(metaclass=SednoOdpowiedzi):
    pass

class SwTomasz(metaclass=SednoOdpowiedzi):
    pass

class Kopernik(metaclass=SednoOdpowiedzi):
    pass

fil1 = Arystoteles()
print(fil1.odpowiedz())

fil2 = Platon()
print(fil2.odpowiedz())

fil3 = SwTomasz()
print(fil3.odpowiedz())

#stwórz obiekt klasy Kopernik i zmodyfikuje działanie metody odpowiedz()
# tak żeby zwracała informację: "Nie! Ziemia jest okrągła."

fil4 = Kopernik()
print(fil4.odpowiedz_new())