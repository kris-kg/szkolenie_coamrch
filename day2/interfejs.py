from abc import ABCMeta, abstractmethod

class IPojazd:

    __metaclass__ = ABCMeta

    @abstractmethod
    def spalanie(self,spal):raise NotImplementedError

    @abstractmethod
    def kosztprzejazdu(self,spal,odl,cena_l):raise NotImplementedError


class Pojazd(IPojazd):

    def spalanie(self, spal):
        return spal

    def kosztprzejazdu(self, spal, odl, cena_l):
        return self.spalanie(spal)*odl/100*cena_l

p1 = Pojazd()
print(p1.spalanie(8.9))
print(p1.kosztprzejazdu(8.9,761,6.12))