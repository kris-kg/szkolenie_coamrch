from abc import ABC, abstractmethod
import math

class Figura(ABC):

    def __init__(self,a,b):
        self.a = a
        self.b = b

    @abstractmethod
    def policz_pole(self):
        pass



class Prostokat(Figura):

    def policz_pole(self):
        return self.a*self.b

class Trojkat(Figura):

    def policz_pole(self):
        return self.a*self.b/2


pr = Prostokat(4.5,5.7)
tr = Trojkat(6,5.3)

print(f"pole prostokąta: {pr.policz_pole():.2f}")
print(f"pole trójkąta: {tr.policz_pole():.2f}")

class Trapez(Figura):

    def __init__(self,a,b,h):
        super().__init__(a,b)
        self.h = h

    def policz_pole(self):
        return (self.a+self.b)*self.h/2

trp = Trapez(6.1,4.2,4.4)
print(f"pole trzpezu: {trp.policz_pole():.2f}")


class Kolo(Figura):

    def __init__(self,a):
        super().__init__(a,0)

    def policz_pole(self):
        return math.pi*self.a**2


kl = Kolo(5.5)
print(f"pole koła: {kl.policz_pole():.2f}")



