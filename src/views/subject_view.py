import customtkinter as ctk
from tkinter import messagebox
from service import service

from views import constants as const

class SubjectFrame(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        # -- Top bar --
        top_bar = ctk.CTkFrame(self, height=50)
        top_bar.pack(fill="x", side="top")

        # -- Title of the page --
        title_label = ctk.CTkLabel(top_bar, text="Le Tue Materie", font=const.TITLE_FONT)
        title_label.pack(side="left", padx=10, pady=10)

        # -- Button '+' --
        add_button = ctk.CTkButton(top_bar, text="Nuova Materia", font=const.DEFAULT_FONT, width=40, command=self.add_subject)
        add_button.pack(side="right", padx=10, pady=10)

        # -- Display subjects --
        self.update_subjects()


    def update_subjects(self):
        """
        Aggiorna la lista dei pulsanti delle materie.
        """
        # Rimuove i pulsanti delle materie (se presenti)
        for widget in self.winfo_children():
            if isinstance(widget, ctk.CTkButton):
                widget.destroy()

        # Legge tutte le materie
        all_subjects = service.get_all_subject()

        # Crea nuovi pulsanti per ogni materia
        for subject in all_subjects:
            # Crea una cornice per ciascuna riga
            row_frame = ctk.CTkFrame(self)
            row_frame.pack(fill="x", pady=5)

            # Etichetta con il nome della materia (sinistra)
            subject_label = ctk.CTkLabel(row_frame, text=subject, font=const.DEFAULT_FONT)
            subject_label.pack(side="left", padx=10, pady=5, fill="x", expand=True)

            # Collega l’etichetta al menu della materia
            subject_label.bind("<Button-1>", lambda event, name=subject: self.master.topic_menu(name))

            # Pulsante per avviare le flashcard
            start_button = ctk.CTkButton(row_frame, text="Avvia", font=const.DEFAULT_FONT,
                                        command=lambda name=subject: self.start_flashcard(name))
            start_button.pack(side="right", padx=5)

            # Pulsante per modificare la materia
            edit_button = ctk.CTkButton(row_frame, text="Modifica", font=const.DEFAULT_FONT,
                                        command=lambda name=subject: self.edit_subject(name))
            edit_button.pack(side="right", padx=5)

            # Pulsante per eliminare la materia
            delete_button = ctk.CTkButton(row_frame, text="Elimina", font=const.DEFAULT_FONT,
                                        command=lambda name=subject: self.delete_subject(name))
            delete_button.pack(side="right", padx=5)


    def add_subject(self):
        """
        Apre una finestra per aggiungere una nuova materia.
        """
        new_subject = ctk.CTkToplevel()
        new_subject.title("Nuova Materia")

        ctk.CTkLabel(new_subject, text="Nome della Materia", font=(const.LABEL_FONT, 25)).pack(pady=10)

        # Input form
        subject_name_entry = ctk.CTkEntry(new_subject, width=300)
        subject_name_entry.pack(pady=10)

        # Confirm button
        add_button = ctk.CTkButton(
            new_subject, 
            text="Aggiungi", 
            font=const.LABEL_FONT, 
            command=lambda: self.confirm_add(subject_name_entry.get(), new_subject)
        )
        add_button.pack(pady=10)

    def confirm_add(self, subject_name, window):
        """
        Conferma e aggiunge una nuova materia.
        """
        # Verifica se l'input non è vuoto
        if subject_name:
            service.add_subject(subject_name)
            messagebox.showinfo("Successo", f"Nuova materia '{subject_name}' aggiunta!")
            self.update_subjects()
        else:
            messagebox.showwarning("Attenzione", "Il nome della materia non può essere vuoto.")
        window.destroy()
