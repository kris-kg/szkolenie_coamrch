class Kolor:

    paleta = "paleta X"

    #opis stanu - konstruktor

    def __init__(costam,id,nazwa):
        costam.id = id
        costam.nazwakoloru = nazwa

    #działanie  - funkcje klasy - metody

    def print_kolor(costam):
        print(f"id koloru: {costam.id}, nazwa: {costam.nazwakoloru}, paleta: {costam.paleta}")

k1 = Kolor(1,"czerwony")
k2 = Kolor(22,"grafitowy")


k1.paleta = "Paleta C"
k1.print_kolor()


k2.print_kolor()
