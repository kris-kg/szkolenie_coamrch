import csv

with open("firma.csv",encoding='utf-8') as pc:
    csv_reader = csv.reader(pc,delimiter=";")
    licznik_linii = 0
    for wiersz in csv_reader:
        if licznik_linii == 0:
            print(f'nazwa kolumny: {", ".join(wiersz)}')

        else:
            print(f'\t{wiersz[0]} pracuje na stanowisku: {wiersz[1]} i ma urodziny'
                  f'w miesiącu {wiersz[2]}, otrzymuje nagrodę w wysokości: {wiersz[3]} zł')
        licznik_linii += 1

    print(f'wczytano {licznik_linii} linii')
    print(f'wczytano {licznik_linii-1} osób')