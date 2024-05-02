import tkinter as tk
import tkinter.ttk as ttk

from .tabs import GetController, SetController




class AdvanceView(ttk.Frame):
    def __init__(self, master, settings_data):
        super().__init__(master)
        self.settings_data = settings_data

        self.setup_tabs_manager()
        self.setup_tabs()
    

    def setup_tabs_manager(self):
        self.notebook = ttk.Notebook(self)
        self.notebook.grid(row=0,column=0,pady=20)
        

    def setup_tabs(self):
        self.get_tab = GetController(self.notebook, self.settings_data)
        self.get_tab.grid(row=0,column=0,sticky=tk.NSEW)
        self.get_tab.columnconfigure(0,weight=1)
        self.notebook.add(self.get_tab,text=_("Get"))

        self.set_tab = SetController(self.notebook, self.settings_data)
        self.set_tab.grid(row=0,column=0,sticky=tk.NSEW)
        self.set_tab.columnconfigure(0,weight=1)
        self.notebook.add(self.set_tab,text=_("Set"))