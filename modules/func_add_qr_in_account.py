import customtkinter
import modules.functions as m_func
# import modules.functions_reg as m_func_reg
import modules.lists as m_lists
import modules.text_input as m_input
from PIL import Image
import os









def add_qr_in_account():
    if os.path.exists(path=f"json/{m_lists.login_of_user}.json"):
        dict1 = m_func.read_json(name_json=f"json/{m_lists.login_of_user}.json")
        # print(dict1)
        
        for arg in dict1.values():
            # print(arg)
            if not arg == m_lists.login_of_user:
                frame0 = customtkinter.CTkFrame(
                    master= m_input.frame_with_qrcodes,
                    width=60,
                    height= 60
                )
                frame0.grid(row=m_lists.index_of_column_for_qr, column = 0)
                
                m_lists.list_of_frames.append(frame0)
                
                image_of_qr = Image.open(arg)
                image = customtkinter.CTkImage(
                    light_image = image_of_qr,
                    size = (50, 50)
                )
                image_label = customtkinter.CTkLabel(
                    master= frame0,
                    text = "",
                    image = image,
                    bg_color='black'
                )
                image_label.grid(row= 0, column= 0)
                
                m_lists.index_of_column_for_qr += 1
               
               
        for key in dict1.keys():
            if not key == "login":
                # print(key)
                frame01 = customtkinter.CTkFrame(
                    master= m_input.frame_with_qrcodes,
                    width=60,
                    height= 60
                )
                frame01.grid(row=m_lists.index_of_column_for_text, column = 1)
                
                m_lists.list_of_frames.append(frame01)
                
                label_of_qr = customtkinter.CTkLabel(
                    master= frame01,
                    width=50,
                    height=50,
                    text=key
                )
                label_of_qr.grid(row=0, column = 1)
                
                m_lists.index_of_column_for_text += 1
                
                
                
def remove_history():
    for el in m_lists.list_of_frames:
        el.grid_forget()
        
    m_lists.index_of_column_for_text = 0
    m_lists.index_of_column_for_qr = 0