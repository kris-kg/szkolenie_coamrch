owoce = [
    ('awokado',7.99),
    ('cytryna',6.50),
    ('banan',4.99),
    ('winogrono',12.22),
    ('jabłko',3.55)
]

for i,(nazwa,cena) in enumerate(owoce):
    print('#%d: %-10s = %.2f zł' %(i,nazwa,cena))

print("*****************************************")

for i,(nazwa,cena) in enumerate(owoce):
    print('#%d: %-10s = %.2f zł' %(
        i+1,
        nazwa.title(),
        round(cena,1)
    ))

print("*****************************************")
sklep = ['słuchawki Gear','Wieża TECH','przewód FG56']

enu_sklep = enumerate(sklep)
print(type(enu_sklep))

print(list(enu_sklep))

enu2_sklep = enumerate(sklep,10)
print(list(enu2_sklep))
print("*****************************************")

liczby = [1,2,3]
opis = ['one','two','three']
pl = ['jeden','dwa','trzy','cztery']
wynik = zip()
wynik_lista = list(wynik)
print(wynik_lista)

wynik = zip(liczby,opis)
wynik_lista = list(wynik)
print(wynik_lista)

wynik = zip(liczby,opis,pl)
wynik_lista = list(wynik)
print(wynik_lista)