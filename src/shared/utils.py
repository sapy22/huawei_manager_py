import tkinter as tk




def disable_children_widgets(frm, exclude: tuple | None=None):
    for child in frm.winfo_children():
        wtype = child.winfo_class()
        if wtype not in ("Frame","TFrame","Labelframe","TLabelframe"):
            if exclude and child in exclude:
                continue
            child.configure(state="disable")
        else:
            disable_children_widgets(child, exclude)


def enable_children_widgets(frm, exclude: tuple | None=None):
    for child in frm.winfo_children():
        wtype = child.winfo_class()
        if wtype not in ("Frame","TFrame","Labelframe","TLabelframe"):
            if exclude and child in exclude:
                continue
            child.configure(state="normal")
        else:
            enable_children_widgets(child, exclude)


def center_window_on_screen(window):
    window.withdraw()
    window.update() 
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    window.geometry(f"+{x}+{y}")
    window.deiconify()


def center_window_on_master(window):
    window.withdraw()
    window.update()
    master_center_x = window.master.winfo_rootx() + (window.master.winfo_width() // 2)
    master_center_y = window.master.winfo_rooty() + (window.master.winfo_height() // 2) 
    x = master_center_x - (window.winfo_width() // 2)
    y = master_center_y - (window.winfo_height() // 2)
    window.geometry(f"+{x}+{y}")
    window.deiconify()


def show_message(msg_type: int, msg: str, parent=None):
    """ msg_type:
    0 = error
    1 = info
    2 = response
    3 = confirm
    """
    match msg_type:
        case 0:
            v = tk.messagebox.showerror(_("Error"),msg,parent=parent)
        case 1:
            v = tk.messagebox.showinfo(_("Info"),msg,parent=parent)
        case 2:
            v = tk.messagebox.showinfo(_("Response"),msg,parent=parent)
        case 3:
            v = tk.messagebox.askokcancel(_("Confirm"),msg,parent=parent)
    
    return v