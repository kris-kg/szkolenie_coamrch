class Osoba:

    koloroczu = "niebieski"

    def __init__(self,imie,wiek):
        self.imie = imie
        self.wiek = wiek
        self.info()


    def info(self):
        print("tworzenie nowej osoby....")

    def print_osoba(self):
        print(f"osoba - imię:{self.imie}, wiek: {self.wiek}")

    def wiekza10lat(self):
        return self.wiek + 10

    def czypracownik(self):
        return False

print("*******************************************************")
p1 = Osoba("Jan",32)
p1.koloroczu = "piwne"
print(f"kolor oczu: {p1.koloroczu}")
p1.print_osoba()
print(f"liczba lat za dekadę: {p1.wiekza10lat()} lat/a")
print(f"czy osoba jest pracownikiem? {p1.czypracownik()}")
print("*******************************************************")

p2 = Osoba("Olga",21)
print(f"kolor oczu: {p2.koloroczu}")
p2.print_osoba()
print(f"liczba lat za dekadę: {p2.wiekza10lat()} lat/a")
print(f"czy osoba jest pracownikiem? {p2.czypracownik()}")
print("*******************************************************")

class Pracownik(Osoba):

    def __init__(self,imie,wiek,firma,stanowisko):
        super().__init__(imie,wiek)
        self.firma = firma
        self.stanowisko = stanowisko

    def czypracownik(self):
        return True




e1 = Pracownik("Leon",45,"ABC","dyrektor")
e1.print_osoba()
print(f"wiek za 10 lat: {e1.wiekza10lat()}")
print(f"czy osoba jest pracownikiem? {e1.czypracownik()}")


class Sport:

    def __init__(self,dyscyplina, best_wynik, czas):
        self.dyscyplina = dyscyplina
        self.best_wynik = best_wynik
        self.czas = czas

    def info_sport(self):
        return f"dyscyplina: {self.dyscyplina}, czas uprawiania: {self.czas} lat, życiówka: {self.best_wynik}"

class Ekstra:
    pass


class Student(Pracownik,Sport,Ekstra):

    def __init__(self,imie,wiek,student_id,kierunek,rok_ukon,firma="",stanowisko="",dyscyplina="",
                 best_wynik="", czas=""):
        Pracownik.__init__(self,imie,wiek,firma,stanowisko)
        Sport.__init__(self,dyscyplina, best_wynik, czas)
        self.student_id = student_id
        self.kierunek = kierunek
        self.rok_ukon = rok_ukon


    def print_student(self):
        print(f"infromacja o studencie nr {self.student_id}, kierunek: {self.kierunek}, "
              f"roku ukończenia: {self.rok_ukon}")

    def czypracownik(self):
        if self.firma == "":
            return False
        else:
            return True

print("*******************************************************")
s1 = Student("Olaf",22,345345,"budowalny",2023)
s1.print_osoba()
s1.print_student()
print(f"liczba lat za dekadę: {s1.wiekza10lat()} lat/a")
print(f"czy osoba jest pracownikiem? {s1.czypracownik()}")
print("*******************************************************")

s2 = Student("Ala",22,65757,"informatyka",2023,"Krzak SA","junior developer")
s2.print_osoba()
s2.print_student()
print(f"liczba lat za dekadę: {s2.wiekza10lat()} lat/a")
print(f"czy osoba jest pracownikiem? {s2.czypracownik()}")
print("*******************************************************")
s3 = Student("Piotr",21,734664,"socjologia",2024,dyscyplina="ultra biegi",
             best_wynik="102km 16h 34m 12s",czas=5)
s3.print_osoba()
s3.print_student()
print(f"liczba lat za dekadę: {s3.wiekza10lat()} lat/a")
print(f"czy osoba jest pracownikiem? {s3.czypracownik()}")
print(s3.info_sport())
print("*******************************************************")





