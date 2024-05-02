import tkinter as tk
import tkinter.ttk as ttk

from src.shared.widgets import ToolTip




class ConnectionView(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=10)
        self.tooltip = ToolTip(self)
        
        self.setup_widgets()



    def setup_widgets(self):
        self._setup_conn_widget()
    

    def _setup_conn_widget(self):
        pad_option = {"padx":5,"pady":5,"ipadx":5,"ipady":5}
        entry_setting = {"font":('helvetica', 12, 'bold'),"justify":"center"}
        
        conn_frm = ttk.Frame(self,padding=5)
        conn_frm.grid(row=0,column=0,sticky=tk.NSEW)
        
        conn_frm.columnconfigure(0,weight=1)
        conn_frm.columnconfigure(1,weight=2)
        
        ttk.Label(conn_frm,text=_("IP"),style="n.TLabel",anchor=tk.CENTER).grid(row=0,column=0,sticky=tk.NSEW)
        self.ip_v = tk.StringVar()
        self.ip_entry = ttk.Entry(conn_frm,textvariable=self.ip_v,**entry_setting)
        self.ip_entry.grid(row=0,column=1,sticky=tk.NSEW)

        ttk.Label(conn_frm,text=_("USER"),style="n.TLabel",anchor=tk.CENTER).grid(row=1,column=0,sticky=tk.NSEW)
        self.user_v = tk.StringVar(value="admin")
        self.user_entry = ttk.Entry(conn_frm,textvariable=self.user_v,**entry_setting)
        self.user_entry.grid(row=1,column=1,sticky=tk.NSEW)

        ttk.Label(conn_frm,text=_("PASSWORD"),style="n.TLabel",anchor=tk.CENTER).grid(row=2,column=0,sticky=tk.NSEW)
        self.password_v = tk.StringVar()
        self.password_entry = ttk.Entry(conn_frm,textvariable=self.password_v,**entry_setting,show="*")
        self.password_entry.grid(row=2,column=1,sticky=tk.NSEW)

        self.show_pass_v = tk.BooleanVar(value=False)
        self.show_pass_ck_btn = ttk.Checkbutton(conn_frm,text=_("Show Pass"),variable=self.show_pass_v)
        self.show_pass_ck_btn.grid(row=3,column=1,**pad_option)

        self.keep_conn_v = tk.BooleanVar(value=False)
        keep_conn = ttk.Checkbutton(conn_frm,text=_("Keep Connection"),variable=self.keep_conn_v)
        keep_conn.grid(row=3,column=0,**pad_option)
        self.tooltip.bind(keep_conn, _("Auto login after 5min"))