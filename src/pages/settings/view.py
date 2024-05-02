import tkinter as tk
import tkinter.ttk as ttk

from .tabs import ConnectionController, LanguageController, UIController




class SettingsView(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.setup_frames()
        self.setup_tabs_manager()
        self.setup_tabs()
        self.setup_widgets()


    def setup_frames(self):
        self.top_frm = ttk.Frame(self)
        self.top_frm.grid(row=0,column=0,sticky=tk.NSEW)
        self.top_frm.columnconfigure(0,weight=1)

        self.btm_frm = ttk.Frame(self)
        self.btm_frm.grid(row=1,column=0,sticky=tk.NSEW)
        self.btm_frm.columnconfigure(0,weight=1)


    def setup_tabs_manager(self):
        self.notebook = ttk.Notebook(self.top_frm)
        self.notebook.grid(row=0,column=0,sticky=tk.NSEW)
        

    def setup_tabs(self):
        self.connection_tab = ConnectionController(self.notebook)
        self.connection_tab.grid(row=0,column=0,sticky=tk.NSEW)
        self.connection_tab.columnconfigure(0,weight=1)
        self.notebook.add(self.connection_tab,text=_("Connection"))

        self.language_tab = LanguageController(self.notebook)
        self.language_tab.grid(row=0,column=0,sticky=tk.NSEW)
        self.language_tab.columnconfigure(0,weight=1)
        self.notebook.add(self.language_tab,text=_("Language"))

        self.ui_tab = UIController(self.notebook)
        self.ui_tab.grid(row=0,column=0,sticky=tk.NSEW)
        self.ui_tab.columnconfigure(0,weight=1)
        self.notebook.add(self.ui_tab,text=_("UI"))


    def setup_widgets(self):
        self._setup_save_widget()
    

    def _setup_save_widget(self):
        pad_option = {"padx":5,"pady":5,"ipadx":5,"ipady":5}

        save_frm = ttk.Frame(self.btm_frm,padding=10)
        save_frm.grid(row=0,column=0,sticky=tk.NSEW)
        save_frm.columnconfigure(0,weight=1)
       
        self.save_btn = ttk.Button(save_frm,text=_("Save"))
        self.save_btn.grid(row=0,column=0,**pad_option)