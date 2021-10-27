import sys

try:
    f = open("waznedane.txt","r")
    s = f.readline()
    i = int(s.strip())
    raise Exception(d = i/0)
    #d = i/0
except OSError as err:
    print(f"błąd systemowy: {format(err)}")
except ValueError:
    print("nie można przekonwertować str na int")
except Exception as exx:
    print('prawdopodobnie dzielenie przez 0',type(exx))
    print(exx.args)
    print(exx)
except:
    print(f"nieoczekiwany błąd! {sys.exc_info()[0]}")
    raise