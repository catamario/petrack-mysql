from operations.eveniment_operatii import (modifica_eveniment, delete_eveniment, cautare_eveniment, get_descriere)
from operations.persoana_operatii import (modifica_persoana, delete_persoana, cautare_persoana, get_nume)
from domain.eveniment_entitate import add_eveniment
from domain.persoana_entitate import add_persoana
from ui.operations_console import run_menu_operations

def run_menu(all_persoane, all_evenimente):
    while True:
        print("1 - Adauga persoana\n2 - Sterge persoana\n3 - Adauga eveniment\n"
              "4 - Sterge eveniment\n5 - Afiseaza persoane\n6 - Afiseaza evenimente\n"
              "7 - Modifica datele unei persoane\n8 - Modifica datele unui eveniment\n"
              "9 - Cauta persoana\n10 - Cauta eveniment\n"
              "11 - Deschide meniul cu operatii\n"
              "12-Iesi")
        optiune = input("optiune:")

        if optiune == "1":
            ui_add_persoana(all_persoane)
        elif optiune == "2":
            persoana_stearsa = input("Numele persoanei pe care doresti sa o stergi din lista:")
            if delete_persoana(all_persoane, persoana_stearsa) is True:
                print(f"Persoana cu numele {persoana_stearsa} a fost stearsa.")
            else:
                print(f"Persoana cu numele {persoana_stearsa} nu a fost gasita.")
        elif optiune == "3":
            ui_add_eveniment(all_evenimente)
        elif optiune == "4":
            eveniment_sters = int(input("ID-ul evenimentului pe care doresti sa-l stergi din lista:"))
            if delete_eveniment(all_evenimente, eveniment_sters) is True:
                print(f"Evenimentul cu ID-ul {eveniment_sters} a fost sters.")
            else:
                print(f"Evenimentul cu ID-ul {eveniment_sters} nu a fost gasit.")
        elif optiune == "5":
            nume_list = get_nume(all_persoane)
            print("Lista de persoane:")
            for nume in nume_list:
                print(nume)
        elif optiune == "6":
            descriere_list = get_descriere(all_evenimente)
            print("Lista de evenimente:")
            for descriere in descriere_list:
                print(descriere)
        elif optiune == "7":
            idtemp=int(input("Alege id pe care sa il modifici:"))
            modifica_persoana(all_persoane, idtemp)
        elif optiune == "8":
            idtemp = int(input("Alege id pe care sa il modifici:"))
            modifica_eveniment(all_evenimente, idtemp)
        elif optiune == "9":
            numetemp=input("Cauta persoana dupa nume:")
            if cautare_persoana(all_persoane, numetemp) is not None:
                print(f"Persoana {cautare_persoana(all_persoane, numetemp)} exista in program.")
            else:
                print("Nu exista acest nume printre persoanele din program.")
        elif optiune == "10":
            descrieretemp=input("Cauta eveniment dupa descriere:")
            if cautare_eveniment(all_evenimente, descrieretemp) is not None:
                print(f"Evenimentul cu descrierea {cautare_eveniment(all_evenimente, descrieretemp)} exista in program.")
            else:
                print("Nu exista acest eveniment descris.")
        elif optiune == "11":
            run_menu_operations(all_persoane, all_evenimente)
        elif optiune == "12":
            print("Iesi din program.")
            break  # iese din bucla while si opreste programul
        else:
            print("Optiune invalida. Te rog sa alegi din nou.")

"""PENTRU EVENIMENTE"""

def ui_add_eveniment(all_evenimente):
    eveniment_id = int(input("id eveniment:"))
    data = input("data eveniment (format: YYYY-MM-DD):")
    ora = input("ora evenimentului (format: HH:MM):")
    descriere = input("descriere eveniment:")
    try:
        add_eveniment(all_evenimente, eveniment_id, data, ora, descriere)
    except:
        ValueError
        print("Deja exista un eveniment cu acest id.")
        ui_add_eveniment(all_evenimente)


"""PENTRU PERSOANE"""

def ui_add_persoana(all_persoane):
    persoana_id = int(input("id:"))
    nume = input("nume:")
    adresa = input("adresa:")
    try:
        add_persoana(all_persoane, persoana_id, nume, adresa)
    except:
        ValueError
        print("Deja exista o persoana cu acest id")
        ui_add_persoana(all_persoane) #reapeleaza UI de adaugare persoana daca exista deja ID