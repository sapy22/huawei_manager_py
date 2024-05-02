import tkinter as tk
import tkinter.ttk as ttk

from src.shared.settings import resources_dir
from src.shared.localize import lc_is_rtl_layout, regrid_frame




class NavBar(ttk.Frame):
    def __init__(self,master):
        super().__init__(master,style="nav.TFrame")

        self.setup_nav_btns()
        self.check_locale()
    

    def setup_nav_btns(self):
        pad_option = {"padx":0,"pady":0,"ipadx":5,"ipady":7}
        
        continer_frm = ttk.Frame(self,style="nav.TFrame")
        continer_frm.grid(row=0,column=0,sticky=tk.W)

        self.signal_icon = tk.PhotoImage(file = resources_dir / "icons/signal_24.png")
        self.signal_btn = ttk.Button(continer_frm,text=_("Signal"),style="nav.TButton",image=self.signal_icon,compound=tk.LEFT)
        self.signal_btn.grid(row=0,column=0,**pad_option)
        
        self.band_select_icon = tk.PhotoImage(file = resources_dir / "icons/band_select_24.png")
        self.band_select_btn = ttk.Button(continer_frm,text=_("Band Select"),style="nav.TButton",image=self.band_select_icon,compound=tk.LEFT) 
        self.band_select_btn.grid(row=0,column=1,**pad_option)

        self.sms_icon = tk.PhotoImage(file = resources_dir / "icons/sms_24.png")
        self.sms_btn = ttk.Button(continer_frm,text=_("SMS"),style="nav.TButton",image=self.sms_icon,compound=tk.LEFT) 
        self.sms_btn.grid(row=0,column=2,**pad_option)

        self.advance_icon = tk.PhotoImage(file = resources_dir / "icons/advance_24.png")
        self.advance_btn = ttk.Button(continer_frm,text=_("Advance"),style="nav.TButton",image=self.advance_icon,compound=tk.LEFT) 
        self.advance_btn.grid(row=0,column=3,**pad_option)

        self.settings_icon = tk.PhotoImage(file = resources_dir / "icons/settings_24.png")
        self.settings_btn = ttk.Button(continer_frm,text=_("Settings"),style="nav.TButton",image=self.settings_icon,compound=tk.LEFT)
        self.settings_btn.grid(row=0,column=4,**pad_option)

        self.about_icon = tk.PhotoImage(file = resources_dir / "icons/about_24.png")
        self.about_btn = ttk.Button(continer_frm,text=_("About"),style="nav.TButton",image=self.about_icon,compound=tk.LEFT)
        self.about_btn.grid(row=0,column=5,**pad_option)
    

    def check_locale(self):
        if lc_is_rtl_layout():
            regrid_frame(self)