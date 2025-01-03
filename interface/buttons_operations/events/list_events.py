from tkinter import *
from database.db_connection import get_connection

class List_Events(Frame):
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
            self, text="LIST EVENTS", bg="#333333", fg="#BDFDC0", font=("Arial", 20, "bold"), justify="center"
        )
        content_label.pack(pady=30)


        div_Form = Frame(self, bg="#333333", height=250)
        div_Form.pack(pady=5, fill="x")
        form = Frame(div_Form, bg="#333333", height=250)
        form.place(anchor = "n", relx="0.5")

        #LIST
        self.output_label = Label(form, font=("Arial", 16), bg="#DDDDDD", fg="#000000", text="", height=8)
        self.output_label.pack(fill="x")


        # Mesaj de confirmare
        self.confirmation_label = Label(form, text="MESAJ DE CONFIRMARE\nROSU/VERDE", font=("Arial", 14, "bold"), fg="#FF0000", bg="#333333")
        self.confirmation_label.pack()

        # ADD BUTTON
        add_button = Button(
            self,
            text="LIST",
            bg="#66BB6A",
            fg="white",
            font=("Arial", 14, "bold"),
            width=15, height=2,
            relief="flat",
            command=self.show_events_list
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
            command=lambda: (self.reset_page(), controller.show_frame("EventsPage"))   # Navighează înapoi la MainPage
        )
        back_button.pack(pady=10)



    def show_events_list(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = "SELECT descriere FROM all_evenimente"
            cursor.execute(query)
            all_evenimente = cursor.fetchall()

        except:
            print("Eroare MYSQL")


        if all_evenimente:
            def get_nume(all_evenimente):
                nume_list = []
                for eveniment in all_evenimente:
                    nume_list.append(eveniment[0])
                self.confirmation_label.config(text="The list was displayed successfully", fg="#00FF00")
                return nume_list
        else:
            self.confirmation_label.config(text="The list could not be displayed", fg="#FF0000")

        nume_list = get_nume(all_evenimente)
        self.output_label.config(text="\n".join(nume_list))
        conn.close()
        cursor.close()

    def reset_page(self):
        self.output_label.config(text="")  # Golește lista
        self.confirmation_label.config(text="CONFIRMATION MESSAGE", fg="#FF0000")