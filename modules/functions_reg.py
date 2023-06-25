import modules.create_frame as m_frame
import modules.lists as m_lists
import sqlite3
import json
import customtkinter as ctk
import modules.create_input as m_input
import os
import modules.screen_app as m_app
import modules.text_input as m_text_input
import modules.functions as m_func
import modules.func_add_qr_in_account as m_func_add_qr

# # регистрация
# import tkinter as tk
# from tkinter import messagebox
# import sqlite3
# import json
# import modules_registr.create_app as m_app
# import modules_registr.create_frame as m_frame
# import modules_registr.create_button as m_button
# import modules_registr.create_input as m_input
# import modules_registr.functions as m_func
# # приложение
# import customtkinter
# import modules.screen_app as m_app_1
# import modules.create_button as m_button_1
# import modules.functions as m_func_1
# import modules.create_tabview as m_tabview_1



def grid_remove_frame():
    if m_lists.REGISTER_FRAME_SHOW_FLAG and not m_lists.LOGIN_FRAME_SHOW_FLAG:
        m_frame.login_frame.place_forget()
        m_frame.register_frame.place(x=0,y=50)
    if m_lists.LOGIN_FRAME_SHOW_FLAG and not m_lists.REGISTER_FRAME_SHOW_FLAG:
        m_text_input.label_account_has_been_created.place_forget()
        m_frame.register_frame.place_forget()
        m_frame.login_frame.place(x=0,y=50)


def register_frame_show():
    m_lists.REGISTER_FRAME_SHOW_FLAG = True
    m_lists.LOGIN_FRAME_SHOW_FLAG = False
    grid_remove_frame()
    
    
    
def login_frame_show():
    m_lists.LOGIN_FRAME_SHOW_FLAG = True
    m_lists.REGISTER_FRAME_SHOW_FLAG = False
    grid_remove_frame()
    
    
# def show_custom_messagebox(text):
#     # Створення нового вікна
#     messagebox = ctk.CTk()
#     messagebox.title("Повідомлення")

#     # Додавання тексту
#     label = ctk.CTkLabel(messagebox, text=text)
#     label.pack(padx=20, pady=20)

#     # Кнопка "ОК" для закриття вікна
#     ok_button = ctk.CTkButton(messagebox, text="OK", command=messagebox.destroy)
#     ok_button.pack(pady=10)

#     # Запуск головного циклу подій вікна
#     messagebox.mainloop()




 



    

    
# Функція для створення таблиці користувачів в базі даних SQLite
def create_users_table():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      login TEXT,
                      password TEXT,
                      email TEXT)''')

    conn.commit()
    conn.close()

# Функція для додавання нового користувача до бази даних SQLite
def add_user(login, password, email):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO users (login, password, email) VALUES (?, ?, ?)", (login, password, email))

    conn.commit()
    conn.close()


# def show_custom_messagebox(text):
#     # Створення нового вікна
#     messagebox = ctk.CTk()
#     # messagebox.geometry(f"{None}+{None}x{500}x{500}")
#     messagebox.title("Повідомлення")

#     # Додавання тексту
#     label = ctk.CTkLabel(messagebox, text=text)
#     label.pack(padx=20, pady=20)

#     # Кнопка "ОК" для закриття вікна
#     ok_button = ctk.CTkButton(messagebox, text="OK", command=messagebox.destroy)
#     ok_button.pack(pady=10)

#     # Запуск головного циклу подій вікна
#     messagebox.mainloop()


# Функція для отримання всіх користувачів з бази даних SQLite
def get_users():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    cursor.execute("SELECT login, password FROM users")
    users = cursor.fetchall()

    conn.close()

    return users

# Функція для збереження користувачів у JSON файл
# def save_users_to_json():
#     users = get_users()
    
#     dict1 = {}
    
#     for i in range(len(users)):
#         dict1[users[i][0]] = users[i][1]
    
#     with open('json/users.json', 'w') as file:
#         json.dump(dict1, file, indent=4, ensure_ascii=True)
        

def get_logins():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    cursor.execute("SELECT login FROM users")
    logins = cursor.fetchall()

    conn.close()

    return logins

# with open(find_path_to_file(name_file=name_json), "w") as file:
#     json.dump(name_dict, file, indent=4, ensure_ascii=True)

def get_emails():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    cursor.execute("SELECT email FROM users")
    emails = cursor.fetchall()

    conn.close()

    return emails


# def find_path_to_file(name_file):
#     full_path = os.path.abspath(__file__ + "/..")
#     full_path = full_path.split("\\")
#     del full_path[-1]
#     full_path = "/".join(full_path)
#     full_path = os.path.join(full_path, name_file)
#     return full_path


# Функція для створення нового акаунту
def create_account():
    m_text_input.label_login_exists.place_forget()
    m_text_input.label_email_exists.place_forget()
    m_text_input.label_error_password.place_forget()
    m_text_input.label_account_has_been_created.place_forget()
    m_text_input.label_login_is_too_long.place_forget()
    m_text_input.label_entry_is_empty.place_forget()
    
    
    login = m_input.text_input_register_login.get()
    password = m_input.text_input_register_password.get()
    # password1 = m_input.text_input_register_password.get()
    password2 = m_input.text_input_register_password_2.get()
    email =  m_input.text_input_register_email.get()
    
    logins = get_logins()
    emails = get_emails()
    
    # print(logins)
    # print(login)
    if not (login, ) in logins:
        if not (email, ) in emails:
            if password2 == password:
                if len(login) <= 12:
                    add_user(login, password, email)
                    m_text_input.label_account_has_been_created.place(x=250, y= 350)
    
    
    if (login, ) in logins:            
        m_text_input.label_login_exists.place(x=250, y=200)
    
    if (email, ) in emails:
        m_text_input.label_email_exists.place(x=250, y=250)
        
    if password2 != password:
        m_text_input.label_error_password.place(x=250, y=300)
    
    if len(login) > 12:
        m_text_input.label_login_is_too_long.place(x=210, y= 350)
    
    if login == '' or password == '' or password2 == '' or email == '':
        m_text_input.label_entry_is_empty.place(x=210, y=400)
    
        
    
    
    # if ("@") not in email:
    #     show_custom_messagebox("Неправельний E-mail!")
        

        
    # messagebox.showinfo("Успіх", "Акаунт створено успішно!")
    # show_custom_messagebox("Акаунт створено успішно!")

# Функція для входу в акаунт
def login_account():
    m_text_input.label_wrong_login_or_password.place_forget()
    
    
    login = m_input.text_input_login_login.get()
    password = m_input.text_input_login_password.get()

    users = get_users()
    # перевірка чи співпадає логін і пароль 
    if (login, password) in users:
        
        # messagebox.showinfo("Успіх", "Успішний вхід!")
        # show_custom_messagebox("Успішний вхід!")
        # Відкрийте нове вікно або виконайте потрібні дії після входу в акаунт
        open_frame_json()
    else:
        # messagebox.showerror("Помилка", "Неправильний логін або пароль!")    
        # show_custom_messagebox("Неправильний логін або пароль!!")
        # pass
        # show_custom_messagebox("Неправильний логін або пароль!!")
        m_text_input.label_wrong_login_or_password.place(x=250, y=300)

        

        
def open_frame_json():
    m_lists.LOGIN_FRAME_SHOW_FLAG = False
    m_lists.login_of_user = m_input.text_input_login_login.get()
    
    
    if not os.path.exists(f"{m_lists.login_of_user}_json_images"):
        os.makedirs(f"{m_lists.login_of_user}_json_images")
        
    if not os.path.exists(f"{m_lists.login_of_user}_profile"):
        os.makedirs(f"{m_lists.login_of_user}_profile")
    
    
    m_lists.login_label = ctk.CTkLabel(
        master= m_app.main_app.FRAME2,
        height=25,
        width=50,
        text=f"Логін: {m_lists.login_of_user}"
    )
    m_lists.login_label.place(x=660, y=130)

    

    m_lists.dict_for_json["login"] = f"{m_lists.login_of_user}"
    # m_lists.list_of_dicts.append(dict1)
    
    
    m_text_input.frame_with_qrcodes.place(x=0, y=0)
    m_text_input.frame_with_qrcodes._scrollbar.grid(padx = 0.001,pady = 1)
    
    # m_func.iteration_of_list()
    
    # m_func.add_history()
    m_func.add_profile_picture()
    
    m_func_add_qr.add_qr_in_account()
    
    m_app.main_app_reg.withdraw()
    m_app.main_app.deiconify()