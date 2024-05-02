import tkinter as tk
import tkinter.ttk as ttk

from src.shared.localize import lc_is_rtl_layout
from src.shared.utils import center_window_on_master




class GetView(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.setup_frames()
        self.setup_widgets()

    
    def setup_frames(self):
        frm = ttk.Frame(self)
        frm.grid()
        frm.rowconfigure(0,weight=1)

        self.content_frm = ttk.Frame(frm)
        self.content_frm.grid(row=0,column=0)

        self.side_bar = ttk.Frame(frm)
        self.side_bar.grid(row=0,column=1,padx=10,sticky=tk.N)


    def setup_widgets(self):
        self._setup_content_widget()
        self._setup_api_device_widget()
        self._setup_api_net_widget()
        self._setup_api_monitoring_widget()
        self._setup_api_dhcp_widget()


    def _setup_content_widget(self):
        v = ("name","value")
        if lc_is_rtl_layout():
            v = tuple(reversed(v))

        self.tree = ttk.Treeview(self.content_frm, columns=v, selectmode="browse", show="headings",height=20)
        self.tree.grid(row=0,column=0)

        tree_v_sb = ttk.Scrollbar(self.content_frm,orient="vertical", command=self.tree.yview)
        tree_v_sb.grid(row=0,column=1,sticky=tk.NSEW)
        self.tree.configure(yscrollcommand=tree_v_sb.set)
        
        self.tree.heading("name", text=_("Name"), anchor=tk.CENTER)
        self.tree.heading("value", text=_("Value"), anchor=tk.CENTER)

        self.tree.column("name", width=150, anchor=tk.CENTER,stretch=False)
        self.tree.column("value", width=600, anchor=tk.CENTER,stretch=False)
    

    def _setup_api_device_widget(self):
        pad_option = {"padx":5,"pady":5,"ipadx":5,"ipady":5}

        device_frm = ttk.Labelframe(self.side_bar,text="api/device",labelanchor=tk.NW)
        device_frm.grid(row=0,column=0,sticky=tk.NSEW)
        device_frm.columnconfigure(1,weight=1)

        continer_frm = ttk.Frame(device_frm)
        continer_frm.grid(row=0,column=0,sticky=tk.W)

        self.signal_btn = ttk.Button(continer_frm,text="signal")
        self.signal_btn.grid(row=0,column=0,**pad_option)

        self.information_btn = ttk.Button(continer_frm,text="information")
        self.information_btn.grid(row=0,column=1,**pad_option)


    def _setup_api_net_widget(self):
        pad_option = {"padx":5,"pady":5,"ipadx":5,"ipady":5}

        net_frm = ttk.Labelframe(self.side_bar,text="api/net",labelanchor=tk.NW)
        net_frm.grid(row=1,column=0,sticky=tk.NSEW)
        net_frm.columnconfigure(1,weight=1)

        continer_frm = ttk.Frame(net_frm)
        continer_frm.grid(row=0,column=0,sticky=tk.W)

        self.plmn_btn = ttk.Button(continer_frm,text="plmn")
        self.plmn_btn.grid(row=0,column=0,**pad_option)

        self.plmn_list_btn = ttk.Button(continer_frm,text="plmn_list")
        self.plmn_list_btn.grid(row=0,column=1,**pad_option)

        self.net_mode_btn = ttk.Button(continer_frm,text="net_mode")
        self.net_mode_btn.grid(row=1,column=0,**pad_option)

        self.net_mode_list_btn = ttk.Button(continer_frm,text="net_mode_list")
        self.net_mode_list_btn.grid(row=1,column=1,**pad_option)


    def _setup_api_monitoring_widget(self):
        pad_option = {"padx":5,"pady":5,"ipadx":5,"ipady":5}

        monitoring_frm = ttk.Labelframe(self.side_bar,text="api/monitoring",labelanchor=tk.NW)
        monitoring_frm.grid(row=2,column=0,sticky=tk.NSEW)
        monitoring_frm.columnconfigure(1,weight=1)

        continer_frm = ttk.Frame(monitoring_frm)
        continer_frm.grid(row=0,column=0,sticky=tk.W)

        self.status_btn = ttk.Button(continer_frm,text="status")
        self.status_btn.grid(row=0,column=0,**pad_option)

    
    def _setup_api_dhcp_widget(self):
        pad_option = {"padx":5,"pady":5,"ipadx":5,"ipady":5}

        dhcp_frm = ttk.Labelframe(self.side_bar,text="api/dhcp",labelanchor=tk.NW)
        dhcp_frm.grid(row=3,column=0,sticky=tk.NSEW)
        dhcp_frm.columnconfigure(1,weight=1)

        continer_frm = ttk.Frame(dhcp_frm)
        continer_frm.grid(row=0,column=0,sticky=tk.W)

        self.settings_btn = ttk.Button(continer_frm,text="settings")
        self.settings_btn.grid(row=0,column=0,**pad_option)


    def setup_content_window(self, text):
        pad_option = {"padx":5,"pady":5,"ipadx":5,"ipady":5}

        window = tk.Toplevel(self)
        window.overrideredirect(True)
        window.resizable(0,0)
        window.columnconfigure(0,weight=1)

        frm = ttk.Labelframe(window)
        frm.grid()

        ttk.Label(frm,text=text,wraplength=800,anchor="center").grid(row=0,column=0,**pad_option)

        ttk.Button(frm,text=_("Exit"),command=window.destroy).grid(row=1,column=0,**pad_option)

        center_window_on_master(window)

        window.grab_set()