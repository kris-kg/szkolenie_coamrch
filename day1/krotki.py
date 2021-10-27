animal = ("pies", "kot", "papuga", "pies", "papuga")

print(animal)
print(animal.count("pies"))

for a in animal:
    print(a)

if "papuga" in animal:
    print("tak! papuga to ptak.")

if "budynek" in animal:
    print("to błąd!")

anim2 = ("pająk","ryba")
animal = animal + anim2
print(animal)

mojakrotka = tuple(("obekt45",23,45,0.0003,True))

print(mojakrotka)
mojalista = list(mojakrotka)
print(mojalista)
mojalista.remove(45)
mojalista.append(100)
print(mojalista)

mojakrotka = tuple(mojalista)
print(mojakrotka)

auto1 = ('audiQ7',3.8,2019)
(marka,poj,rok) = auto1
print(marka)
print(poj)
print(rok)