import tkinter as tk
import tkinter.ttk as ttk

from src.shared.constant import COUNTRIES



class UIView(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=10)
        self.setup_frames()
        self.setup_widgets()


    def setup_frames(self):
        self.top_frm = ttk.Frame(self)
        self.top_frm.grid(row=0,column=0,sticky=tk.NSEW)
        self.top_frm.columnconfigure(1,weight=1)

        self.btm_frm = ttk.Frame(self)
        self.btm_frm.grid(row=1,column=0,sticky=tk.NSEW)
        self.btm_frm.columnconfigure(0,weight=1)


    def setup_widgets(self):
        self._setup_mode_widget()
        self._setup_country_widget()
        self._setup_graph_widget()


    def _setup_mode_widget(self):
        pad_option = {"padx":5,"pady":5,"ipadx":5,"ipady":5}
        
        mode_frm = ttk.Labelframe(self.top_frm,text=_("Mode"),padding=5)
        mode_frm.grid(row=0,column=0,sticky=tk.NSEW)
        mode_frm.columnconfigure(0,weight=1)

        continer_frm = ttk.Frame(mode_frm)
        continer_frm.grid(row=0,column=0,sticky=tk.W)

        self.nr_5g_mode_v = tk.BooleanVar(value=True)
        ttk.Checkbutton(continer_frm,text=_("NR-5G"),variable=self.nr_5g_mode_v).grid(row=0,column=0,**pad_option)
    

    def _setup_country_widget(self):
        pad_option = {"padx":5,"pady":5,"ipadx":5,"ipady":5}

        bh_frm = ttk.Labelframe(self.top_frm,text=_("Band Hint"),padding=5)
        bh_frm.grid(row=0,column=1,sticky=tk.NSEW,padx=5)
        bh_frm.columnconfigure(1,weight=1)

        ttk.Label(bh_frm,text=_("Country")).grid(row=0,column=0)

        self.country_cb = ttk.Combobox(bh_frm,justify="center",state="readonly")
        self.country_cb.grid(row=0,column=1,sticky=tk.NSEW,**pad_option)

        self.country_cb["values"] = COUNTRIES


    def _setup_graph_widget(self):
        pad_option = {"padx":5,"pady":5,"ipadx":5,"ipady":5}
        
        graph_frm = ttk.Labelframe(self.btm_frm,text=_("Graph"),padding=5)
        graph_frm.grid(row=0,column=0,sticky=tk.NSEW)
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