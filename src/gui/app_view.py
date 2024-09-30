import customtkinter as ctk
from gui.subject_view import SubjectFrame

class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("System")  # Predefinito, può essere "Light" o "Dark"
        ctk.set_default_color_theme("dark-blue")  # Può essere anche "green" o "dark-blue"

        self.title('Flashcard')
        self.geometry('1000x700')
        self.minsize(400, 400)
        self.subject_menu()

        switch = ctk.CTkSwitch(self, text='Cambia Tema', font=('Red Hat Display', 20), command=self.toggle_theme)
        switch.pack(pady=10)


    def toggle_theme(self):
        # Cambia tra tema chiaro e scuro
        if ctk.get_appearance_mode() == "Dark":
            ctk.set_appearance_mode("Light")
        else:
            ctk.set_appearance_mode("Dark")


    def subject_menu(self):
        '''
            shows the main menu, where there are all the subject
        '''
        frame = SubjectFrame(self)
        frame.pack(fill="both", expand=True)



    def topic_menu(self, subject_name):

        pass
