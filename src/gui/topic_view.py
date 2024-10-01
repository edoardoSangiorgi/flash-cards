import customtkinter as ctk
from tkinter import messagebox
from app import service
from model.subject import Subject

class TopicFrame(ctk.CTkFrame):

    def __init__(self, subject_name ,master):
        super().__init__(master)

        self.subject_name = subject_name

        self.font_title = 'DM Serif Display'
        self.font_text = 'Red Hat Display'

        # -- top bar --
        top_bar = ctk.CTkFrame(self, height=50)
        top_bar.pack(fill="x", side="top")

        # -- back button --
        back = ctk.CTkButton(top_bar, text='<', font=(self.font_text, 30), width=50, command=master.subject_menu)
        back.pack(side="left", padx=10, pady=10)

        # -- title of the page --
        title_label = ctk.CTkLabel(top_bar, text=self.subject_name, font=(self.font_title, 50))
        title_label.pack(side="left", padx=10, pady=10)

        # -- button '+' --
        add_button = ctk.CTkButton(top_bar, text="Nuovo Argomento", font=(self.font_text, 30), width=40, command=self.add_topic)
        add_button.pack(side="right", padx=10, pady=10)

        self.update_topics()


    def update_topics(self):
        '''
            update the topic button list
        '''
        # -- remove topic buttons (if present) --
        for widget in self.winfo_children():
            if isinstance(widget, ctk.CTkButton):
                widget.destroy()

        # -- read all topics --
        subject = Subject(self.subject_name)
        all_topics = subject.get_all_topics()

        # -- create new topic buttons --
        for topic in all_topics:
            button = ctk.CTkButton(
                self, 
                text=topic, 
                width=200, 
                height=100,
                font=(self.font_text, 25) 
                #command=lambda m=subject: self.master.topic_menu(m)
            )
            button.pack(pady=5)


    def add_topic(self):
        new_topic = ctk.CTkToplevel()
        new_topic.title("Nuovo Argomento")

        ctk.CTkLabel(new_topic, text="Nome dell'Argomento", font=(self.font_text, 25)).pack(pady=10)

        # -- input form --
        topic_name_entry = ctk.CTkEntry(new_topic, width=300)
        topic_name_entry.pack(pady=10)

        # -- confirm button --
        add_button = ctk.CTkButton(new_topic, text="Aggiungi", font=(self.font_text, 20), command=lambda: self.confirm_add(topic_name_entry.get(), new_topic))
        add_button.pack(pady=10)


    def confirm_add(self, topic_name, window):
        # -- check if the input is empty
        if topic_name:
            service.add_topic(self.subject_name, topic_name)
            messagebox.showinfo("Successo", f"Nuova materia '{topic_name}' aggiunta!")
            self.update_topics()
        else:
            messagebox.showwarning("Attenzione", "Il nome della materia non può essere vuoto.")
        window.destroy()



