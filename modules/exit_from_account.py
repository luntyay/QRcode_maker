import customtkinter as ctk
import modules.functions as m_func
import modules.functions_reg as m_func_reg
import modules.lists as m_lists
import modules.screen_app as m_app
import modules.func_add_qr_in_account as m_func_add_history


def exit_from_acc_func():
    m_lists.LOGIN_FRAME_SHOW_FLAG = True
    m_lists.login_of_user = None
    m_lists.var_for_entry = None
    m_lists.var_for_entry_json = None
    m_lists.list_of_qrcodes = []
    m_lists.index = -1
    m_lists.QRCODE_EXISTS = None
    m_lists.color_of_bg = (255, 255, 255)
    m_lists.color_of_qr = (0, 0, 0)
    m_lists.index_of_login = -1
    # m_lists.list_of_dicts = []
    m_lists.index_of_column_for_qr = 0
    m_lists.index_of_column_for_text = 0
    
    m_func_add_history.remove_history()
    
    m_lists.list_of_frames = []
    m_lists.list_of_qr_for_history = []
    m_lists.qr_version_dont_update = None
    
    for el in m_lists.list_of_profile_pictures:
        el.place_forget()
    
    m_lists.list_of_profile_pictures = []
    
    for el in m_lists.list_of_dir_profile:
        el.place_forget()
    
    m_lists.list_of_dir_profile = []
    
    for el in m_lists.list_of_grid_forget:
        el.grid_forget()
    
    m_lists.list_of_grid_forget = []
    
    m_lists.login_label.place_forget()
    
    m_lists.login_label = None
    
    m_app.main_app.withdraw()
    m_app.main_app_reg.deiconify()
    
    m_func_reg.grid_remove_frame()
    
    m_func.close_frame_with_manual()
    m_func.close_frame_with_versions()