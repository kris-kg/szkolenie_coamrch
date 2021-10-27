def filtering(arr,test):
    passed = []
    for element in arr:
        if (test(element)):
            passed.append(element)
    return passed

def isSuperNumber(num):
    return num >= 10

print(filtering([1,5,11,23,4,7,9,17],isSuperNumber))



def mapowanie(arr,transformacja):
    mapa = []
    for element in arr:
        mapa.append(transformacja(element))
    return mapa


def dodajdwa(n):
    return n+2

print(mapowanie([2,5,1,7,9,11,34],dodajdwa))

print("_____________________________________________")

def zamiana(value):
    def wrapper(value):
        return -1*value
    return wrapper

@zamiana
def abs(value):
    return value

print(abs(2))
print(abs(-9))

@zamiana
def policz(value):
    return valuew**2-value

print(policz(2))

@zamiana
def policz(a):
    return

print(policz(2))