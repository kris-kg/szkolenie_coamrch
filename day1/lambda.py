a = 10
print(a)

a = "dziesiątka"
print(a)

x = lambda a:a+10

print(x(4))
print(x(0.04))


y = lambda a,b,c=1:a+b+c

print(y(4,22,5.5))
print(y(4,22))

def multi(n):
    return lambda a:a*n

d = multi(5)
print(d(6))
print(multi(7)(9.9))