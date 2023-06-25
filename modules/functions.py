import qrcode
import customtkinter
import aspose.words as aw
import tkinter
from tkinter import colorchooser
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import SolidFillColorMask
import modules.lists as m_lists
import modules.screen_app as m_app
from PIL import Image, ImageDraw, ImageOps
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

from qrcode import constants, exceptions, util
from qrcode.image.base import BaseImage
from qrcode.image.pure import PyPNGImage
import modules.text_input as m_input
import os
import json
import modules.func_add_qr_in_account as m_func_add_history



url = None
qr = None
cl_qr1 = None
qr1 = None
qr_version = None

image_of_profile = None

content = None

path_to_file_json = None


color_list = [None, (128, 128, 128), (255, 0, 255), (255, 0, 0), (255, 255, 0), (0, 255, 0), (0, 255, 255), (0, 0, 255), (255, 165, 0), (0, 0, 0)]

color_list_bg = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 255, 0), (0, 255, 255), (0, 0, 255), (255, 0, 255), (128, 128, 128), (0, 0, 0), (255, 255, 255), None, None]

def open_file():
    global file, content
    file = customtkinter.filedialog.askopenfile(mode ='r', filetypes =[('Файл "PNG"', '*.png'), ('Файл "JPG"', '*.jpg')])
    if file is not None:
        content = file.name
        # print(content)

def open_image_profile():
    global image_of_profile
    file = customtkinter.filedialog.askopenfile(mode ='r', filetypes =[('Файл "PNG"', '*.png'), ('Файл "JPG"', '*.jpg')])
    if file is not None:
        image_of_profile = file.name
        # print(content)
        # return content


def find_path_to_file(name_file):
    full_path = os.path.abspath(__file__ + "/..")
    full_path = full_path.split("\\")
    del full_path[-1]
    full_path = "/".join(full_path)
    full_path = os.path.join(full_path, name_file)
    return full_path
    

def create_json(name_json, name_dict):
    with open(find_path_to_file(name_file=name_json), "w") as file:
        json.dump(name_dict, file, indent=4, ensure_ascii=True)
        
def read_json(name_json):
    with open(find_path_to_file(name_json), "r") as file:
        data = json.load(file)
        return data


def iteration_of_list():
    dict_of_jsons = read_json(name_json=f"json/{m_lists.login_of_user}.json")
    for key in dict_of_jsons.keys():
        # print(el)
        if key == "login":
            continue
        m_lists.index_of_login += 1
        print(m_lists.index_of_login)
        # for arg in el.values():
        #     # print(arg)
        #     if arg == m_lists.login_of_user:
        #         break


def create_qrcode():
    global url, qr, qr_version
    
    if qr_version:
        qr = qrcode.QRCode(
            version= int(qr_version),
            error_correction = qrcode.constants.ERROR_CORRECT_L,
            box_size= 10,
            border= 1
        )
        
        qr.add_data(url)
        qr.make(fit=True)

        
        m_lists.color_of_bg = (255, 255, 255)
        m_lists.color_of_qr = (0, 0, 0)
        # color_list_bg[10] = None
        # color_list_bg[11] = None


        qr = qr.make_image(back_color=m_lists.color_of_bg, fill_color= m_lists.color_of_qr)
        m_lists.index += 1
        path_to_file = f"qrcodes/qrcode{m_lists.index}.png"
        qr.save(path_to_file)
        
        
        m_lists.var_for_entry_json = m_lists.var_for_entry
        
        
        

        # m_lists.list_of_dicts[m_lists.index_of_login][f"qrcode{m_lists.index}"] = path_to_file
        # create_json(name_json=f"json/{m_lists.login_of_user}.json", name_dict= m_lists.list_of_dicts[m_lists.index_of_login])

        image2 = Image.open(path_to_file)
        
        image = customtkinter.CTkImage(
                light_image = image2,
                size = (500, 441)
            )
        image_label = customtkinter.CTkLabel(
            master=m_app.main_app.FRAME4,
            text = "",
            image = image,
            bg_color='black'
        )
        image_label.grid(row= 5, column= 5)
        
        m_lists.list_of_grid_forget.append(image_label)
        
        
        m_lists.var_for_entry = None
        m_lists.QRCODE_EXISTS = True
        content = None
        m_lists.qr_version_dont_update = qr_version
        qr_version = None
        
        
        # m_lists.BG_COLOR_CHOSEN = False
        # m_lists.QR_COLOR_CHOSEN = False
        # print(m_lists.QR_COLOR_CHOSEN)
        # print(m_lists.BG_COLOR_CHOSEN)
        
        # remove_some_grid()
        # add_history()
        # m_input.text1.set("")
    
    

# def create_qrcode_color():
#     global url
#     if m_lists.index2 == 9:
#         m_lists.index2 = 0
#     m_lists.index2 += 1
#     print(m_lists.index2)
#     qr1 = qrcode.QRCode(
#         version= 1,
#         error_correction = qrcode.constants.ERROR_CORRECT_L,
#         box_size= 10,
#         border= 1
#     )
#     qr1.add_data(url)
#     qr1.make(fit=True)
#     cl_qr1 = qr1.make_image(image_factory=StyledPilImage, color_mask=SolidFillColorMask((255,255,255), color_list[m_lists.index2]))
    
#     m_lists.index += 1
#     path_to_file = f"qrcodes/qrcode{m_lists.index}.png"
#     cl_qr1.save(path_to_file)

#     image2 = Image.open(path_to_file)
    
#     image = customtkinter.CTkImage(
#             light_image = image2,
#             size = (500, 441)
#         )
#     image_label = customtkinter.CTkLabel(
#         master=m_app.main_app.FRAME4,
#         text = "",
#         image = image,
#         bg_color='black'
#     )
#     image_label.grid(row= 5, column= 5)
#     

def qr_img():
    global url, qr, qr_version
    if m_lists.QRCODE_EXISTS:
        open_file()
        #qr2.add_data(url)
        #qr2.make(fit=True)
        #qr2 = qr2.make_image(image_factory=StyledPilImage, color_mask=SolidFillColorMask(color_list_bg[m_lists.index_of_bg], color_list_bg[m_lists.index_of_fc]), embeded_image_path=content)

        qr2 = qrcode.QRCode(
            version= int(m_lists.qr_version_dont_update),
            error_correction = qrcode.constants.ERROR_CORRECT_L,
            box_size= 10,
            border= 1
        )
        # else:
        #     qr2 = qrcode.QRCode(
        #         version= 1,
        #         error_correction = qrcode.constants.ERROR_CORRECT_L,
        #         box_size= 10,
        #         border= 1
        #     )

        qr2.add_data(m_lists.var_for_entry_json)
        qr2.make(fit=True)
        qr2 = qr2.make_image(image_factory=StyledPilImage, color_mask=SolidFillColorMask(m_lists.color_of_bg, m_lists.color_of_qr))
        # m_lists.index += 1
        if content is not None:
            logo = Image.open(content)
            logo_size = 50
            width, height = qr2.size
            xmin = ymin = int((width / 2) - (logo_size / 2))
            xmax = ymax = int((width / 2) + (logo_size / 2))
            logo = logo.resize((xmax - xmin, ymax - ymin))
            qr2.paste(logo, (xmin, ymin, xmax, ymax))     
        path_to_file = f"qrcodes/qrcode{m_lists.index}.png"
        qr2.save(path_to_file)
        
        
        # path_to_file = f"{m_lists.login_of_user}_json_images/{m_lists.var_for_entry_json}.png"
        # qr2.save(path_to_file)
        
        
        # m_lists.list_of_dicts[m_lists.index_of_login][f"qrcode{m_lists.index}"] = path_to_file
        # create_json(name_json=f"json/{m_lists.login_of_user}.json", name_dict= m_lists.list_of_dicts[m_lists.index_of_login])

        image2 = Image.open(path_to_file)
        
        image = customtkinter.CTkImage(
                light_image = image2,
                size = (500, 441)
            )
        image_label = customtkinter.CTkLabel(
            master=m_app.main_app.FRAME4,
            text = "",
            image = image,
            bg_color='black'
        )
        image_label.grid(row= 5, column= 5)
        
        m_lists.list_of_grid_forget.append(image_label)
        
        # remove_some_grid()
        # add_history()
        #m_app.main_app.TEXT.set("")
    
    

    
    
def accept_url():
    global url
    if m_input.text1.get():
        url = m_input.text1.get()
        m_lists.var_for_entry = m_input.text1.get()
        # print(url)
        # m_app.main_app.TEXT.set("Введіть url:")
        m_input.text1.set("")
        m_lists.CAN_CHOOSE_VERSION = True
    





def create_qrcode_color_choose():
    global url, qr1, cl_qr1, qr_version
    if m_lists.QRCODE_EXISTS:
        try:
            qr1 = qrcode.QRCode(
                version= int(m_lists.qr_version_dont_update),
                error_correction = qrcode.constants.ERROR_CORRECT_L,
                box_size= 10,
                border= 1
            )
            qr1.add_data(url)
            qr1.make(fit=True)

            result = colorchooser.askcolor(initialcolor="black")
            color = result[0]

            m_lists.color_of_bg = color


            cl_qr1 = qr1.make_image(image_factory=StyledPilImage, color_mask=SolidFillColorMask(m_lists.color_of_bg, m_lists.color_of_qr))
            if content is not None:
                logo = Image.open(content)
                logo_size = 50
                width, height = cl_qr1.size
                xmin = ymin = int((width / 2) - (logo_size / 2))
                xmax = ymax = int((width / 2) + (logo_size / 2))
                logo = logo.resize((xmax - xmin, ymax - ymin))
                cl_qr1.paste(logo, (xmin, ymin, xmax, ymax))     

            path_to_file = f"qrcodes/qrcode{m_lists.index}.png"
            cl_qr1.save(path_to_file)
            
            image2 = Image.open(path_to_file)
            
            image = customtkinter.CTkImage(
                    light_image = image2,
                    size = (500, 441)
                )
            image_label = customtkinter.CTkLabel(
                master=m_app.main_app.FRAME4,
                text = "",
                image = image,
                bg_color='black'
            )
            image_label.grid(row= 5, column= 5)
            
            m_lists.list_of_grid_forget.append(image_label)
        except:
            if m_lists.color_of_bg == None:
                m_lists.color_of_bg = (255, 255, 255)
            else:
                pass

        










def create_bg_color_choose():
    global url, qr_version
    if m_lists.QRCODE_EXISTS:
        try:
            qr1 = qrcode.QRCode(
                version= int(m_lists.qr_version_dont_update),
                error_correction = qrcode.constants.ERROR_CORRECT_L,
                box_size= 10,
                border= 1
            )
            qr1.add_data(url)
            qr1.make(fit=True)
            result = colorchooser.askcolor(initialcolor="black")
            color = result[0]
            m_lists.color_of_qr = color

            qr1 = qr1.make_image(image_factory=StyledPilImage, color_mask=SolidFillColorMask(m_lists.color_of_bg, m_lists.color_of_qr))
            if content is not None:
                logo = Image.open(content)
                logo_size = 50
                width, height = qr1.size
                xmin = ymin = int((width / 2) - (logo_size / 2))
                xmax = ymax = int((width / 2) + (logo_size / 2))
                logo = logo.resize((xmax - xmin, ymax - ymin))
                qr1.paste(logo, (xmin, ymin, xmax, ymax))
            path_to_file = f"qrcodes/qrcode{m_lists.index}.png"
            qr1.save(path_to_file)

            
            image2 = Image.open(path_to_file)
            
            image = customtkinter.CTkImage(
                    light_image = image2,
                    size = (500, 441)
                )
            image_label = customtkinter.CTkLabel(
                master=m_app.main_app.FRAME4,
                text = "",
                image = image,
                bg_color='black'
            )
            image_label.grid(row= 5, column= 5)
            
            m_lists.list_of_grid_forget.append(image_label)
        
        except:
            if m_lists.color_of_qr == None:
                m_lists.color_of_qr = (0,0,0)
            else:
                pass
        # remove_some_grid()
        # add_history()
    #m_app.main_app.TEXT.set("")


def save_png():
    global url, qr_version, path_to_file_json
    if m_lists.QRCODE_EXISTS:
        qr1 = qrcode.QRCode(
            version= int(m_lists.qr_version_dont_update),
            error_correction = qrcode.constants.ERROR_CORRECT_L,
            box_size= 10,
            border= 1
        )
        qr1.add_data(url)
        qr1.make(fit=True)
        # print(color_list_bg[m_lists.index_of_bg], color_list_bg[m_lists.index_of_fc])
        
        # print(color_list_bg[m_lists.index_of_bg], color_list_bg[m_lists.index_of_fc])
        # print(m_lists.QR_COLOR_CHOSEN)
        # print(m_lists.BG_COLOR_CHOSEN)
        # if m_lists.QR_COLOR_CHOSEN and m_lists.BG_COLOR_CHOSEN:
        #     print(1)
        #     qr1 = qr1.make_image(image_factory=StyledPilImage, color_mask=SolidFillColorMask(color_list_bg[m_lists.index_of_bg], color_list_bg[m_lists.index_of_fc]), embeded_image_path=content)
        # if m_lists.QR_COLOR_CHOSEN and not m_lists.BG_COLOR_CHOSEN:
        #     print(2)
        #     qr1 = qr1.make_image(image_factory=StyledPilImage, color_mask=SolidFillColorMask((255, 255, 255), color_list_bg[m_lists.index_of_fc]), embeded_image_path=content)
        # if m_lists.BG_COLOR_CHOSEN and not m_lists.QR_COLOR_CHOSEN:
        #     print(3)
        #     qr1 = qr1.make_image(image_factory=StyledPilImage, color_mask=SolidFillColorMask(color_list_bg[m_lists.index_of_bg], (0,0,0)), embeded_image_path=content)
        # if not m_lists.QR_COLOR_CHOSEN and not m_lists.BG_COLOR_CHOSEN:
        #     print(4)
        #     qr1 = qr1.make_image(image_factory=StyledPilImage, color_mask=SolidFillColorMask((255,255,255), (0,0,0)), embeded_image_path=content)
        
        qr1 = qr1.make_image(image_factory=StyledPilImage, color_mask=SolidFillColorMask(m_lists.color_of_bg, m_lists.color_of_qr))
        if content is not None:
                logo = Image.open(content)
                logo_size = 50
                width, height = qr1.size
                xmin = ymin = int((width / 2) - (logo_size / 2))
                xmax = ymax = int((width / 2) + (logo_size / 2))
                logo = logo.resize((xmax - xmin, ymax - ymin))
                qr1.paste(logo, (xmin, ymin, xmax, ymax))
        path_to_file_json = m_lists.var_for_entry_json
        
        if '/' in m_lists.var_for_entry_json:
            # print(1)
            path_to_file_json = m_lists.var_for_entry_json.split('/')
            # print(path_to_file_json)
            path_to_file_json = "".join(path_to_file_json)
            # print(path_to_file_json)
        
        if ':' in m_lists.var_for_entry_json:
            path_to_file_json = path_to_file_json.split(':')
            path_to_file_json = "".join(path_to_file_json)
        
        if '*' in m_lists.var_for_entry_json:
            path_to_file_json = path_to_file_json.split("*")
            path_to_file_json = "".join(path_to_file_json)
        
        if '?' in m_lists.var_for_entry_json:
            path_to_file_json = path_to_file_json.split("?")
            path_to_file_json = "".join(path_to_file_json)
        
        if '"' in m_lists.var_for_entry_json:
            path_to_file_json = path_to_file_json.split('"')
            path_to_file_json = "".join(path_to_file_json)
        
        if '<' in m_lists.var_for_entry_json:
            path_to_file_json = path_to_file_json.split("<")
            path_to_file_json = "".join(path_to_file_json)
        
        if '>' in m_lists.var_for_entry_json:
            path_to_file_json = path_to_file_json.split(">")
            path_to_file_json = "".join(path_to_file_json)
        
        path_to_file = f"{m_lists.login_of_user}_json_images/{path_to_file_json}.png"
        qr1.save(path_to_file)
        m_lists.index_of_login += 1
        # iteration_of_list()
        print(m_lists.index_of_login)
        m_lists.dict_for_json[f"{m_lists.var_for_entry_json}"] = path_to_file
        
        if not os.path.exists(path=f"json/{m_lists.login_of_user}.json"):
            create_json(name_json=f"json/{m_lists.login_of_user}.json", name_dict= m_lists.dict_for_json)
            # print(2)
        else:
            dict1 = read_json(name_json=f"json/{m_lists.login_of_user}.json")
            dict1[m_lists.var_for_entry_json] = path_to_file
            # print(1, dict1)
            create_json(name_json=f"json/{m_lists.login_of_user}.json", name_dict= dict1)
        # m_lists.index += 1
        # path_to_file = f"qrcodes/qrcode{m_lists.index}.png"
        # qr1.save(path_to_file)

        image_origin = Image.open(path_to_file)


        fileTypes = [('Файл "PNG"', '*.png'),]
        fileName = customtkinter.filedialog.asksaveasfilename(initialdir = image_origin,  filetypes = fileTypes)
        # print(fileName)
        if fileName:
            image_origin.convert("RGB").save(f"{fileName}.png")
            m_lists.QRCODE_EXISTS = None
            # remove_some_grid()
            # add_history()
            m_func_add_history.remove_history()
            m_func_add_history.add_qr_in_account()
            
            
        

def save_jpeg():
    global url, qr_version
    if m_lists.QRCODE_EXISTS:
        qr1 = qrcode.QRCode(
            version= int(m_lists.qr_version_dont_update),
            error_correction = qrcode.constants.ERROR_CORRECT_L,
            box_size= 10,
            border= 1
        )
        qr1.add_data(url)
        qr1.make(fit=True)
        # print(color_list_bg[m_lists.index_of_bg], color_list_bg[m_lists.index_of_fc])
        
        # print(color_list_bg[m_lists.index_of_bg], color_list_bg[m_lists.index_of_fc])
        # if m_lists.QR_COLOR_CHOSEN and m_lists.BG_COLOR_CHOSEN:
        #     qr1 = qr1.make_image(image_factory=StyledPilImage, color_mask=SolidFillColorMask(color_list_bg[m_lists.index_of_bg], color_list_bg[m_lists.index_of_fc]), embeded_image_path=content)
        # if m_lists.QR_COLOR_CHOSEN and not m_lists.BG_COLOR_CHOSEN:
        #     qr1 = qr1.make_image(image_factory=StyledPilImage, color_mask=SolidFillColorMask((255, 255, 255), color_list_bg[m_lists.index_of_fc]), embeded_image_path=content)
        # if m_lists.BG_COLOR_CHOSEN and not m_lists.QR_COLOR_CHOSEN:
        #     qr1 = qr1.make_image(image_factory=StyledPilImage, color_mask=SolidFillColorMask(color_list_bg[m_lists.index_of_bg], (0,0,0)), embeded_image_path=content)
        # if not m_lists.QR_COLOR_CHOSEN and not m_lists.BG_COLOR_CHOSEN:
        #     qr1 = qr1.make_image(image_factory=StyledPilImage, color_mask=SolidFillColorMask((255,255,255), (0,0,0)), embeded_image_path=content)
        
        qr1 = qr1.make_image(image_factory=StyledPilImage, color_mask=SolidFillColorMask(m_lists.color_of_bg, m_lists.color_of_qr))
        if content is not None:
                logo = Image.open(content)
                logo_size = 50
                width, height = qr1.size
                xmin = ymin = int((width / 2) - (logo_size / 2))
                xmax = ymax = int((width / 2) + (logo_size / 2))
                logo = logo.resize((xmax - xmin, ymax - ymin))
                qr1.paste(logo, (xmin, ymin, xmax, ymax))
        # path_to_file = f"{m_lists.login_of_user}_json_images/{m_lists.var_for_entry_json}.png"
        # qr1.save(path_to_file)
        
        path_to_file_json = m_lists.var_for_entry_json
        
        if '/' in m_lists.var_for_entry_json:
            # print(1)
            path_to_file_json = m_lists.var_for_entry_json.split('/')
            # print(path_to_file_json)
            path_to_file_json = "".join(path_to_file_json)
            # print(path_to_file_json)
        
        if ':' in m_lists.var_for_entry_json:
            path_to_file_json = path_to_file_json.split(':')
            path_to_file_json = "".join(path_to_file_json)
        
        if '*' in m_lists.var_for_entry_json:
            path_to_file_json = path_to_file_json.split("*")
            path_to_file_json = "".join(path_to_file_json)
        
        if '?' in m_lists.var_for_entry_json:
            path_to_file_json = path_to_file_json.split("?")
            path_to_file_json = "".join(path_to_file_json)
        
        if '"' in m_lists.var_for_entry_json:
            path_to_file_json = path_to_file_json.split('"')
            path_to_file_json = "".join(path_to_file_json)
        
        if '<' in m_lists.var_for_entry_json:
            path_to_file_json = path_to_file_json.split("<")
            path_to_file_json = "".join(path_to_file_json)
        
        if '>' in m_lists.var_for_entry_json:
            path_to_file_json = path_to_file_json.split(">")
            path_to_file_json = "".join(path_to_file_json)
        
        path_to_file = f"{m_lists.login_of_user}_json_images/{path_to_file_json}.png"
        qr1.save(path_to_file)
        m_lists.index_of_login += 1
        # iteration_of_list()
        print(m_lists.index_of_login)
        m_lists.dict_for_json[f"{m_lists.var_for_entry_json}"] = path_to_file
        
        if not os.path.exists(path=f"json/{m_lists.login_of_user}.json"):
            create_json(name_json=f"json/{m_lists.login_of_user}.json", name_dict= m_lists.dict_for_json)
        else:
            dict1 = read_json(name_json=f"json/{m_lists.login_of_user}.json")
            dict1[m_lists.var_for_entry_json] = path_to_file
            create_json(name_json=f"json/{m_lists.login_of_user}.json", name_dict= dict1)

        image_origin = Image.open(path_to_file)

        
        fileTypes = [('Файл "JPEG"', '*.jpeg'),]
        fileName = customtkinter.filedialog.asksaveasfilename(initialdir = image_origin,  filetypes = fileTypes)
        # print(fileName)
        if fileName:
            image_origin.convert("RGB").save(f"{fileName}.jpeg")
            m_lists.QRCODE_EXISTS = None
            # remove_some_grid()
            # add_history()
            m_func_add_history.remove_history()
            m_func_add_history.add_qr_in_account()
            


def save_jpg():
    global url, qr_version
    if m_lists.QRCODE_EXISTS:

        qr1 = qrcode.QRCode(
            version= int(m_lists.qr_version_dont_update),
            error_correction = qrcode.constants.ERROR_CORRECT_L,
            box_size= 10,
            border= 1
        )

        qr1.add_data(url)
        qr1.make(fit=True)
        

        # if m_lists.QR_COLOR_CHOSEN and m_lists.BG_COLOR_CHOSEN:
        #     qr1 = qr1.make_image(image_factory=StyledPilImage, color_mask=SolidFillColorMask(color_list_bg[m_lists.index_of_bg], color_list_bg[m_lists.index_of_fc]), embeded_image_path=content)
        # if m_lists.QR_COLOR_CHOSEN and not m_lists.BG_COLOR_CHOSEN:
        #     qr1 = qr1.make_image(image_factory=StyledPilImage, color_mask=SolidFillColorMask((255, 255, 255), color_list_bg[m_lists.index_of_fc]), embeded_image_path=content)
        # if m_lists.BG_COLOR_CHOSEN and not m_lists.QR_COLOR_CHOSEN:
        #     qr1 = qr1.make_image(image_factory=StyledPilImage, color_mask=SolidFillColorMask(color_list_bg[m_lists.index_of_bg], (0,0,0)), embeded_image_path=content)
        # if not m_lists.QR_COLOR_CHOSEN and not m_lists.BG_COLOR_CHOSEN:
        #     qr1 = qr1.make_image(image_factory=StyledPilImage, color_mask=SolidFillColorMask((255,255,255), (0,0,0)), embeded_image_path=content)
        
        qr1 = qr1.make_image(image_factory=StyledPilImage, color_mask=SolidFillColorMask(m_lists.color_of_bg, m_lists.color_of_qr))
        if content is not None:
                logo = Image.open(content)
                logo_size = 50
                width, height = qr1.size
                xmin = ymin = int((width / 2) - (logo_size / 2))
                xmax = ymax = int((width / 2) + (logo_size / 2))
                logo = logo.resize((xmax - xmin, ymax - ymin))
                qr1.paste(logo, (xmin, ymin, xmax, ymax))
        # path_to_file = f"{m_lists.login_of_user}_json_images/{m_lists.var_for_entry_json}.png"
        # qr1.save(path_to_file)
        # path_to_file = f"{m_lists.login_of_user}_json_images/{m_lists.var_for_entry_json}.png"
        # qr1.save(path_to_file)
        

        
        path_to_file_json = m_lists.var_for_entry_json
        
        if '/' in m_lists.var_for_entry_json:
            # print(1)
            path_to_file_json = m_lists.var_for_entry_json.split('/')
            # print(path_to_file_json)
            path_to_file_json = "".join(path_to_file_json)
            # print(path_to_file_json)
        
        if ':' in m_lists.var_for_entry_json:
            path_to_file_json = path_to_file_json.split(':')
            path_to_file_json = "".join(path_to_file_json)
        
        if '*' in m_lists.var_for_entry_json:
            path_to_file_json = path_to_file_json.split("*")
            path_to_file_json = "".join(path_to_file_json)
        
        if '?' in m_lists.var_for_entry_json:
            path_to_file_json = path_to_file_json.split("?")
            path_to_file_json = "".join(path_to_file_json)
        
        if '"' in m_lists.var_for_entry_json:
            path_to_file_json = path_to_file_json.split('"')
            path_to_file_json = "".join(path_to_file_json)
        
        if '<' in m_lists.var_for_entry_json:
            path_to_file_json = path_to_file_json.split("<")
            path_to_file_json = "".join(path_to_file_json)
        
        if '>' in m_lists.var_for_entry_json:
            path_to_file_json = path_to_file_json.split(">")
            path_to_file_json = "".join(path_to_file_json)
        
        path_to_file = f"{m_lists.login_of_user}_json_images/{path_to_file_json}.png"
        qr1.save(path_to_file)
        m_lists.index_of_login += 1
        # iteration_of_list()
        print(m_lists.index_of_login)
        m_lists.dict_for_json[f"{m_lists.var_for_entry_json}"] = path_to_file
        
        if not os.path.exists(path=f"json/{m_lists.login_of_user}.json"):
            create_json(name_json=f"json/{m_lists.login_of_user}.json", name_dict= m_lists.dict_for_json)
            # print(2)
        else:
            dict1 = read_json(name_json=f"json/{m_lists.login_of_user}.json")
            dict1[m_lists.var_for_entry_json] = path_to_file
            # print(1, dict1)
            create_json(name_json=f"json/{m_lists.login_of_user}.json", name_dict= dict1)

        image_origin = Image.open(path_to_file)

        
        fileTypes = [('Файл "JPG"', '*.jpg'),]
        fileName = customtkinter.filedialog.asksaveasfilename(initialdir = image_origin,  filetypes = fileTypes)
        # print(fileName)
        if fileName:
            image_origin.convert("RGB").save(f"{fileName}.jpg")
            m_lists.QRCODE_EXISTS = None
            # remove_some_grid()
            # add_history()
            m_func_add_history.remove_history()
            m_func_add_history.add_qr_in_account()
            


def save_svg():
    global url, qr_version
    if m_lists.QRCODE_EXISTS:
        qr1 = qrcode.QRCode(
            version= int(m_lists.qr_version_dont_update),
            error_correction = qrcode.constants.ERROR_CORRECT_L,
            box_size= 10,
            border= 1
        )
        
        qr1.add_data(url)
        qr1.make(fit=True)



        # if m_lists.QR_COLOR_CHOSEN and m_lists.BG_COLOR_CHOSEN:
        #     qr1 = qr1.make_image(image_factory=StyledPilImage, color_mask=SolidFillColorMask(color_list_bg[m_lists.index_of_bg], color_list_bg[m_lists.index_of_fc]), embeded_image_path=content)
        # if m_lists.QR_COLOR_CHOSEN and not m_lists.BG_COLOR_CHOSEN:
        #     qr1 = qr1.make_image(image_factory=StyledPilImage, color_mask=SolidFillColorMask((255, 255, 255), color_list_bg[m_lists.index_of_fc]), embeded_image_path=content)
        # if m_lists.BG_COLOR_CHOSEN and not m_lists.QR_COLOR_CHOSEN:
        #     qr1 = qr1.make_image(image_factory=StyledPilImage, color_mask=SolidFillColorMask(color_list_bg[m_lists.index_of_bg], (0,0,0)), embeded_image_path=content)
        # if not m_lists.QR_COLOR_CHOSEN and not m_lists.BG_COLOR_CHOSEN:
        #     qr1 = qr1.make_image(image_factory=StyledPilImage, color_mask=SolidFillColorMask((255,255,255), (0,0,0)), embeded_image_path=content)
        
        qr1 = qr1.make_image(image_factory=StyledPilImage, color_mask=SolidFillColorMask(m_lists.color_of_bg, m_lists.color_of_qr))
        if content is not None:
                logo = Image.open(content)
                logo_size = 50
                width, height = qr1.size
                xmin = ymin = int((width / 2) - (logo_size / 2))
                xmax = ymax = int((width / 2) + (logo_size / 2))
                logo = logo.resize((xmax - xmin, ymax - ymin))
                qr1.paste(logo, (xmin, ymin, xmax, ymax))
        
        path_to_file_json = m_lists.var_for_entry_json
        
        if '/' in m_lists.var_for_entry_json:
            # print(1)
            path_to_file_json = m_lists.var_for_entry_json.split('/')
            # print(path_to_file_json)
            path_to_file_json = "".join(path_to_file_json)
            # print(path_to_file_json)
        
        if ':' in m_lists.var_for_entry_json:
            path_to_file_json = path_to_file_json.split(':')
            path_to_file_json = "".join(path_to_file_json)
        
        if '*' in m_lists.var_for_entry_json:
            path_to_file_json = path_to_file_json.split("*")
            path_to_file_json = "".join(path_to_file_json)
        
        if '?' in m_lists.var_for_entry_json:
            path_to_file_json = path_to_file_json.split("?")
            path_to_file_json = "".join(path_to_file_json)
        
        if '"' in m_lists.var_for_entry_json:
            path_to_file_json = path_to_file_json.split('"')
            path_to_file_json = "".join(path_to_file_json)
        
        if '<' in m_lists.var_for_entry_json:
            path_to_file_json = path_to_file_json.split("<")
            path_to_file_json = "".join(path_to_file_json)
        
        if '>' in m_lists.var_for_entry_json:
            path_to_file_json = path_to_file_json.split(">")
            path_to_file_json = "".join(path_to_file_json)
        
        path_to_file = f"{m_lists.login_of_user}_json_images/{path_to_file_json}.png"
        qr1.save(path_to_file)
        m_lists.index_of_login += 1
        # iteration_of_list()
        print(m_lists.index_of_login)
        m_lists.dict_for_json[f"{m_lists.var_for_entry_json}"] = path_to_file
        
        if not os.path.exists(path=f"json/{m_lists.login_of_user}.json"):
            create_json(name_json=f"json/{m_lists.login_of_user}.json", name_dict= m_lists.dict_for_json)
            # print(2)
        else:
            dict1 = read_json(name_json=f"json/{m_lists.login_of_user}.json")
            dict1[m_lists.var_for_entry_json] = path_to_file
            # print(1, dict1)
            create_json(name_json=f"json/{m_lists.login_of_user}.json", name_dict= dict1)

        image_origin = Image.open(path_to_file)

        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)

        
        fileTypes = [('Файл "SVG"', '*.svg'), ('Файл "PNG"', '*.png')]
        fileName = customtkinter.filedialog.asksaveasfilename(initialdir = image_origin,  filetypes = fileTypes)
        # print(fileName)
        if fileName:
            image_origin.convert("RGB").save(f"{fileName}.png")
            shape = builder.insert_image(f"{fileName}.png")
            shape.image_data.save(f"{fileName}.svg")
            os.remove(f"{fileName}.png")
            m_lists.QRCODE_EXISTS = None
            # remove_some_grid()
            # add_history()
            m_func_add_history.remove_history()
            m_func_add_history.add_qr_in_account()
            
        
        
def show_frame_with_versions():
    if m_lists.CAN_CHOOSE_VERSION:
        m_lists.FRAME_WITH_VERSIONS_IS_OPEN = True
        m_input.frame6.place(x=100, y=100)
# m_lists.var_for_entry and 

def close_frame_with_versions():
    if m_lists.FRAME_WITH_VERSIONS_IS_OPEN:
        m_input.frame6.place_forget()
        m_lists.FRAME_WITH_VERSIONS_IS_OPEN = False
        # m_lists.CAN_CHOOSE_VERSION = False
    

def accept_version():
    global qr_version
    version_var = m_input.text2.get()
    
    try:
        if int(version_var) in range(1, 41):
            m_input.label_error.place_forget()
            # m_input.label_correct.place(x=0, y=200)
            m_input.frame6.place_forget()
            qr_version = version_var
            m_input.text2.set("")
            m_lists.CAN_CHOOSE_VERSION = False
            close_frame_with_versions()
            m_lists.CAN_CHOOSE_VERSION = False
        else:
            m_input.label_error.place(x=0, y=200)
    except:
        m_input.label_error.place(x=0, y=200)



# def mini_qrcode():
#     global url, qr
#     # open_file()
#     qr2 = qrcode.QRCode(
#         version= 1,
#         error_correction = qrcode.constants.ERROR_CORRECT_L,
#         box_size= 2,
#         border= 1
#     )
#     qr2.add_data(url)
#     qr2.make(fit=True)
#     m_lists.color_of_bg = (255, 255, 255)
#     m_lists.color_of_qr = (0, 0, 0)

#     # qr2 = qr2.make_image(back_color=m_lists.color_of_bg, fill_color=m_lists.color_of_qr)
#     qr2 = qr2.make_image(image_factory=StyledPilImage, color_mask=SolidFillColorMask(color_list_bg[m_lists.index_of_bg], color_list_bg[m_lists.index_of_fc]))
#     if content is not None:
#                 logo = Image.open(content)
#                 logo_size = 50
#                 width, height = qr2.size
#                 xmin = ymin = int((width / 2) - (logo_size / 2))
#                 xmax = ymax = int((width / 2) + (logo_size / 2))
#                 logo = logo.resize((xmax - xmin, ymax - ymin))
#                 qr2.paste(logo, (xmin, ymin, xmax, ymax))
    
#     # m_lists.index += 1
#     path_to_file = f"qrcodes/qrcode{m_lists.index}.png"
#     qr2.save(path_to_file)

#     image2 = Image.open(path_to_file)
    
#     image = customtkinter.CTkImage(
#             light_image = image2,
#             size = (500, 441)
#         )
#     image_label = customtkinter.CTkLabel(
#         master=m_app.main_app.FRAME4,
#         text = "",
#         image = image,
#         bg_color='black'
#     )
#     image_label.grid(row= 5, column= 5)
    



# def add_history():
#     if os.path.exists(path=f"{m_lists.login_of_user}_json_images"):
#         m_lists.list_of_qr_for_history = os.listdir(f"{m_lists.login_of_user}_json_images")
        
#         # dict1 = m_func.read_json(name_json=f"json/{m_lists.login_of_user}.json")
#         # print(dict1)
        
#         for el in m_lists.list_of_qr_for_history:
#             # if not el == m_lists.login_of_user:
#             frame0 = customtkinter.CTkFrame(
#                 master= m_input.frame_with_qrcodes,
#                 width=60,
#                 height= 60
#             )
#             frame0.grid(row=m_lists.index_of_column_for_qr, column = 0)
            
#             m_lists.list_of_frames.append(frame0)
            
#             path_to_file = f"{m_lists.login_of_user}_json_images/{el}"
            
#             image_of_qr = Image.open(path_to_file)
#             image = customtkinter.CTkImage(
#                 light_image = image_of_qr,
#                 size = (50, 50)
#             )
#             image_label = customtkinter.CTkLabel(
#                 master= frame0,
#                 text = "",
#                 image = image,
#                 bg_color='black'
#             )
#             image_label.grid(row= 0, column= 0)
            
#             m_lists.index_of_column_for_qr += 1
               
               
#         for el in m_lists.list_of_qr_for_history:
#             frame01 = customtkinter.CTkFrame(
#                 master= m_input.frame_with_qrcodes,
#                 width=60,
#                 height= 60
#             )
#             frame01.grid(row=m_lists.index_of_column_for_text, column = 1)
            
#             m_lists.list_of_frames.append(frame01)
            
#             name_of_file = el.rsplit('.', 1)
#             name_of_file = name_of_file[0]
            
#             label_of_qr = customtkinter.CTkLabel(
#                 master= frame01,
#                 width=50,
#                 height=50,
#                 text=name_of_file
#             )
#             label_of_qr.grid(row=0, column = 1)
            
#             m_lists.index_of_column_for_text += 1


# def remove_some_grid():
#     for el in m_lists.list_of_frames:
#         el.grid_remove()
        

def change_profile_picture():
    global image_of_profile
    try:
        open_image_profile()
        
        profile_picture = Image.open(image_of_profile)
        
        path_to_file = f"{m_lists.login_of_user}_profile/{m_lists.login_of_user}.png"
        profile_picture.save(path_to_file)
        
        profile_picture = customtkinter.CTkImage(
            light_image=profile_picture,
            size=(150, 150)
        )
        
        profile_picture = customtkinter.CTkLabel(
            master=m_app.main_app.FRAME3,
            text="",
            image=profile_picture
        )
        profile_picture.place(x=0, y=0)
        
        m_lists.list_of_profile_pictures.append(profile_picture)
    except:
        pass
    
    
def add_profile_picture():
    if os.path.exists(f"{m_lists.login_of_user}_profile"):
        try:
            profile_picture = os.listdir(f"{m_lists.login_of_user}_profile")[0]
            profile_picture = Image.open(f"{m_lists.login_of_user}_profile/{profile_picture}")
            profile_picture = customtkinter.CTkImage(
                light_image=profile_picture,
                size=(150, 150)
            )
            
            profile_picture = customtkinter.CTkLabel(
                master=m_app.main_app.FRAME3,
                text="",
                image=profile_picture
            )
            profile_picture.place(x=0, y=0)
            
            m_lists.list_of_dir_profile.append(profile_picture)
        except:
            pass
        
        
def show_frame_with_manual():
    m_lists.FRAME_WITH_MANUAL_IS_OPEN = True
    m_input.frame_with_manual.place(x=100, y=100)
    
    
def close_frame_with_manual():
    if m_lists.FRAME_WITH_MANUAL_IS_OPEN:
        m_input.frame_with_manual.place_forget()
        m_lists.FRAME_WITH_MANUAL_IS_OPEN = False