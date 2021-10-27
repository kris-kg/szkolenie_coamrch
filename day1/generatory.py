def liczby():
    for i in range(11):
        yield i*2

for parzysta in liczby():
    print(parzysta)


def operacje():
    print("wstrzymania działania...")
    yield 1
    print("wznowienie działania .... ")

    print("wstrzymania działania...")
    yield 2
    print("wznowienie działania .... ")

for i in operacje():
    print(f"wartość: {i}")


#kolejna funkcja, zakomentowanie wielu linii CTRL + /
"""
komentarz dokumentacyjny
wiele linii
"""

def ret():
    for i in range(5):
        if i==3:
            return
        else:
            yield i


for x in ret():
    print(x)


def gen():
    x=0
    while True:
        y = yield x
        if y is None:
            x = x+1
        else:
            x = y
print("____________________________________________")
g = gen()
print(next(g))
print(next(g))
print(next(g))

print(g.send(12))
print(next(g))
print(next(g))