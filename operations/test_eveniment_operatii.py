from domain.eveniment_entitate import Eveniment
from operations.eveniment_operatii import (get_descriere, cautare_eveniment, delete_eveniment)

def test_get_descriere():
    all_evenimente = [
        Eveniment(1, "20.05.2024", "20:30", "Jocul prietenilor"),
        Eveniment(2, "15.06.2024", "18:00", "Concert de vară"),
        Eveniment(3, "10.07.2024", "09:45", "Ședință de proiect")
    ]

    # obtinem lista de nume
    descriere_list = get_descriere(all_evenimente)

    # verificam daca lista de nume este corecta
    assert len(descriere_list) == 3, "Eroare: numărul de descrieri ar trebui să fie 3"
    assert descriere_list[0] == "Jocul prietenilor", "Eroare: prima descriere ar trebui să fie 'Jocul prietenilor'"
    assert descriere_list[1] == "Concert de vară", "Eroare: a doua descriere ar trebui să fie 'Concert de vară'"
    assert descriere_list[2] == "Ședință de proiect", "Eroare: a treia descriere ar trebui să fie 'Ședință de proiect'"




def test_cautare():
    all_evenimente = [ Eveniment(1, "20.05.2024", "20:30", "Jocul prietenilor")]

    assert cautare_eveniment(all_evenimente, "Jocul prietenilor") == "Jocul prietenilor", "Eroare: 'Jocul prietenilor' ar trebui să fie găsit"
    assert cautare_eveniment(all_evenimente, "Eveniment_inexistenta") is None, "Eroare: 'Eveniment_inexistenta' ar trebui sa nu fie gasit"




def test_delete_eveniment():
    all_evenimente = [
        Eveniment(1, "20.05.2024", "20:30", "Jocul prietenilor"),
        Eveniment(2, "15.06.2024", "18:00", "Concert de vară"),
        Eveniment(3, "10.07.2024", "09:45", "Ședință de proiect")
    ]

    # ștergem Evenimentul "Jocul prietenilor"
    delete_eveniment(all_evenimente, 1)

    # verificăm dacă "Jocul prietenilor" a fost șters
    assert len(all_evenimente) == 2, "Eroare: numărul de evenimente ar trebui să fie 2 după ștergere"
    assert all_evenimente[0].get_eveniment_descriere() == "Concert de vară", "Eroare: Evenimentul rămas ar trebui să fie 'Concert de vară'"
    assert all_evenimente[1].get_eveniment_descriere() == "Ședință de proiect", "Eroare: Evenimentul rămas ar trebui să fie 'Ședință de proiect'"

    # încercăm să ștergem un Eveniment care nu există
    delete_eveniment(all_evenimente, "Eveniment_inexistent")

    # verificăm că numărul de evenimente nu s-a schimbat
    assert len(all_evenimente) == 2, "Eroare: numărul de evenimente ar trebui să fie 2"




if __name__=='__main__':
    test_get_descriere()
    test_cautare()
    test_delete_eveniment()