def get_descriere(all_evenimente):
    descriere_list = []
    for eveniment in all_evenimente:
        descriere_list.append(eveniment.get_eveniment_descriere())
    return descriere_list




def cautare_eveniment(all_list, nume):
    if all_list:
        for eveniment in all_list:
            if nume == eveniment.get_eveniment_descriere():
                return eveniment.get_eveniment_descriere()

    return None




def modifica_eveniment(all_lista, id):
    if all_lista:
        for eveniment in all_lista:
            if id == eveniment.get_eveniment_id():
                eveniment.set_eveniment_id(int(input("ID:")))
                eveniment.set_eveniment_data(input("DATA:"))
                eveniment.set_eveniment_ora(input("ORA:"))
                eveniment.set_eveniment_descriere(input("DESCRIERE:"))
                print(f' ID: {eveniment.get_eveniment_id()}, \n DATA: {eveniment.get_eveniment_data()}, \n ORA: {eveniment.get_eveniment_ora()}, \n DESCRIERE: {eveniment.get_eveniment_descriere()}')
                break




def delete_eveniment(all_evenimente, eveniment_id):
    for eveniment in all_evenimente:
        if eveniment.get_eveniment_id() == eveniment_id:
            all_evenimente.remove(eveniment)
            return True
    return False