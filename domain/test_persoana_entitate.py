from lab7.domain.persoana_entitate import Persoana
from persoana_entitate import add_persoana

def test_add_persoana():
    all_persoane = []

    # adaugam prima persoana
    add_persoana(all_persoane, 1, "Catalin", "Lalelelor")

    # verificam daca persoana a fost adaugata
    assert len(all_persoane) == 1, "Eroare: numarul de persoane ar trebui sa fie 1"
    assert all_persoane[0].get_persoana_id() == 1, "Eroare: persoana_id ar trebui sa fie 1"
    assert all_persoane[0].get_persoana_nume() == "Catalin", "Eroare: nume ar trebui sa fie 'Catalin'"
    assert all_persoane[0].get_persoana_adresa() == "Lalelelor", "Eroare: adresa ar trebui sa fie 'Lalelelor'"




def test_add_operation():
    all_persoane = []

    persoana1=Persoana(1, "Catalin", "Lalelelor")
    persoana2=Persoana(2, "Mario", "Ghioceilor")

    assert persoana1 + persoana2 == "Catalin Mario", "Test esuat: operatorul (+) nu a functionat corect."

def test_iadd_operation():
    all_persoane = []

    persoana1=Persoana(1, "Catalin", "Lalelelor")
    persoana2=Persoana(2, "Mario", "Ghioceilor")

    persoana1 += persoana2
    assert str(persoana1) == "Catalin Mario", "Test esuat: operatorul (+=) nu a functionat corect."

def test_sub_operation():
    persoana1 = Persoana(1, "Catalin", "Lalelelor")
    persoana2 = Persoana(2, "Mario", "Ghioceilor")


    assert persoana2 - persoana1 == 1, f"Test esuat: {persoana2.get_persoana_id()} - {persoana1.get_persoana_id()} nu a funcționat corect."



if __name__ == '__main__':
    test_add_persoana()
    test_add_operation()
    test_iadd_operation()
    test_sub_operation()
