from eveniment_entitate import add_eveniment
from eveniment_entitate import Eveniment

def test_add_eveniment():
    all_evenimente = []

    # adaugam prima persoana
    add_eveniment(all_evenimente, 1, "24.12.2024", "20:33", "Mircea Bravo")

    # verificam daca persoana a fost adaugata
    assert len(all_evenimente) == 1, "Eroare: numarul de persoane ar trebui sa fie 1"
    assert all_evenimente[0].get_eveniment_id() == 1, "Eroare: persoana_id ar trebui sa fie 1"
    assert all_evenimente[0].get_eveniment_data() == "24.12.2024", "Eroare: data ar trebui sa fie '24.12.2024'"
    assert all_evenimente[0].get_eveniment_ora() == "20:33", "Eroare: ora ar trebui sa fie '20:33'"
    assert all_evenimente[0].get_eveniment_descriere() == "Mircea Bravo", "Eroare: descrierea ar trebui sa fie 'Mircea Bravo'"




def test_eq_ne_operation(): #comparatie data
    all_evenimente = []

    eveniment1 = Eveniment(1, "24.12.2024", "20:33", "Dumbrava")
    eveniment2 = Eveniment(2, "25.12.2024", "20:34", "Aleea")
    eveniment3 = Eveniment(3, "24.12.2024", "20:35", "Sceneta")

    assert eveniment1 == eveniment3, "Test esuat: operatorul (==) nu a functionat corect."
    assert eveniment1 != eveniment2, "Test esuat: operatorul (!-) nu a functionat corect."

def test_lt_gt_operation(): #comparatie data
    all_evenimente = []

    eveniment1 = Eveniment(1, "24.12.2024", "20:33", "Dumbrava")
    eveniment2 = Eveniment(2, "25.12.2024", "20:34", "Aleea")
    eveniment3 = Eveniment(3, "24.12.2024", "20:35", "Sceneta")


    assert eveniment1 < eveniment3, "Test esuat: operatorul (<) nu a functionat corect."
    assert eveniment2 > eveniment1, "Test esuat: operatorul (>) nu a functionat corect."


def test_le_ge_operation(): #comparatie data si ora
    all_evenimente = []

    eveniment1 = Eveniment(1, "24.12.2024", "20:33", "Dumbrava")
    eveniment2 = Eveniment(2, "25.12.2024", "20:34", "Aleea")
    eveniment3 = Eveniment(3, "24.12.2024", "20:35", "Sceneta")


    assert eveniment1 < eveniment3, "Test esuat: operatorul (<) nu a functionat corect."
    assert eveniment2 > eveniment1, "Test esuat: operatorul (>) nu a functionat corect."


if __name__ == '__main__':
    test_add_eveniment()
    test_eq_ne_operation()
    test_lt_gt_operation()
    test_le_ge_operation()
