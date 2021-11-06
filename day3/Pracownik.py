class Pracownik:

    def __init__(self,imie,wiek):
        self.imie = imie
        self.wiek = wiek

    def dane_prac(self):
        print(f"imię pracownika: {self.imie}, wiek: {self.wiek}")

class Sportowiec:

    def __init__(self,dysc,lata):
        self.dysc = dysc
        self.lata = lata

    def infosport(self):
        print(f"sport - dyscyplina: {self.dysc}, lata uprawiania: {self.lata}")


class Dane:

    def __init__(self,adres,zarobki,prac_obj,sport_obj):
        self.adres = adres
        self.zarobki = zarobki
        self.prac_obj = prac_obj
        self.sport_obj = sport_obj

    def display_pracownik(self):
        self.prac_obj.dane_prac()
        self.sport_obj.infosport()
        print(f"adres:{self.adres}, zarobek: {self.zarobki}")


p = Pracownik("Olga",24)
s = Sportowiec("piłka nożna",5)
daneprac = Dane("Kraków, Złota 4",4500,p,s)

#rozszerz konstruktor klasy Dane o obiekt nowej klasy Sportowiec(dysc, lata) z metodą info_sport
#poszerz działanie metody display_pracownik o dane sportowe

daneprac.display_pracownik()

