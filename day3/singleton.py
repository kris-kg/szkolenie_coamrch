class Singleton(type):
    instance = None
    def __call__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(Singleton,cls).__call__(*args, **kwargs)
        return cls.instance


class ZwSing(metaclass=Singleton):
    pass

a = ZwSing()
b = ZwSing()

assert  a is b

print(hex(id(a)))
print(hex(id(b)))