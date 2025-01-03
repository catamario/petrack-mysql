from tkinter import *
from database.db_connection import get_connection


class Edit_People(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#333333")
        self.controller = controller

        # Header
        header = Frame(self, bg="#282828", height=75)
        header.pack(fill="x")
        header_label = Label(
            header, text="People & Events Tracker", bg='#282828', fg='#66BB6A', font=("Arial", 20, "bold")
        )
        header_label.pack(pady=20)

        # Content
        content_label = Label(
            self, text="EDIT PEOPLE", bg="#333333", fg="#BDFDC0", font=("Arial", 20, "bold"), justify="center"
        )
        content_label.pack(pady=30)


        div_Form = Frame(self, bg="#333333", height=250)
        div_Form.pack(pady=5, fill="x")
        form = Frame(div_Form, bg="#333333", height=250)
        form.place(anchor = "e", relx="0.9", rely="0.5")

        # ID
        id_label = Label(form, text="id:", font=("Arial", 20), fg="#FFFFFF", bg="#333333")
        id_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.id_entry = Entry(form, font=("Arial", 16), bg="#DDDDDD", fg="#000000")
        self.id_entry.grid(row=0, column=1, padx=10, pady=5)

        # Nume
        name_label = Label(form, text="name:", font=("Arial", 20), fg="#FFFFFF", bg="#333333")
        name_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.name_entry = Entry(form, font=("Arial", 16), bg="#DDDDDD", fg="#000000")
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)

        # Adress
        address_label = Label(form, text="adress:", font=("Arial", 20), fg="#FFFFFF", bg="#333333")
        address_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.address_entry = Entry(form, font=("Arial", 16), bg="#DDDDDD", fg="#000000")
        self.address_entry.grid(row=2, column=1, padx=10, pady=5)

        # Mesaj de confirmare
        self.confirmation_label = Label(form, text="CONFIRMATION MESSAGE", font=("Arial", 14, "bold"), fg="#FF0000",
                                        bg="#333333")
        self.confirmation_label.grid(row=3, column=1, padx=10, pady=5)

        # ADD BUTTON
        add_button = Button(
            self,
            text="EDIT",
            bg="#66BB6A",
            fg="white",
            font=("Arial", 14, "bold"),
            width=15, height=2,
            relief="flat",
            command=lambda: self.modifica_persoana(self.id_entry, self.name_entry, self.address_entry)
        )
        add_button.pack()

        # Back Button
        back_button = Button(
            self,
            text="Back to Main",
            bg="#9DBA4D",
            fg="white",
            font=("Arial", 14, "bold"),
            width=15,height=2,
            relief="flat",
            command=lambda: (self.reset_page(), controller.show_frame("PeoplePage"))  # Navighează înapoi la MainPage
        )
        back_button.pack(pady=10)





    def modifica_persoana(self, id_entry, name_entry, address_entry):
        id=id_entry.get()
        name=name_entry.get()
        address=address_entry.get()

        #DATABASE
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = "SELECT persoana_id, nume, adresa FROM all_persoane"
            cursor.execute(query)
            all_persoane = cursor.fetchall()
        except:
            print("Eroare MySQL")

        if all_persoane:
            for persoana in all_persoane:
                if int(id) == persoana[0]:
                    update_query = "UPDATE all_persoane SET nume = %s, adresa = %s WHERE persoana_id = %s"
                    cursor.execute(update_query, (name, address, int(id)))
                    conn.commit()
                    self.confirmation_label.config(text=f"The person with id {id} \nhas been edited successfully",
                                                   fg="#00FF00")
                    break
        else:
            self.confirmation_label.config(text=f"Couldn't find id {id}", fg="#FF0000")

    def reset_page(self):
        self.confirmation_label.config(text="CONFIRMATION MESSAGE", fg="#FF0000")
        self.id_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.address_entry.delete(0, END)