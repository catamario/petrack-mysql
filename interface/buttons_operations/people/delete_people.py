from tkinter import *
from database.db_connection import get_connection

class Delete_People(Frame):
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
            self, text="DELETE PEOPLE", bg="#333333", fg="#BDFDC0", font=("Arial", 20, "bold"), justify="center"
        )
        content_label.pack(pady=30)


        div_Form = Frame(self, bg="#333333", height=250)
        div_Form.pack(pady=5, fill="x")
        form = Frame(div_Form, bg="#333333", height=250)
        form.place(anchor = "e", relx="0.9", rely="0.5")

        # Nume
        name_label = Label(form, text="name:", font=("Arial", 20), fg="#FFFFFF", bg="#333333")
        name_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.name_entry = Entry(form, font=("Arial", 16), bg="#DDDDDD", fg="#000000")
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)


        # Mesaj de confirmare
        self.confirmation_label = Label(form, text="CONFIRMATION MESSAGE", font=("Arial", 14, "bold"), fg="#FF0000", bg="#333333")
        self.confirmation_label.grid(row=4, column=1, padx=10, pady=5)

        # ADD BUTTON
        add_button = Button(
            self,
            text="DELETE",
            bg="#66BB6A",
            fg="white",
            font=("Arial", 14, "bold"),
            width=15, height=2,
            relief="flat",
            command=lambda: self.delete_persoana(self.name_entry)
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
            command=lambda: (self.reset_page(), controller.show_frame("PeoplePage"))   # Navighează înapoi la MainPage
        )
        back_button.pack(pady=10)

    def delete_persoana(self,  name_entry):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = "SELECT nume FROM all_persoane"
            cursor.execute(query)
            all_persoane=cursor.fetchall()
        except:
            print("Eroare MySQL")
        nume = name_entry.get()
        persoana_gasita = False


        for persoana in all_persoane:
            if persoana[0] == nume:
                delete_query = "DELETE FROM all_persoane WHERE nume = %s"
                cursor.execute(delete_query, (nume,))
                conn.commit()  # Confirmăm modificarea în baza de date
                persoana_gasita = True
                break


        if persoana_gasita:
            self.confirmation_label.config(text=f"The person {nume} \nhas been deleted successfully", fg="#00FF00")
        else:
            self.confirmation_label.config(text=f"Couldn't find {nume}", fg="#FF0000")


    def reset_page(self):
        self.confirmation_label.config(text="CONFIRMATION MESSAGE", fg="#FF0000")
        self.name_entry.delete(0, END)