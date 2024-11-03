import customtkinter as ctk
from tkinter import messagebox
from service import service
from model.subject import Subject
from views import constants as const


class TopicFrame(ctk.CTkFrame):

    def __init__(self, master, subject_name):
        super().__init__(master)

        self.subject_name = subject_name

        # -- Top bar --
        top_bar = ctk.CTkFrame(self, height=50)
        top_bar.pack(fill="x", side="top")

        # -- Back button --
        back_button = ctk.CTkButton(
            top_bar, text='<', 
            font=const.BUTTON_FONT, 
            width=50, 
            command=lambda: master.subject_menu()
        )
        back_button.pack(side="left", padx=10, pady=10)

        # -- Title of the page --
        title_label = ctk.CTkLabel(
            top_bar,
            text=self.subject_name, 
            font=const.TITLE_FONT
        )
        title_label.pack(side="left", padx=10, pady=10)

        # -- Button '+' for adding a new topic --
        add_button = ctk.CTkButton(
            top_bar, text="Nuovo Argomento", 
            font=const.BUTTON_FONT, 
            width=40, 
            command=self.add_topic
        )
        add_button.pack(side="right", padx=10, pady=10)

        # -- Display topics --
        self.topics_container = ctk.CTkFrame(self)
        self.topics_container.pack(fill="both", expand=True)
        self.update_topics()


    def update_topics(self):
        """
        Aggiorna la lista dei pulsanti dei topic.
        """
        # Rimuove i pulsanti dei topic precedenti
        for widget in self.topics_container.winfo_children():
            widget.destroy()

        # Legge tutti i topic della materia
        subject = Subject(self.subject_name)
        all_topics = subject.get_all_topics()

        # Crea nuovi pulsanti per ogni topic
        for topic in all_topics:
            button = ctk.CTkButton(
                self.topics_container,
                text=topic,
                width=200,
                height=100,
                font=const.BUTTON_FONT
                # command=lambda t=topic: ... per futura navigazione
            )
            button.pack(pady=5)

    def add_topic(self):
        """
        Apre una finestra per aggiungere un nuovo argomento.
        """
        new_topic_window = ctk.CTkToplevel()
        new_topic_window.title("Nuovo Argomento")

        ctk.CTkLabel(
            new_topic_window, text="Nome dell'Argomento", 
            font=const.LABEL_FONT
        ).pack(pady=10)

        # Input form
        topic_name_entry = ctk.CTkEntry(new_topic_window, width=300)
        topic_name_entry.pack(pady=10)

        # Confirm button
        confirm_button = ctk.CTkButton(
            new_topic_window, text="Aggiungi", 
            font=const.BUTTON_FONT, 
            command=lambda: self.confirm_add(topic_name_entry.get(), new_topic_window)
        )
        confirm_button.pack(pady=10)

    def confirm_add(self, topic_name, window):
        """
        Conferma e aggiunge un nuovo argomento.
        """
        if topic_name:
            service.add_topic(self.subject_name, topic_name)
            messagebox.showinfo("Successo", f"Nuovo argomento '{topic_name}' aggiunto!")
            self.update_topics()
        else:
            messagebox.showwarning("Attenzione", "Il nome dell'argomento non può essere vuoto.")
        window.destroy()
