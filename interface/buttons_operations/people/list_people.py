from tkinter import *
from database.db_connection import get_connection


class List_People(Frame):
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
            self, text="LIST PEOPLE", bg="#333333", fg="#BDFDC0", font=("Arial", 20, "bold"), justify="center"
        )
        content_label.pack(pady=30)


        div_Form = Frame(self, bg="#333333", height=250)
        div_Form.pack(pady=5, fill="x")
        form = Frame(div_Form, bg="#333333", height=250)
        form.place(anchor = "n", relx="0.5")

        #LIST
        self.output_label = Label(form, font=("Arial", 16), bg="#DDDDDD", fg="#000000", text="", height=8, width=15)
        self.output_label.pack()


        # Mesaj de confirmare
        self.confirmation_label = Label(form, text="CONFIRMATION MESSAGE", font=("Arial", 14, "bold"), fg="#FF0000", bg="#333333")
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
            command=self.show_people_list
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

    def show_people_list(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query="SELECT nume FROM all_persoane"
            cursor.execute(query)
            all_persoane = cursor.fetchall()
        except:
            print("Eroare MYSQL")


        if all_persoane:
            def get_nume(all_persoane):
                nume_list = []
                for persoana in all_persoane:
                    nume_list.append(persoana[0])
                self.confirmation_label.config(text="The list was displayed successfully", fg="#00FF00")
                return nume_list
        else:
            self.confirmation_label.config(text="The list could not be displayed", fg="#FF0000")

        nume_list = get_nume(all_persoane)
        self.output_label.config(text="\n".join(nume_list))
        conn.close()
        cursor.close()

    def reset_page(self):
        self.output_label.config(text="")  # Golește lista
        self.confirmation_label.config(text="CONFIRMATION MESSAGE", fg="#FF0000")