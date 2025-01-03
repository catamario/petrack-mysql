from database.db_connection import get_connection

def add_eveniment(eveniment_id, data, ora, descriere):
    if find_by_id_eveniment(eveniment_id) is None:
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = "INSERT INTO all_evenimente (eveniment_id, data, ora, descriere) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (eveniment_id, data, ora, descriere))
            conn.commit()
        finally:
            cursor.close()
            conn.close()
    else:
        raise ValueError("Evenimentul cu acest ID există deja.")




class Eveniment:
    def __init__(self, eveniment_id, data, ora, descriere):
        self.__eveniment_id = eveniment_id
        self.__data = data
        self.__ora = ora
        self.__descriere = descriere

    def __str__(self):
        return f"{self.__data} {self.__ora}"

    ##GETTER
    def get_eveniment_id(self):
        return self.__eveniment_id

    def get_eveniment_data(self):
        return self.__data

    def get_eveniment_ora(self):
        return self.__ora

    def get_eveniment_descriere(self):
        return self.__descriere

    ##SETTER
    def set_eveniment_id(self, eveniment_id):
        self.__eveniment_id = eveniment_id

    def set_eveniment_data(self, data):
        self.__data = data

    def set_eveniment_ora(self, ora):
        self.__ora = ora

    def set_eveniment_descriere(self, descriere):
        self.__descriere = descriere


## OPERATIONS

    """   (==)     (!=)   PENTRU DATA"""
    def __eq__(self, other):
        return self.__data == other.get_eveniment_data()

    def __ne__(self, other):
        return not self.__eq__(other)

    """   (<)     (>)   PENTRU ORA"""
    def __lt__(self, other):
        return self.__ora < other.get_eveniment_ora()

    def __gt__(self, other):
        return self.__ora > other.get_eveniment_ora()

    """   (<=)     (>=)   PENTRU ORA+DATA"""

    def __le__(self, other):
        return (self.__data, self.get_eveniment_ora()) <= (other.__data, other.get_eveniment_ora())

    def __ge__(self, other):
        return (self.__data, self.get_eveniment_ora()) >= (other.__data, other.get_eveniment_ora())



def find_by_id_eveniment(id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = "SELECT eveniment_id, data, ora, descriere FROM all_evenimente WHERE eveniment_id = %s"
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        if result:
            return result
        return None
    finally:
        cursor.close()
        conn.close()