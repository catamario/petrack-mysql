from tkinter import *

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
        output_label = Label(form, font=("Arial", 16), bg="#DDDDDD", fg="#000000", text="lista", height=8)
        output_label.pack(fill="x")


        # Mesaj de confirmare
        confirmation_label = Label(form, text="MESAJ DE CONFIRMARE\nROSU/VERDE", font=("Arial", 14, "bold"), fg="#FF0000", bg="#333333")
        confirmation_label.pack()

        # ADD BUTTON
        add_button = Button(
            self,
            text="LIST",
            bg="#66BB6A",
            fg="white",
            font=("Arial", 14, "bold"),
            width=15, height=2,
            relief="flat",
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
            command=lambda: controller.show_frame("EventsPage")  # Navighează înapoi la MainPage
        )
        back_button.pack(pady=10)
