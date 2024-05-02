from .settings import get_layout_direction
from .constant import DirectionDict, StyleDict




def lc_is_rtl_layout() -> bool:
    if get_layout_direction() == DirectionDict.get("Right to Left"):
        return True

    return False


def lc_col(col_size, col) -> int:
    """Return the adjusted column index to reflect a right-to-left (RTL) layout"""
    # 0 1 2 3 <> 3 2 1 0
    return col_size - (col + 1) # +1 because 0 index


def lc_notebook(obj):
    """Change the Notebook widget style and reverse tabs order to reflect a right-to-left (RTL) layout"""
    obj.configure(style=StyleDict.get("RTL Notebook"))

    for i, tab in enumerate(reversed(obj.tabs())):
        obj.insert(i,tab)


def lc_btn(obj):
    """Change the Button widget pic side to reflect a right-to-left (RTL) layout"""
    if str(obj["compound"]) == "left":
        obj.configure(compound="right")


def lc_rd_btn(obj):
    """Change the Radiobutton widget style to reflect a right-to-left (RTL) layout"""
    obj.configure(style=StyleDict.get("RTL Radiobutton"))


def lc_chk_btn(obj):
    """Change the Checkbutton widget style to reflect a right-to-left (RTL) layout"""
    obj.configure(style=StyleDict.get("RTL Checkbutton"))


###################################################################################################################################

def _reconfigure_frm_columns_to_rtl(frm, col_size):
    cw_list = []
    for col in range(col_size):
        weight_v = frm.grid_columnconfigure(col)["weight"] 
        if weight_v > 0:
            cw_list.append((col,weight_v))
            frm.grid_columnconfigure(col,weight=0)

    for col, w in cw_list:
        frm.grid_columnconfigure(lc_col(col_size, col), weight=w)


def _reconfigure_frm_childs_to_rtl(frm, col_size, row_size):
    for row in range(row_size):
        w_list = [] # reset every row
        for col in range(col_size):
            try:
                for child in frm.grid_slaves(row,col):
                    if child.winfo_class() in ("Frame","TFrame","Labelframe","TLabelframe","TNotebook"):
                        regrid_frame(child)
                    

                    if child.grid_info() and child.grid_info()["sticky"] == "w": # continer frame
                        child.grid(sticky="e")

                    if child.winfo_class() in ("Labelframe","TLabelframe"):
                        child.configure(labelanchor="ne")

                    if child.winfo_class() == "TNotebook":
                        lc_notebook(child)

                    elif child.winfo_class() == "TButton":
                        lc_btn(child)

                    elif child.winfo_class() == "TRadiobutton":
                        lc_rd_btn(child)

                    elif child.winfo_class() == "TCheckbutton":
                        lc_chk_btn(child)

                    elif child.winfo_class() == "Canvas":
                        if child.class_name == "SignalBar":
                            child.change_to_rtl_layout()
                    #
                    w_list.append((child, col))

            except IndexError:
                pass
            except Exception as e:
                print(e,"_reconfigure_frm_childs_to_rtl")

        for w, col in w_list:
             w.grid(column=lc_col(col_size, col))


def regrid_frame(frm):
    if frm.winfo_class() == "TNotebook":
        for tab in frm.tabs():
            regrid_frame(frm.nametowidget(tab))

    if frm.winfo_class() in ("Frame","TFrame","Labelframe","TLabelframe"):

        col_size, row_size = frm.grid_size()

        _reconfigure_frm_columns_to_rtl(frm, col_size)

        _reconfigure_frm_childs_to_rtl(frm, col_size, row_size)