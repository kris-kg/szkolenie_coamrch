try:
    print(x)
except NameError:
    print('x nie istnieje!')
except:
    print('inny błąd')
finally:
    x = 119
    print(x)


print("ciąg dalszy")