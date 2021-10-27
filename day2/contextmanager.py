class ContextManager():

    def __init__(self):
        print("metoda init (konstruktora)")

    def __enter__(self):
        print("metoda enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("metoda exit")

with ContextManager() as manager:
    print("blok wykonawczy!")