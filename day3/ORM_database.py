import mysql.connector
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:abc123@localhost:3306/dbtestowa', echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(length=50))
    fullname = sqlalchemy.Column(sqlalchemy.String(length=50))
    nickname = sqlalchemy.Column(sqlalchemy.String(length=50))

    def __repr__(self):
        return f"<User(name={self.name}, fullname={self.fullname}, nickname={self.nickname})"


Base.metadata.create_all(engine)

Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

newuser = User(name='Marcin',fullname='Marcin Albiniak',nickname='al')
session.add(newuser)
session.commit()

newuser = User(name='Alicja',fullname='Alicja Nowak',nickname='ala')
session.add(newuser)
session.commit()

Session = sessionmaker(bind=engine)
session = Session()

for s in session.query(User).all():
    print(s.fullname)
print("_________________________________________________________")
for s in session.query(User).filter(User.nickname=="al"):
    print(s.fullname)
