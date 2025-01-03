from tkinter import *

class EventsPage(Frame):
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
            self, text="This is the Events Page.", bg="#333333", fg="#BDFDC0", font=("Arial", 16), justify="center"
        )
        content_label.pack(pady=50)

        buttons_div = Frame(self, bg="#333333", height=60)
        buttons_div.pack(pady=30, fill="x")
        buttons_frame = Frame(buttons_div, bg="#333333")
        buttons_frame.place(relx=0.5, anchor="n")

        # Buttons
        add_button = Button(
            buttons_frame,
            text="ADD",
            bg="#66BB6A",
            fg="white",
            font=("Arial", 20, "bold"),
            width=7,
            relief="flat",
            command=lambda: controller.show_frame("Add_Events")
        )
        add_button.grid(row=0, column=0, padx=10)

        edit_button = Button(
            buttons_frame,
            text="EDIT",
            bg="#66BB6A",
            fg="white",
            font=("Arial", 20, "bold"),
            width=7,
            relief="flat",
            command=lambda: controller.show_frame("Edit_Events")
        )
        edit_button.grid(row=0, column=1, padx=10)

        delete_button = Button(
            buttons_frame,
            text="DELETE",
            bg="#66BB6A",
            fg="white",
            font=("Arial", 20, "bold"),
            width=7,
            relief="flat",
            command=lambda: controller.show_frame("Delete_Events")
        )
        delete_button.grid(row=0, column=2, padx=10)

        # Manage All Button
        buttons_div_2 = Frame(self, bg="#333333", height=60)
        buttons_div_2.pack(pady=5, fill="x")
        buttons_frame_2 = Frame(buttons_div_2, bg="#333333")
        buttons_frame_2.place(relx=0.5, anchor="n")
        search_button = Button(
            buttons_frame_2,
            text="SEARCH",
            bg="#66BB6A",
            fg="white",
            font=("Arial", 20, "bold"),
            width=7,
            relief="flat",
            command=lambda: controller.show_frame("Search_Events")
        )
        search_button.grid(row=0, column=0, padx=10)

        list_button = Button(
            buttons_frame_2,
            text="LIST",
            bg="#66BB6A",
            fg="white",
            font=("Arial", 20, "bold"),
            width=7,
            relief="flat",
            command=lambda: controller.show_frame("List_Events")
        )
        list_button.grid(row=0, column=1, padx=10)

        # Back Button
        back_button = Button(
            self,
            text="Back to Main",
            bg="#9DBA4D",
            fg="white",
            font=("Arial", 14, "bold"),
            width=15, height=2,
            relief="flat",
            command=lambda: controller.show_frame("MainPage")  # Navighează înapoi la MainPage
        )
        back_button.pack(pady=50)
