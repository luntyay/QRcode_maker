import customtkinter as ctk
import modules.screen_app as m_app


register = ctk.CTkTabview(
    master= m_app.main_app_reg,
    width=75,
    height=50,
)

register.place(x=50, y=10)