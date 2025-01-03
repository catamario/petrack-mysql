from database.db_connection import get_connection

def add_persoana(persoana_id, nume, adresa):
    if find_by_id_persoana(persoana_id) is None:
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = "INSERT INTO all_persoane (persoana_id, nume, adresa) VALUES (%s, %s, %s)"
            cursor.execute(query, (persoana_id, nume, adresa))
            conn.commit()
        finally:
            cursor.close()
            conn.close()
    else:
        raise ValueError(f"Persoana cu ID-ul {persoana_id} exista deja în baza de date.")




class Persoana:
    def __init__(self, persoana_id, nume, adresa):
        self.__persoana_id = persoana_id
        self.__nume = nume
        self.__adresa = adresa

    def __str__(self):
        return self.__nume



##GETTER
    def get_persoana_id(self):
        return self.__persoana_id

    def get_persoana_nume(self):
        return self.__nume

    def get_persoana_adresa(self):
        return self.__adresa

##SETTER
    def set_persoana_id(self, persoana_id):
        self.__persoana_id = persoana_id

    def set_persoana_nume(self, nume):
        self.__nume = nume

    def set_persoana_adresa(self, adresa):
        self.__adresa = adresa


## OPERATIONS

    """   (+)     PENTRU NUME"""
    def __add__(self, other):
        return f"{self.__nume} {other.get_persoana_nume()}"


    """(+=)   PENTRU NUME"""
    def __iadd__(self, other):
        self.__nume += f" {other.get_persoana_nume()}"
        return self


    """(-)    PENTRU ID"""
    def __sub__(self, other):
        return self.__persoana_id - other.get_persoana_id()





def find_by_id_persoana(persoana_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = "SELECT persoana_id, nume, adresa FROM all_persoane WHERE persoana_id = %s"
        cursor.execute(query, (persoana_id,))
        result = cursor.fetchone()
        if result:
            return result
        return None
    finally:
        cursor.close()
        conn.close()