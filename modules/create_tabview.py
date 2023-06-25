import customtkinter
import modules.screen_app as m_app



tabview = customtkinter.CTkTabview(
    master= m_app.main_app.FRAME2,
    width= 450,
    height= 600
)
tabview.place(x= 10, y= 70)

tabview.add("Дії з QR-кодом")
# tabview.add("колір ключа")
tabview.add("Історія акаунту")
# tabview.add("tab 3")
# tabview.add("tab 4")
# tabview.add("tab 5")
# tabview.set("tab 2")

# button_1 = customtkinter.CTkButton(tabview.tab("tab 1"))
# button_1.pack(padx=20, pady=20)
# button_2 = customtkinter.CTkButton(tabview.tab("tab 3"))
# button_2.pack(padx=20, pady=20)