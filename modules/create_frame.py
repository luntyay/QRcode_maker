import customtkinter as ctk
import modules.screen_app as m_app



register_frame = ctk.CTkFrame(
    master= m_app.main_app_reg,
    width= 500,
    height= 450
)
# register_frame.place(x=0,y=50)

# register_label = ctk.CTkLabel(
#     master= register_frame,
#     width= 50,
#     height = 25,
#     text= "пвапавпвапв"
# )
# register_label.place(x=0, y=0)





login_frame = ctk.CTkFrame(
    master= m_app.main_app_reg,
    width= 500,
    height= 450
)
# login_frame.place(x=0,y=50)

# login_label = ctk.CTkLabel(
#     master= login_frame,
#     width= 50,
#     height = 25,
#     text= "Login"
# )
# login_label.place(x=0, y=0)



button_frame = ctk.CTkFrame(
    master= m_app.main_app_reg,
    width= 500,
    height= 50
)
button_frame.place(x=0, y=0)



# json_frame = ctk.CTkFrame(
#     master= m_app.main_app_reg,
#     width= 500,
#     height= 500
# )




class My_Frame(ctk.CTkFrame):
    def __init__(self, text, text_color, master, width, height, border_width, fg_color, **kwargs):
        super().__init__(master = master,
                        width = width, 
                        height = height, 
                        border_width = border_width, 
                        fg_color = fg_color,
                        **kwargs)

        self.LABEL = ctk.CTkLabel(self, text= text, text_color = text_color)
        self.LABEL.place(x= 480, y= 10)


class MessageFrame(ctk.CTkFrame):
    def __init__(self, text, master, width, height, border_width, bg_color, **kwargs):
        super().__init__(master= master, width= width, height= height, border_width= border_width, bg_color= bg_color, **kwargs)
        self.NAME = text
        self.FONT = ctk.CTkFont(family= "Arial", size= 20, weight= "bold") 
    def place_name(self):
        self.MESSAGE = ctk.CTkLabel(self, text= self.NAME)
        self.MESSAGE.place(x = 50, y = 10)
        
       
