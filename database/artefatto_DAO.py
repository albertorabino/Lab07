from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass



    def read_epoche(self):
        cnx = ConnessioneDB.get_connection()
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("""SELECT DISTINCT epoca 
                          FROM artefatto """)
        rows = cursor.fetchall()
        epoche = [r[0] for r in rows]
        cursor.close()
        cnx.close()
        return epoche

    @staticmethod
    def read_artefatti(museo: str, epoca: str):
        print("Executing read from database using SQL query")
        result = []
        cnx = ConnessioneDB.get_connection()

        if cnx is None:
            print("Connection failed")
            return []
        else:
            cursor = cnx.cursor(dictionary=True)
            query = ("""
                    select 
                            a.nome as nome_artefatto,
                            m.nome as nome_museo, 
                            a.epoca as epoca
                    from 
                            artefatto a,
                            museo m
                    where 
                            (%s is NULL or a.epoca=%s)
                    and 
                            (%s is NULL or m.nome=%s)
                 """)
            cursor.execute(query, (epoca, epoca, museo, museo))
            rows = cursor.fetchall()
            for row in rows:
                artefatto = Artefatto(row["id"], row["nome"], row["tipologia"], row["epoca"], row["id_museo"])
                result.append(artefatto)

            cursor.close()
            cnx.close()
            return result