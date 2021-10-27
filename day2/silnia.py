#n! = 1*2*3*...*n
#double 10**308
# b:float = 10.00**340
# print(b)
#
# c:int = 10**340
# print(c)

def silnia(n):
    if n<0:
        raise ValueError("silnia niezdefiniowana dla liczb ujmenych")
    wynik = 1
    for i in range(1,n+1):
        wynik *= i
    return wynik

def silnia_rek(n):
    if n < 0:
        raise ValueError("silnia niezdefiniowana dla liczb ujmenych")
    if n == 0:
        return 1
    else:
        return n*silnia_rek(n-1)

try:
    n = int(input("Podaj wartość argumentu n silnii: "))
    print(f"silnia z n={n} wynosi: {silnia(n)}")
    print(f"silnia rekurencyjna z n={n} wynosi: {silnia_rek(n)}")
except ValueError as e:
    print(e)
# except:
#     print("nieznany błąd")
