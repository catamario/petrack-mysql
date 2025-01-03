from tkinter import *

class MainPage(Frame):
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

        # Welcome frame
        welcome_frame = Frame(self, bg="#333333")
        welcome_frame.pack(pady=50)
        welcome_label = Label(
            welcome_frame, text="Welcome!", bg="#333333", fg="#BDFDC0", font=("Arial", 16, "bold"), justify="center"
        )
        welcome_label.pack()
        rest_of_text_label = Label(
            welcome_frame,
            text="The best solution for managing people and events effortlessly.",
            bg="#333333",
            fg="#BDFDC0",
            font=("Arial", 14),
            justify="center",
            wraplength=450,
        )
        rest_of_text_label.pack()

        # Buttons div
        buttons_div = Frame(self, bg="#333333", height=60)
        buttons_div.pack(pady=50, fill="x")
        buttons_frame = Frame(buttons_div, bg="#333333")
        buttons_frame.place(relx=0.5, anchor="n")

        # Buttons
        people_button = Button(
            buttons_frame,
            text="People",
            bg="#66BB6A",
            fg="white",
            font=("Arial", 20, "bold"),
            width=10,
            relief="flat",
            command=lambda: controller.show_frame("PeoplePage")  # Navighează la PeoplePage
        )
        people_button.grid(row=0, column=0, padx=10)

        events_button = Button(
            buttons_frame,
            text="Events",
            bg="#66BB6A",
            fg="white",
            font=("Arial", 20, "bold"),
            width=10,
            relief="flat",
            command=lambda: controller.show_frame("EventsPage")
        )
        events_button.grid(row=0, column=1, padx=10)

        # Manage All Button
        buttons_div_2 = Frame(self, bg="#333333", height=60)
        buttons_div_2.pack(pady=5, fill="x")
        buttons_frame_2 = Frame(buttons_div_2, bg="#333333")
        buttons_frame_2.place(relx=0.5, anchor="n")
        manage_button = Button(
            buttons_frame_2,
            text="Manage All",
            bg="#66BB6A",
            fg="white",
            font=("Arial", 20, "bold"),
            width=10,
            relief="flat",
            command=lambda: print("Navighează la Manage All")
        )
        manage_button.grid()