

from unittest import result

from database import DB_connect
from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto
from model.museoDTO import Museo
import mysql.connector

'''
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
'''

# TODO

class MuseoDAO:
    def __init__(self):
        pass

    def read_musei(self):
        result = []
        cnx = ConnessioneDB.get_connection()
        cursor = cnx.cursor()

        query = ''' SELECT * FROM museo'''
        cursor.execute(query)
        for row in cursor:
            museo = Museo(row["id"], row["nome"], row["tipologia"])
            result.append(museo)
        cursor.close()
        cnx.close()
        return result

