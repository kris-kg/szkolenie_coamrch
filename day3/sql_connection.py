import mysql.connector
#passwd
db = mysql.connector.connect(user="root",password = "abc123",host="127.0.0.1",
                             port=3306,database="dbtestowa")

cursorObject = db.cursor()

#cursorObject.execute("CREATE DATABASE dbtestowa")

# studentTable = """
#                 CREATE TABLE STUDENT (
#                 IMIE VARCHAR(20) NOT NULL,
#                 KIERUNEK VARCHAR(50) NOT NULL,
#                 NR_ALB INT NOT NULL,
#                 WIEK INT
#                 )
#
# """
# cursorObject.execute(studentTable)

# sql = "INSERT INTO STUDENT(IMIE,KIERUNEK,NR_ALB,WIEK) VALUES(%s,%s,%s,%s)"
# #val = ("Romek","mechanika pojazdów",534534,21)
#
# val = [
#     ("Tomek","mechanika pojazdów",54645,21),
#     ("Olga","mechanika pojazdów",534534,21),
#     ("Gienek","mechanika pojazdów",676,21),
#     ("Ala","mechanika pojazdów",5467845,21),
#     ("Hania","mechanika pojazdów - \"ciągniki\"",5443645,21),
#
#        ]
#
# cursorObject.executemany(sql,val)

query = "SELECT IMIE,KIERUNEK FROM STUDENT WHERE NR_ALB > 60000"
cursorObject.execute(query)
wynik = cursorObject.fetchall()
for x in wynik:
    print(x)

#db.commit()
db.close()