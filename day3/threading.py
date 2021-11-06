import threading

def print_cube(n):
    #while True:
    print(f"sześcian:{n**3}")

def print_square(n):
    #while True:
    print(f"kwadrat: {n**2}")

if __name__ == "__main__":
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))


    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('wykonano!')