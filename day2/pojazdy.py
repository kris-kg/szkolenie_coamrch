from abc import ABC, abstractmethod


class Pojazd(ABC):

    @abstractmethod
    def pokaz_naped(self):
        pass

    @abstractmethod
    def predkosc_max(self):
        pass


class Silnik:

    def __init__(self, rodzaj, poj):
        self.rodzaj = rodzaj
        self.poj = poj


class Marka:

    def __init__(self, nazwa, typ, rocznik):
        self.nazwa = nazwa
        self.typ = typ
        self.rocznik = rocznik


class Rower(Pojazd, Marka):

    def __init__(self, nazwa, typ, rocznik):
        Marka.__init__(self, nazwa, typ, rocznik)

    def pokaz_naped(self):
        return "korba"

    def predkosc_max(self):
        return 60

    def opis_roweru(self):
        print("Rower marki: {}, napęd: {}, prędkość maksymalna: {}".format(
            self.nazwa, self.pokaz_naped(), self.predkosc_max()))


class Osobowy(Pojazd, Silnik, Marka):

    def __init__(self, rodzaj, poj, nazwa, typ, rocznik):
        Silnik.__init__(self, rodzaj, poj)
        Marka.__init__(self, nazwa, typ, rocznik)

    def pokaz_naped(self):
        return "silnik"

    def predkosc_max(self):
        if self.poj <= 1.0:
            return 140
        elif self.poj <= 1.5:
            return 170
        elif self.poj <= 1.8:
            return 190
        elif self.poj <= 2.2:
            return 210
        elif self.poj <= 3.0:
            return 240
        else:
            return "prędkość większa niż 240"

    def opis_auta(self):
        print("Samochód marki: {}, typ: {}, z roku: {}, pojemność {}, rodzaj silnika: {}".format(
            self.nazwa, self.typ, self.rocznik, self.poj, self.rodzaj))



r = Rower("Trek","Madone",2019)
r.opis_roweru()
print("napęd roweru to {}".format(r.pokaz_naped()))
print("prędkość maksymalna  = {} km/h".format(r.predkosc_max()))

print("___________________________________________________\n")

sam1 = Osobowy("hybyryda",2.2,"Toyota","Avensis",2018)
print("napęd samochodu to {}".format(sam1.pokaz_naped()))
print("prędkość maksymalna  = {} km/h".format(sam1.predkosc_max()))
sam1.opis_auta()