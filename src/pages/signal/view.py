import tkinter as tk
import tkinter.ttk as ttk

from .tabs import MonitorController, StatisticsController

from src.shared.settings import resources_dir




class SignalView(ttk.Frame):
    def __init__(self, master, settings_data):
        super().__init__(master)
        self.settings_data = settings_data

        self.setup_tabs_manager()
        self.setup_tabs()
        self.setup_widgets()


    def setup_tabs_manager(self):
        self.notebook = ttk.Notebook(self)
        self.notebook.grid(row=1,column=0,sticky=tk.NSEW)


    def setup_tabs(self):
        self.monitor_tab = MonitorController(self.notebook,self.settings_data)
        self.monitor_tab.grid(row=0,column=0,sticky=tk.NSEW)
        self.monitor_tab.columnconfigure(0,weight=1)
        self.monitor_tab.rowconfigure(1,weight=1)
        self.notebook.add(self.monitor_tab,text=_("Monitor"))

        self.Statistics_tab = StatisticsController(self.notebook,self.settings_data)
        self.Statistics_tab.grid(row=0,column=0,sticky=tk.NSEW)
        self.Statistics_tab.columnconfigure(0,weight=1)
        self.notebook.add(self.Statistics_tab,text=_("Statistics"))


    def setup_widgets(self):
        pad_option = {"padx":5,"pady":5,"ipadx":1,"ipady":1}

        start_frm = ttk.Frame(self,padding=10)
        start_frm.grid(row=0,column=0)

        self.start_icon = tk.PhotoImage(file = resources_dir / "icons/start_24.png")
        self.start_btn = ttk.Button(start_frm,text=_("start"),image=self.start_icon)
        self.start_btn.grid(row=0,column=0,**pad_option)

        self.stop_icon = tk.PhotoImage(file = resources_dir / "icons/stop_24.png")
        self.stop_btn = ttk.Button(start_frm,text=_("stop"),state="disabled",image=self.stop_icon) 
        self.stop_btn.grid(row=0,column=2,**pad_option)
        
        self.app_runtime_v = tk.StringVar(value="0:00:00")
        ttk.Label(start_frm,textvariable=self.app_runtime_v).grid(row=0,column=1)