from tkinter import *
from database.db_connection import get_connection

class Edit_Events(Frame):
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
            self, text="EDIT EVENT", bg="#333333", fg="#BDFDC0", font=("Arial", 20, "bold"), justify="center"
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

        # DATE
        date_label = Label(form, text="date:", font=("Arial", 20), fg="#FFFFFF", bg="#333333")
        date_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.date_entry = Entry(form, font=("Arial", 16), bg="#DDDDDD", fg="#000000")
        self.date_entry.grid(row=1, column=1, padx=10, pady=5)

        # TIME
        time_label = Label(form, text="time:", font=("Arial", 20), fg="#FFFFFF", bg="#333333")
        time_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.time_entry = Entry(form, font=("Arial", 16), bg="#DDDDDD", fg="#000000")
        self.time_entry.grid(row=2, column=1, padx=10, pady=5)

        # NAME
        name_label = Label(form, text="name:", font=("Arial", 20), fg="#FFFFFF", bg="#333333")
        name_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.name_entry = Entry(form, font=("Arial", 16), bg="#DDDDDD", fg="#000000")
        self.name_entry.grid(row=3, column=1, padx=10, pady=5)

        # Mesaj de confirmare
        self.confirmation_label = Label(form, text="MESAJ DE CONFIRMARE\nROSU/VERDE", font=("Arial", 14, "bold"), fg="#FF0000", bg="#333333")
        self.confirmation_label.grid(row=4, column=1, padx=10, pady=5)

        # ADD BUTTON
        add_button = Button(
            self,
            text="EDIT",
            bg="#66BB6A",
            fg="white",
            font=("Arial", 14, "bold"),
            width=15, height=2,
            relief="flat",
            command=lambda: self.modifica_eveniment(self.id_entry, self.date_entry, self.time_entry, self.name_entry)
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
            command=lambda: (self.reset_page(), controller.show_frame("EventsPage"))  # Navighează înapoi la MainPage
        )
        back_button.pack(pady=10)



    def modifica_eveniment(self, id_entry, date_entry, time_entry, name_entry):
        id=int(id_entry.get())
        data=date_entry.get()
        time=time_entry.get()
        name=name_entry.get()

        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = "SELECT eveniment_id, data, ora, descriere FROM all_evenimente"
            cursor.execute(query)
            all_lista = cursor.fetchall()

            if all_lista:
                for eveniment in all_lista:
                    if id == eveniment[0]:
                        update_query = "UPDATE all_evenimente SET data = %s, ora = %s, descriere = %s WHERE eveniment_id = %s"
                        cursor.execute(update_query, (data, time, name, id))
                        conn.commit()
                        self.confirmation_label.config(text=f"The event with id {id} \nhas been edited successfully",
                                                       fg="#00FF00")
                        break
            else:
                self.confirmation_label.config(text=f"Couldn't find id {id}", fg="#FF0000")
        except:
            print("Eroare MySQL")
        finally:
            conn.close()
            cursor.close()

    def reset_page(self):
        self.confirmation_label.config(text="CONFIRMATION MESSAGE", fg="#FF0000")
        self.id_entry.delete(0, END)
        self.date_entry.delete(0, END)
        self.time_entry.delete(0, END)
        self.name_entry.delete(0, END)