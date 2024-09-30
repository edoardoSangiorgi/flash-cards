import tkinter as tk
from tkinter import messagebox
from app import service


class SubjectFrame(tk.Frame):

    def __init__(self, master):
        super().__init__(master)

        color = 'darkgray'
        font_type = 'Georgia'
        
        # -- top bar --
        top_bar = tk.Frame(self, bg=color, height=50)
        top_bar.pack(fill="x", side="top")

        # -- title of the page --
        title_label = tk.Label(top_bar, text="Materie", font=(font_type, 24), bg=color)
        title_label.pack(side="left", padx=10, pady=10)

        # -- button '+' --
        add_button = tk.Button(top_bar, text="+", font=(font_type, 18), bg=color, command=self.add_subject)
        add_button.pack(side="right", padx=10, pady=10)

        # read all subject
        all_subjects = service.get_all_subject()

        # create all the button - one for each subject
        self.update_subjects()


    def update_subjects(self):

        # -- remove subject buttons (if present) --
        for widget in self.winfo_children():
            if isinstance(widget, tk.Button):
                widget.destroy()

        # -- read all subjects --
        all_subjects = service.get_all_subject()

        # -- create new subject buttons --
        for subject in all_subjects:
            button = tk.Button(
                self, 
                text=subject, 
                width=20, 
                height=2, 
                command=lambda m=subject: self.master.topic_menu(m)
            )
            button.pack(pady=5)


    def add_subject(self):

        new_subject = tk.Toplevel()
        new_subject.title("Nuova Materia")
        tk.Label(new_subject, text="Nome").pack(pady=10)

        # -- input form --
        subject_name_entry = tk.Entry(new_subject, width=30)
        subject_name_entry.pack(pady=10)

        # -- confirm button --
        add_button = tk.Button(new_subject, text="Aggiungi", command=lambda: self.confirm_add(subject_name_entry.get(), new_subject))
        add_button.pack(pady=10)


    def confirm_add(self, subject_name, window):

        # -- check if the input is empty
        if subject_name:
            service.add_subject(subject_name)
            messagebox.showinfo("Successo", f"Nuova materia '{subject_name}' aggiunta!")

            # -- update the list of the subjects --
            self.update_subjects()

        else:
            messagebox.showwarning("Attenzione", "Il nome della materia non può essere vuoto.")

        window.destroy()