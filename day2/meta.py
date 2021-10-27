class MojaMeta(type):

    def __new__(cls, clsname, superclasses, attributedict):
        print(f"nazwa klasy: {clsname}")
        print(f"dziedziczone klasy: {superclasses}")
        print(f"zbiór atrybutów: {attributedict}")
        return type.__new__(cls, clsname, superclasses, attributedict)

class S:
    pass

class A(S, metaclass=MojaMeta):
    pass

class F:
    pass

class B(A,F):
    pass

a = A()
b = B()