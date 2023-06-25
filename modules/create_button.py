import customtkinter as ctk 
import modules.screen_app as m_app
import modules.functions as m_func
import modules.create_tabview as m_tab


import customtkinter as ctk
import modules.functions_reg as m_func_reg
import modules.create_frame as m_frame
import modules.text_input as m_input
import modules.exit_from_account as m_exit



# def send_data():
    
#     dict1 = {
#         "login": "",
#         "password": ""
#     }
    
#     m_lists.list_with_jsons.append(dict1)
#     m_lists.index += 1
    
#     m_lists.list_with_jsons[-1]["login"] = m_ci.text_input.get()
#     m_lists.list_with_jsons[-1]["password"] = m_ci.text_input2.get()
    
    
#     m_paj.create_json(name_json=f"json/data{m_lists.index}.json", name_dict=dict1)
#     m_ci.text_input.delete(0, ctk.END)
#     data = m_paj.read_json(name_json=f"json/data{m_lists.index}.json")
#     print(json.dumps(data, indent=4))
   

# button_send = ctk.CTkButton(
#     master= m_app.main_app,
#     width=50,
#     height=50,
#     border_width=3,
#     border_color="darkorange",
#     text="Відправити",
#     fg_color="orange",
#     command= send_data
# )
# button_send.place(x=200, y=350)










def create_button(master, text, command, width, height, image, corner_radius = 5, fg_color = "gray21"):
    button = ctk.CTkButton(master = master,
                           width = width,
                           height = height,
                           corner_radius = corner_radius,
                        #    border_width= 1,
                        #    border_color="black",
                           text = text,
                           fg_color= fg_color,
                           image = image,
                           hover_color = "gray12",
                           command= command
    )
    return button
# "#696969"

button_register_frame = create_button(
    master= m_frame.button_frame,
    width=100,
    height=50,
    text="Реєстрація",
    command= m_func_reg.register_frame_show,
    image = None,
    fg_color="grey"
)
button_register_frame.place(x=125, y=0)


button_login_frame = create_button(
    master= m_frame.button_frame,
    width=100,
    height=50,
    text="Авторизація",
    command= m_func_reg.login_frame_show,
    fg_color="grey",
    image = None
)
button_login_frame.place(x=275, y=0)



button_send_register = create_button(
    master= m_frame.register_frame,
    width=100,
    height=50,
    text= "Зареєструватися",
    command=m_func_reg.create_account,
    fg_color="grey",
    image = None
)
button_send_register.place(x=300, y=100)




button_send_login = create_button(
    master= m_frame.login_frame,
    width=100,
    height=50,
    text= "Авторизуватися",
    command=m_func_reg.login_account,
    fg_color="grey",
    image = None
)
button_send_login.place(x=300, y=100)




button6 = create_button(
    master= m_app.main_app.FRAME2,
    text= "Створити QR - code",
    command = m_func.create_qrcode,
    width= 500,
    height= 50,
    image = None,
    fg_color="grey"
)
button6.place(x = 470, y = 621)

button18 = create_button(
    master=m_tab.tabview.tab("Дії з QR-кодом"),
    # text= "Зберегти QR - code(PNG)",
    text= "PNG",
    command = m_func.save_png,
    width= 100,
    height= 50,
    image = None,
    fg_color="grey"
)
button18.place(x = 10, y = 500)

button19 = create_button(
    master= m_tab.tabview.tab("Дії з QR-кодом"),
    # text= "Зберегти QR - code(JPEG)",
    text= "JPEG",
    command = m_func.save_jpeg,
    width= 100,
    height= 50,
    image = None,
    fg_color="grey"
)
button19.place(x = 115, y = 500)

button20 = create_button(
    master= m_tab.tabview.tab("Дії з QR-кодом"),
    # text= "Зберегти QR - code(JPG)",
    text= "JPG",
    command = m_func.save_jpg,
    width= 100,
    height= 50,
    image = None,
    fg_color="grey"
)
button20.place(x = 220, y = 500)

button21 = create_button(
    master= m_tab.tabview.tab("Дії з QR-кодом"),
    # text= "Зберегти QR - code(SVG)",
    text= "SVG",
    command = m_func.save_svg,
    width= 100,
    height= 50,
    image = None,
    fg_color="grey"
)
button21.place(x = 325, y = 500)

button7 = create_button(
    master= m_app.main_app.FRAME2,
    text= "Ввести дані",
    command = m_func.accept_url,
    width= 50,
    height= 50,
    image = None,
    fg_color="grey"
)
button7.place(x = 410, y = 10) 




button_choose_qr = create_button(
    master= m_tab.tabview.tab("Дії з QR-кодом"),
    text= "Вибрати колір заднього фону",
    command = m_func.create_qrcode_color_choose,
    width= 420,
    fg_color= "grey",
    height= 50,
    image = None
)
button_choose_qr.place(x = 10, y = 10) 


button_choose_bg = create_button(
    master= m_tab.tabview.tab("Дії з QR-кодом"),
    text= "Вибрати колір ключа",
    command = m_func.create_bg_color_choose,
    width= 420,
    fg_color= "grey",
    height= 50,
    image = None
)
button_choose_bg.place(x = 10, y = 70)













# button_version_entry = create_button(
#     master= m_tab.tabview.tab("Дії з QR-кодом"),
#     text= "Створіть мікро QR-код",
#     command = m_func.mini_qrcode,
#     fg_color="grey",
#     height=50,
#     width= 420,
#     image= None
# )
# button_version_entry.place(x = 10, y = 190)

button9 = create_button(
    master= m_tab.tabview.tab("Дії з QR-кодом"),
    text= "Додати логотип",
    command = m_func.qr_img,
    width= 420,
    fg_color= "grey",
    height= 50,
    image = None
)
button9.place(x = 10, y = 190) 




button4 = create_button(
    master= m_app.main_app.FRAME2,
    text= "Вихід",
    command = m_exit.exit_from_acc_func,
    width= 150,
    height= 50,
    image = None,
    fg_color="grey"
)
button4.place(x= 660, y= 10)


button_change_profile_picture = create_button(
    master=m_app.main_app.FRAME2,
    text="Змінити фото профілю",
    command = m_func.change_profile_picture,
    width= 150,
    height= 50,
    image = None,
    fg_color="grey"
)
button_change_profile_picture.place(x=660, y=70)


button_version_entry = create_button(
    master= m_tab.tabview.tab("Дії з QR-кодом"),
    text= "Обрати версію",
    command = m_func.show_frame_with_versions,
    fg_color="grey",
    height=50,
    width= 420,
    image= None
)
button_version_entry.place(x = 10, y = 130)


button_close_frame_with_versions = create_button(
    master= m_input.frame6,
    width=50,
    height=50,
    text="X",
    command=m_func.close_frame_with_versions,
    image=None,
    fg_color="red"
)
button_close_frame_with_versions.place(x=350, y=0)

button_accept_version = create_button(
    master= m_input.frame6,
    width=150,
    height=50,
    text="Обрати версію",
    command=m_func.accept_version,
    image=None
    # fg_color="grey"
)
button_accept_version.place(x=10, y=300)


button_show_manual = create_button(
    master=m_tab.tabview.tab("Дії з QR-кодом"),
    text="Інструкція",
    command = m_func.show_frame_with_manual,
    width=420,
    height=50,
    image=None,
    fg_color="grey"
)
button_show_manual.place(x=10, y=250)

button_close_frame_with_manual = create_button(
    master= m_input.frame_with_manual,
    width=50,
    height=50,
    text="X",
    command=m_func.close_frame_with_manual,
    image=None,
    fg_color="red"
)
button_close_frame_with_manual.place(x=550, y=0)