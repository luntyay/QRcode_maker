import customtkinter as ctk
import modules.screen_app as m_app
import modules.create_frame as m_frame


font1 = ctk.CTkFont(
    family="Calibri",
    size=20,
    weight="bold"
)


text_input_register_login = ctk.CTkEntry(
    master= m_frame.register_frame,
    width=200,
    height=50,
    font=font1
)
text_input_register_login.place(x=0, y=50)


label_login_register = ctk.CTkLabel(
    master= m_frame.register_frame,
    width=50,
    height=50,
    text="Логін"
)
label_login_register.place(x=0, y=0)



label_email_register = ctk.CTkLabel(
    master= m_frame.register_frame,
    width=50,
    height=50,
    text="E-mail"
)
label_email_register.place(x=0, y=100)

text_input_register_email = ctk.CTkEntry(
    master= m_frame.register_frame,
    width=200,
    height=50,
    font=font1
)
text_input_register_email.place(x=0, y=150)

label_password_register = ctk.CTkLabel(
    master= m_frame.register_frame,
    width=50,
    height=50,
    text="Пароль"
)
label_password_register.place(x=0, y=200)



text_input_register_password = ctk.CTkEntry(
    master= m_frame.register_frame,
    width=200,
    height=50,
    font=font1
)
text_input_register_password.place(x=0, y=250)

label_password_register = ctk.CTkLabel(
    master= m_frame.register_frame,
    width=50,
    height=50,
    text="Повторний пароль"
)
label_password_register.place(x=0, y=300)

text_input_register_password_2 = ctk.CTkEntry(
    master= m_frame.register_frame,
    width=200,
    height=50,
    font=font1
)
text_input_register_password_2.place(x=0, y=350)







text_input_login_login = ctk.CTkEntry(
    master= m_frame.login_frame,
    width=200,
    height=50,
    font=font1
)
text_input_login_login.place(x=0, y=50)

label_login_login = ctk.CTkLabel(
    master= m_frame.login_frame,
    width=50,
    height=50,
    text="Логін"
)
label_login_login.place(x=0, y=0)



label_password_login = ctk.CTkLabel(
    master= m_frame.login_frame,
    width=50,
    height=50,
    text="Пароль"
)
label_password_login.place(x=0, y=100)


text_input_login_password = ctk.CTkEntry(
    master= m_frame.login_frame,
    width=200,
    height=50,
    font=font1
)
text_input_login_password.place(x=0, y=150)



# text_input2 = ctk.CTkEntry(
#     master= m_app.main_app,
#     width=200,
#     height=50,
#     font=font1
# )

# text_input2.place(x=100, y=200)