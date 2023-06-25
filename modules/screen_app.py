import customtkinter

class My_Frame(customtkinter.CTkFrame):
    def __init__(self, text, text_color, master, width, height, border_width, fg_color, **kwargs):
        super().__init__(master = master,
                        width = width, 
                        height = height, 
                        border_width = border_width, 
                        fg_color = fg_color,
                        **kwargs)

        self.LABEL = customtkinter.CTkLabel(self, text= text, text_color = text_color)
        self.LABEL.place(x= 480, y= 10)

class App(customtkinter.CTk):
    def __init__(self,app_width,app_height):
        super().__init__()
        self.APP_WIDTH = app_width
        self.APP_HEIGHT = app_height
        self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}")
        self.resizable(False, False)
        self.title("qrcoder")


        self.FRAME2 = My_Frame(text= "",
                                    #    text= "Генератор QR - code",
                                       text_color= "black", 
                                       master = self, 
                                       width= 980, 
                                       height= 680, 
                                       border_width= None,
                                       fg_color= None) 
        self.FRAME2.place(x=10, y=10) 
        
        
        
        self.FRAME3 = My_Frame(text= "", 
                                        text_color= "black", 
                                        master = self.FRAME2, 
                                        width= 150, 
                                        height= 150, 
                                        border_width= None,
                                        fg_color= "gray") 
        self.FRAME3.place(x = 820, y = 10)
        
        
        
        self.FRAME4 = My_Frame(text= "", 
                                        text_color= "black", 
                                        master = self.FRAME2, 
                                        width= 500, 
                                        height= 441, 
                                        border_width= None,
                                        fg_color= "gray") 
        self.FRAME4.place(x = 470, y = 170)
        
        
        
        # self.TEXT = customtkinter.StringVar()
        # self.FRAME5 = customtkinter.CTkEntry(
        #                                master = self.FRAME2, 
        #                                width= 390, 
        #                                height= 50, 
        #                             #    border_width= None, 
        #                             #    bg_color= None,
        #                                corner_radius=5,
        #                             #    text="Введіть url:",
        #                             #    border_color="black",
        #                                fg_color= "#696969",
        #                                textvariable= self.TEXT
        #                                )
        # self.FRAME5.focus_set()
        # # self.TEXT.set("Введіть url:")
        # self.FRAME5.place(x = 10, y = 10)

class App_reg(customtkinter.CTk):
    def __init__(self, app_width, app_height, color, x, y, **kwargs):
        super().__init__(**kwargs)
        self.APP_WIDTH = app_width
        self.APP_HEIGHT = app_height
        self.COLOR = color
        self.X = x
        self.Y = y
        self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}x{self.X}x{self.Y}")
        self.title("REG")
        self.config(bg=self.COLOR)
        self.resizable(False, False)
        
        
        
def on_close():
    main_app.destroy()
    main_app_reg.destroy()

def on_close2():
    main_app.destroy()
    main_app_reg.destroy()


main_app = App(1000, 700)
main_app_reg = App_reg(500, 500, "lightblue", 500, 500)

main_app.protocol("WM_DELETE_WINDOW", on_close)

main_app_reg.protocol("WM_DELETE_WINDOW", on_close2)