class Singleton(type):
    instance = None
    def __call__(cls, *args, **kw):
        if not cls.instance:
             cls.instance = super(Singleton, cls).__call__(*args, **kw)
        return cls.instance

class ASingleton(metaclass=Singleton):
    pass
a = ASingleton()
b = ASingleton()
a is b

print(hex(id(a)))

print(hex(id(b)))