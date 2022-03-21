from connection import connection
import mysql.connector
from imdb import Bea


class Filmm:

    def __init__(self):
        self.connection=connection
        self.cursor=connection.cursor()
        
    
    def addFilm(self,liste):
        sql="insert into films (id,filmname,year,point) values(%s,%s,%s,%s)"
        values=liste
        self.cursor.executemany(sql,values)
        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt eklendi")
        except mysql.connector.Error as err:
            print("hata",err)
        finally:
            self.connection.close()


nesne2=Bea()
listem=nesne2.find()
nesne3=Filmm()
nesne3.addFilm(listem)