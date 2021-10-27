import json

def zapisz_nowego_prac(new_data,filname = "pracownik.json"):
    with open(filname,"r+") as file:
        file_data = json.load(file)
        file_data["pra_info"].append(new_data)
        file.seek(0)
        json.dump(file_data,file,indent=4)

nowyprac = {
            "imie": "Piotr",
            "nazwisko": "Kot",
            "stanowisko": "programista",
            "lata_pracy": 7,
            "email": "pieter@firma.pl"
        }

zapisz_nowego_prac(nowyprac)

