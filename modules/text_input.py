import customtkinter
import modules.screen_app as m_app
import modules.create_tabview as m_tab
import modules.create_frame as m_c_frame

text1 = customtkinter.StringVar()
frame5 = customtkinter.CTkEntry(
                                master = m_app.main_app.FRAME2, 
                                width= 390, 
                                height= 50, 
                            #    border_width= None, 
                            #    bg_color= None,
                                corner_radius=5,
                            #    text="Введіть url:",
                            #    border_color="black",
                                fg_color= "#696969",
                                textvariable= text1
                                )
# frame5.focus_set()
# self.TEXT.set("Введіть url:")
frame5.place(x = 10, y = 10)


frame6 = customtkinter.CTkFrame(
    master=m_app.main_app,
    width=400,
    height=400,
)


label_version = customtkinter.CTkLabel(
    master= frame6,
    width=100,
    height=50,
    text="Напишіть версію qr-коду (від 1 до 40 включно)"
)
label_version.place(x=0, y=0)



text2 = customtkinter.StringVar()
frame7 = customtkinter.CTkEntry(
                                master = frame6, 
                                width= 100, 
                                height= 50, 
                            #    border_width= None, 
                            #    bg_color= None,
                                corner_radius=5,
                            #    text="Введіть url:",
                            #    border_color="black",
                                fg_color= "#696969",
                                textvariable= text2
                                )
# frame5.focus_set()
# self.TEXT.set("Введіть url:")
frame7.place(x = 10, y = 50)


label_error = customtkinter.CTkLabel(
    master= frame6,
    width=100,
    height=50,
    text= "Помилка! Введіть число від 1 до 40",
    text_color="red"
)


# label_correct = customtkinter.CTkLabel(
#     master= frame6,
#     width=100,
#     height=50,
#     text= "Версію прийнято",
#     text_color="green"
# )


# label_login_in_account_tabview = customtkinter.CTkLabel(
#     master= m_tab.tabview.tab("Історія акаунту"),
#     width=50,
#     height=25,
#     text="Login: login"
# )
# label_login_in_account_tabview.place(x=0, y=0)

frame_with_qrcodes = customtkinter.CTkScrollableFrame(
    master=m_tab.tabview.tab("Історія акаунту"),
    width= 410,
    height=490,
    label_text=f"Історія акаунту",
    label_fg_color="grey"
)

# frame_with_qrcodes.place(x=11, y=11,anchor = customtkinter.NW)
# frame_with_qrcodes._scrollbar.place(relx=0.9,rely = 0.01, anchor = customtkinter.NW)



frame_with_manual = customtkinter.CTkFrame(
    master=m_app.main_app,
    width=600,
    height=400
)


font1 = customtkinter.CTkFont(
    family="Arial",
    size=16,
    weight="bold"
)

label_first_step = customtkinter.CTkLabel(
    master=frame_with_manual,
    text="1. У поле вводу введіть дані, які ви хочете перетворити у QR-код.",
    font=font1
)
label_first_step.place(x=0, y=0)

label_second_step = customtkinter.CTkLabel(
    master=frame_with_manual,
    text='2. Коли Ви ввели дані, натисніть кнопку з назвою "Ввести дані".',
    font=font1
)
label_second_step.place(x=0, y=40)

label_third_step = customtkinter.CTkLabel(
    master=frame_with_manual,
    text='3. Оберіть версію QR-коду за допомогою кнопки "Обрати версію".',
    font=font1
)
label_third_step.place(x=0, y=80)

label_fourth_step = customtkinter.CTkLabel(
    master=frame_with_manual,
    text='4. Натисніть кнопку "Створити QR - code".',
    font=font1
)
label_fourth_step.place(x=0, y=120)

label_fifth_step = customtkinter.CTkLabel(
    master=frame_with_manual,
    text="5. За бажанням поміняйте кольори, додайте логотип.",
    font=font1
)
label_fifth_step.place(x=0, y=160)

label_sixth_step = customtkinter.CTkLabel(
    master=frame_with_manual,
    text='6. Збережіть QR-код за допомогою кнопок "SVG", "PNG", "JPG", "JPEG".',
    font=font1
)
label_sixth_step.place(x=0, y=200)


label_caution = customtkinter.CTkLabel(
    master=frame_with_manual,
    text="P.S. Після збереження QR-коду ви не зможете вносити до нього зміни!",
    font=font1,
    text_color="red"
)
label_caution.place(x=0, y=240)



font2 = customtkinter.CTkFont(
    family="Arial",
    size=14,
    weight="bold"
)


label_wrong_login_or_password = customtkinter.CTkLabel(
    master=m_c_frame.login_frame,
    text="Не вірний логін або пароль!",
    text_color="red",
    font=font2
)

label_login_exists = customtkinter.CTkLabel(
    master=m_c_frame.register_frame,
    text="Логін вже зареєстрований!",
    text_color="red",
    font=font2
)

label_email_exists = customtkinter.CTkLabel(
    master=m_c_frame.register_frame,
    text="Пошта вже зареєстрована!",
    text_color="red",
    font=font2
)

label_error_password = customtkinter.CTkLabel(
    master=m_c_frame.register_frame,
    text="Паролі не співпадають!",
    text_color="red",
    font=font2
)

label_account_has_been_created = customtkinter.CTkLabel(
    master=m_c_frame.register_frame,
    text="Акаунт було створено!",
    text_color="green",
    font=font2
)

label_login_is_too_long = customtkinter.CTkLabel(
    master=m_c_frame.register_frame,
    text="Логін не може бути більше 12 символів!",
    text_color="red",
    font=font2
)

label_entry_is_empty = customtkinter.CTkLabel(
    master=m_c_frame.register_frame,
    text="Поля вводу не можуть бути порожніми!",
    text_color="red",
    font=font2
)