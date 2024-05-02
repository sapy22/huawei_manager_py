import tkinter as tk
import tkinter.ttk as ttk




class UIView(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=10)
        self.setup_widgets()


    def setup_widgets(self):
        self._setup_mode_widget()
        self._setup_graph_widget()


    def _setup_mode_widget(self):
        pad_option = {"padx":5,"pady":5,"ipadx":5,"ipady":5}
        
        mode_frm = ttk.Labelframe(self,text=_("Mode"),padding=5)
        mode_frm.grid(row=1,column=0,sticky=tk.NSEW)
        mode_frm.columnconfigure(0,weight=1)

        continer_frm = ttk.Frame(mode_frm)
        continer_frm.grid(row=0,column=0,sticky=tk.W)

        self.nr_5g_mode_v = tk.BooleanVar(value=True)
        ttk.Checkbutton(continer_frm,text=_("NR-5G"),variable=self.nr_5g_mode_v).grid(row=0,column=0,**pad_option)
    

    def _setup_graph_widget(self):
        pad_option = {"padx":5,"pady":5,"ipadx":5,"ipady":5}
        
        graph_frm = ttk.Labelframe(self,text=_("Graph"),padding=5)
        graph_frm.grid(row=2,column=0,sticky=tk.NSEW)
        graph_frm.columnconfigure(0,weight=1)

        continer_frm = ttk.Frame(graph_frm)
        continer_frm.grid(row=0,column=0,sticky=tk.W)

        self.rsrq_graph_v = tk.BooleanVar(value=True)
        ttk.Checkbutton(continer_frm,text=_("RSRQ"),variable=self.rsrq_graph_v).grid(row=0,column=0,**pad_option)
        
        self.rsrp_graph_v = tk.BooleanVar(value=True)
        ttk.Checkbutton(continer_frm,text=_("RSRP"),variable=self.rsrp_graph_v).grid(row=0,column=1,**pad_option)

        self.sinr_graph_v = tk.BooleanVar(value=True)
        ttk.Checkbutton(continer_frm,text=_("SINR"),variable=self.sinr_graph_v).grid(row=0,column=2,**pad_option)

        self.dl_ul_graph_v = tk.BooleanVar(value=True)
        ttk.Checkbutton(continer_frm,text=_("Download & Upload"),variable=self.dl_ul_graph_v).grid(row=0,column=3,**pad_option)