import tkinter as tk
from app import service
from gui.subject_view import SubjectFrame

class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title('Flashcard')
        self.geometry("1000x700")
        self.configure(bg="lightgray")
        self.subject_menu()


    def subject_menu(self):
        '''
            shows the main menu, where there are all the subject
        '''
        frame = SubjectFrame(self)
        frame.pack(fill="both", expand=True)



    def topic_menu(self, subject_name):

        pass
