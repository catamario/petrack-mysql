from domain.persoana_entitate import find_by_id_persoana
from domain.eveniment_entitate import find_by_id_eveniment

def run_menu_operations(all_persoane, all_evenimente):
    while True:
        print("1 - Concateneaza numele a doua persoane folosind id-urile lor.(+)\n2 - Concateneaza numele a doua persoane folosind id-urile lor.(+=)METODA 2\n"
              "3 - Verifica distanta dintre doua persoane prin id-urile acestora.(-)\n"
              "4 - Verifica datele a doua evenimente daca sunt aceleasi sau nu(==)/(!=).\n5 - Verifica daca un eveniment este inaintea altuia in functie de ora.(<)/(>)\n"
              "6 - Verifica daca un eveniment este inaintea altuia in functie de data si ora(<=)/(>=).\n"
              "7 - Mergi inapoi la meniul general")
        optiune = input("optiune:")

        if optiune == "7":
            print("Iesi din program.")
            break  # iese din bucla while si opreste programul

        elif optiune == "1":
            id_cautat1 = int(input("ID-ul primei persoane:"))
            id_cautat2 = int(input("ID-ul celei de a doua persoane:"))

            persoana1 = find_by_id_persoana(all_persoane, id_cautat1)
            persoana2 = find_by_id_persoana(all_persoane, id_cautat2)

            if persoana1 and persoana2 :
                print(persoana1 + persoana2)
            else:
                print("Ai introdus ID gresit, incearca din nou.")

        elif optiune == "2":
            id_cautat1 = int(input("ID-ul primei persoane:"))
            id_cautat2 = int(input("ID-ul celei de a doua persoane:"))

            persoana1 = find_by_id_persoana(all_persoane, id_cautat1)
            persoana2 = find_by_id_persoana(all_persoane, id_cautat2)

            if persoana1 and persoana2 :
                persoana1 += persoana2
                print(persoana1)
            else:
                print("Ai introdus ID gresit, incearca din nou.")

        elif optiune == "3":
            id_cautat1 = int(input("ID-ul primei persoane:"))
            id_cautat2 = int(input("ID-ul celei de a doua persoane:"))

            persoana1 = find_by_id_persoana(all_persoane, id_cautat1)
            persoana2 = find_by_id_persoana(all_persoane, id_cautat2)

            if persoana1 and persoana2:
                print(f"Distanta de persoane dintre cele id-uri este de: {persoana2 - persoana1 - 1} persoana(e)")
            else:
                print("Ai introdus ID gresit, incearca din nou.")

        elif optiune == "4":
            id_cautat1 = int(input("ID-ul primului eveniment:"))
            id_cautat2 = int(input("ID-ul celui de al doilea eveniment:"))

            eveniment1 = find_by_id_eveniment(all_evenimente, id_cautat1)
            eveniment2 = find_by_id_eveniment(all_evenimente, id_cautat2)

            if eveniment1 and eveniment2:
                if eveniment1 == eveniment2:
                    print(f"Evenimentele au loc in aceeasi data. {eveniment1.get_eveniment_data()}")
                else:
                    print(f"Evenimentele au loc in date diferite. ev1: {eveniment1.get_eveniment_data()} si ev2: {eveniment2.get_eveniment_data()}")
            else:
                print("Ai introdus ID gresit, incearca din nou.")

        elif optiune == "5":
            id_cautat1 = int(input("ID-ul primului eveniment:"))
            id_cautat2 = int(input("ID-ul celui de al doilea eveniment:"))

            eveniment1 = find_by_id_eveniment(all_evenimente, id_cautat1)
            eveniment2 = find_by_id_eveniment(all_evenimente, id_cautat2)

            if eveniment1 and eveniment2:
                if eveniment1 > eveniment2:
                    print(f"Primul eveniment introdus are loc dupa cel de al doilea. ev1: {eveniment1.get_eveniment_ora()} - ev2: {eveniment2.get_eveniment_ora()}")
                elif eveniment2 > eveniment1:
                    print(f"Al doilea eveniment introdus are loc inaintea primului eveniment. ev2: {eveniment2.get_eveniment_ora()} - ev1: {eveniment1.get_eveniment_ora()}")
                else:
                    print("Ambele au loc la aceeasi ora.")
            else:
                print("Ai introdus ID gresit, incearca din nou.")

        elif optiune == "6":
            id_cautat1 = int(input("ID-ul primului eveniment:"))
            id_cautat2 = int(input("ID-ul celui de al doilea eveniment:"))

            eveniment1 = find_by_id_eveniment(all_evenimente, id_cautat1)
            eveniment2 = find_by_id_eveniment(all_evenimente, id_cautat2)

            if eveniment1 and eveniment2:
                if eveniment1 >= eveniment2:
                    print(f"Primul eveniment introdus are loc (dupa cel de al doilea)/(concomitent cu cel de al doilea). ev1: {eveniment1.get_eveniment_data()} {eveniment1.get_eveniment_ora()} - ev2: {eveniment2.get_eveniment_data()} {eveniment2.get_eveniment_ora()}")
                else:
                    print(f"Al doilea eveniment introdus are loc (inaintea primului eveniment)/(concomitent cu primul). ev2: {eveniment2.get_eveniment_data()} {eveniment2.get_eveniment_ora()} - ev1: {eveniment1.get_eveniment_data()} {eveniment1.get_eveniment_ora()}")
            else:
                print("Ai introdus ID gresit, incearca din nou.")
        else:
            print("Optiune invalida. Te rog sa alegi din nou.")
