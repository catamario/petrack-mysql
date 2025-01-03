from domain.persoana_entitate import Persoana
from operations.persoana_operatii import (get_nume, cautare_persoana, delete_persoana)

def test_get_nume():
    all_persoane = [
        Persoana(1, "Catalin", "Lalelelor"),
        Persoana(2, "Andrei", "Florilor"),
        Persoana(3, "Florin", "Somcut")
    ]

    # obtinem lista de nume
    nume_list = get_nume(all_persoane)

    # verificam daca lista de nume este corecta
    assert len(nume_list) == 3, "Eroare: numarul de nume ar trebui sa fie 3"
    assert nume_list[0] == "Catalin", "Eroare: primul nume ar trebui sa fie 'Catalin'"
    assert nume_list[1] == "Andrei", "Eroare: al doilea nume ar trebui sa fie 'Andrei'"
    assert nume_list[2] == "Florin", "Eroare: al treilea nume ar trebui sa fie 'Florin'"




def test_cautare():
    all_persoane = [Persoana(1, "john doe", "strada 1")]

    assert cautare_persoana(all_persoane, "john doe") == "john doe", "Eroare: 'john doe' ar trebui sa fie gasit"
    assert cautare_persoana(all_persoane, "persoana_inexistenta") is None, "Eroare: 'persoana_inexistenta' ar trebui sa nu fie gasit"




def test_delete_persoana():
    all_persoane = [
        Persoana(1, "john doe", "strada 1"),
        Persoana(2, "jane doe", "strada 2")
    ]

    # stergem persoana "john doe"
    delete_persoana(all_persoane, "john doe")

    # verificam daca "john doe" a fost sters
    assert len(all_persoane) == 1, "Eroare: numarul de persoane ar trebui sa fie 1 dupa stergere"
    assert all_persoane[0].get_persoana_nume() == "jane doe", "Eroare: persoana ramasa ar trebui sa fie 'jane doe'"

    # incercam sa stergem o persoana care nu exista
    delete_persoana(all_persoane, "persoana_inexistenta")

    # verificam ca numarul de persoane nu s-a schimbat
    assert len(all_persoane) == 1, "Eroare: numarul de persoane ar trebui sa fie 1"




if __name__=='__main__':
    test_get_nume()
    test_cautare()
    test_delete_persoana()