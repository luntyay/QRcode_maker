# регистрация
import modules.create_input as m_input
import modules.functions_reg as m_func_reg
# приложение
import customtkinter
import modules.screen_app as m_app
import modules.create_button as m_button
import modules.functions as m_func
import modules.create_tabview as m_tabview




customtkinter.set_appearance_mode("Dark")

m_app.main_app.iconbitmap("icon/icon.ico")
m_app.main_app_reg.iconbitmap("icon/icon.ico")



m_func_reg.create_users_table()
m_app.main_app_reg.mainloop()



