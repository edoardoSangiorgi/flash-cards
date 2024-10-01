import customtkinter as ctk
from gui.subject_view import SubjectFrame
from gui.topic_view import TopicFrame

class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("System")  # Predefinito, può essere "Light" o "Dark"
        ctk.set_default_color_theme("dark-blue")  # Può essere anche "green" o "dark-blue"

        self.title('Flashcard')
        self.geometry('1000x700')
        self.minsize(400, 400)

        self.current_frame = None
        self.switch = None
        self.subject_menu()
        

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
        self.destroy_current_frame()
        self.current_frame = SubjectFrame(self)
        self.current_frame.pack(fill="both", expand=True)
        self.theme_switch()



    def topic_menu(self, subject_name):
        '''
            shows the menu of a spcific subject and all the arugments

            Input:
                subject_name    :   the name of the subject
                str
        '''
        self.destroy_current_frame()
        self.current_frame = TopicFrame(subject_name, self)
        self.current_frame.pack(fill="both", expand=True)
        self.theme_switch()

    
    def theme_switch(self):
        self.switch = ctk.CTkSwitch(self, text='Cambia Tema', font=('Red Hat Display', 20), command=self.toggle_theme)
        self.switch.pack(pady=10)
    

    def destroy_current_frame(self):
        if self.current_frame is not None:
            self.current_frame.destroy()
        
        if self.switch is not None:
            self.switch.destroy()
