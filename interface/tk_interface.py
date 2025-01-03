from tkinter import *

from interface.buttons_operations.events.delete_events import Delete_Events
from tk_mainpage import MainPage
from tk_peoplepage import PeoplePage
from tk_eventspage import EventsPage
from interface.buttons_operations.people.add_people import Add_People
from interface.buttons_operations.events.add_events import Add_Events
from interface.buttons_operations.people.edit_people import Edit_People
from interface.buttons_operations.events.edit_events import Edit_Events
from interface.buttons_operations.events.delete_events import Delete_Events
from interface.buttons_operations.people.delete_people import Delete_People
from interface.buttons_operations.people.search_people import Search_People
from interface.buttons_operations.events.search_events import Search_Events
from interface.buttons_operations.people.list_people import List_People
from interface.buttons_operations.events.list_events import List_Events

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("P&E Track")
        self.geometry("500x600")
        self.resizable(False, False)
        self.config(background='#333333')

        self.all_persoane = []
        self.all_events = []

        # Container pentru pagini
        self.container = Frame(self, bg="#333333")
        self.container.pack(fill="both", expand=True)

        self.frames = {}

        # Adăugăm paginile
        for Page in (MainPage, PeoplePage, EventsPage, Add_People, Add_Events, Edit_People, Edit_Events, Delete_Events,
                     Delete_People,
                     Search_Events, Search_People, List_Events, List_People):
            page_name = Page.__name__

            frame = Page(parent=self.container, controller=self)

            self.frames[page_name] = frame

        self.show_frame("MainPage")  # Afișăm MainPage la început

    def show_frame(self, page_name):
        """Afișează cadrul selectat și ascunde celelalte."""
        for frame in self.frames.values():
            frame.pack_forget()  # Ascundem toate cadrele
        self.frames[page_name].pack(fill="both", expand=True)  # Afișăm cadrul selectat

if __name__ == "__main__":
    app = App()
    app.mainloop()
