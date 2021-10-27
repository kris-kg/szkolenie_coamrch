def witaj():
    print("witaj użytkowniku")
    print("zaloguj się")
    print("zapłać...")

witaj()

for _ in range(1,21):
    witaj()

def obywatel(nrtelefonu,kraj="Polska"):
    print(f"pochodzę z kraju: {kraj}, telefon: {nrtelefonu}")


obywatel(34534534,"Rosja")
obywatel(345345345,"Rumunia")
obywatel(345345435,"Hiszpania")
obywatel(3453454)

f = 1
def obliczenie(a,b,x):
    f = (a+b)*x - a*b
    return f


print(obliczenie(3,6,7))
print(obliczenie(1.33,6.4,9.9))
print(f)

x = "globalne"
def zwrot():
    global x
    x = x*2
    print(x)

zwrot()

def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print(f"inner: {x}")
    inner()
    print(f"outer: {x}")

outer()

def fx(x,y,z,u):
    return obliczenie(u,z,y)+4*x

print(fx(4,1,22,3))
print(fx(8.8,1,1.222222,3))
