import customtkinter as ctk
from tkinter import messagebox
from service import service
from views import constants as const

class Flashcard(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

