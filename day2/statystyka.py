liczby = [56,878,23,-998,0,45,24,5665,-1002,56,367,1232,56,-989]

def pokaz_stat(lista):
    minimum = min(lista)
    maksimum = max(lista)
    zakres = maksimum - minimum
    return minimum, maksimum, zakres

wynik = pokaz_stat(liczby)
print(wynik)
mini,maxi,zakr = pokaz_stat(liczby)
print(f"wartość maksymalna: {maxi}, wartość minimalna: {mini}, zakres wynosi {zakr}")