import customtkinter as ctk
from tkinter import messagebox
from app import service

class SubjectFrame(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.font_title = 'DM Serif Display'
        self.font_text = 'Red Hat Display'

        # -- top bar --
        top_bar = ctk.CTkFrame(self, height=50)
        top_bar.pack(fill="x", side="top")

        # -- title of the page --
        title_label = ctk.CTkLabel(top_bar, text="Le Tue Materie", font=(self.font_title, 50))
        title_label.pack(side="left", padx=10, pady=10)

        # -- button '+' --
        add_button = ctk.CTkButton(top_bar, text="Nuova Materia", font=(self.font_text, 30), width=40, command=self.add_subject)
        add_button.pack(side="right", padx=10, pady=10)

        # -- display subjects --
        self.update_subjects()


    def update_subjects(self):
        '''
            update the subject button list
        '''
        # -- remove subject buttons (if present) --
        for widget in self.winfo_children():
            if isinstance(widget, ctk.CTkButton):
                widget.destroy()

        # -- read all subjects --
        all_subjects = service.get_all_subject()

        # -- create new subject buttons --
        for subject in all_subjects:
            button = ctk.CTkButton(
                self, 
                text=subject, 
                width=200, 
                height=100,
                font=(self.font_text, 25), 
                command=lambda m=subject: self.master.topic_menu(m)
            )
            button.pack(pady=5)


    def add_subject(self):
        new_subject = ctk.CTkToplevel()
        new_subject.title("Nuova Materia")

        ctk.CTkLabel(new_subject, text="Nome della Materia", font=(self.font_text, 25)).pack(pady=10)

        # -- input form --
        subject_name_entry = ctk.CTkEntry(new_subject, width=300)
        subject_name_entry.pack(pady=10)

        # -- confirm button --
        add_button = ctk.CTkButton(new_subject, text="Aggiungi", font=(self.font_text, 20), command=lambda: self.confirm_add(subject_name_entry.get(), new_subject))
        add_button.pack(pady=10)


    def confirm_add(self, subject_name, window):
        # -- check if the input is empty
        if subject_name:
            service.add_subject(subject_name)
            messagebox.showinfo("Successo", f"Nuova materia '{subject_name}' aggiunta!")
            self.update_subjects()
        else:
            messagebox.showwarning("Attenzione", "Il nome della materia non può essere vuoto.")
        window.destroy()
