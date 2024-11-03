import customtkinter as ctk
from views.subject_view import SubjectFrame
from views.topic_view import TopicFrame
from views import constants as const

class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode(const.DEFAULT_APPEARANCE_MODE)
        ctk.set_default_color_theme(const.DEFAULT_THEME)

        self.title('Flashcard')
        self.geometry(f'{const.WINDOW_WIDTH}x{const.WINDOW_HEIGHT}')
        self.minsize(const.MIN_WIDTH, const.MIN_HEIGHT)

        self.current_frame = None
        self.switch = None
        self.show_frame(SubjectFrame) # -- show the first page
        

    def toggle_theme(self):
        if ctk.get_appearance_mode() == "Dark":
            ctk.set_appearance_mode("Light")
        else:
            ctk.set_appearance_mode("Dark")


    def init_theme_switch(self):
        # inizalize the theme switch
        self.switch = ctk.CTkSwitch(self, text='Cambia Tema', font=const.DEFAULT_FONT, command=self.toggle_theme)
        self.switch.pack(pady=10)



    def show_frame(self, FrameClass, *args):
        '''
            Generic method to show a spcific frame

            Input:
                FrameClass  :   the class of the fram to show
                *args       :   additive args to pass to the frame
        '''

        # -- destroy current frame (if exist) --
        self.destroy_current_frame()

        self.current_frame = FrameClass(self, *args)
        self.current_frame.pack(fill="both", expand=True)
        self.init_theme_switch()



    def destroy_current_frame(self):
        if self.current_frame is not None:
            self.current_frame.destroy()
        
        if self.switch is not None:
            self.switch.destroy()

    
    # -- Wrapper Functions --
    def subject_menu(self):
        # Shows the main menu
        self.show_frame(SubjectFrame)

    def topic_menu(self, subject_name):
        # Show the subject menu
        self.show_frame(TopicFrame, subject_name)
