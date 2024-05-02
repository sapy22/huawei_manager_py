import tkinter as tk
import tkinter.ttk as ttk




class SetView(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.setup_frames()
        self.setup_widgets()

    
    def setup_frames(self):
        self.content_frm = ttk.Frame(self)
        self.content_frm.grid(row=0,column=0)


    def setup_widgets(self):
        self._setup_power_widget()
        self._setup_dns_widget()


    def _setup_power_widget(self):
        pad_option = {"padx":5,"pady":5,"ipadx":5,"ipady":5}

        power_frm = ttk.Labelframe(self.content_frm,text=_("Power"),labelanchor=tk.NW)
        power_frm.grid(row=0,column=0,sticky=tk.NSEW,padx=10)

        self.power_shutdown_btn = ttk.Button(power_frm,text=_("ShutDown"))
        self.power_shutdown_btn.grid(row=0,column=0,**pad_option)

        self.power_restart_btn = ttk.Button(power_frm,text=_("Restart"))
        self.power_restart_btn.grid(row=0,column=1,**pad_option)

        self.power_reset_btn = ttk.Button(power_frm,text=_("Reset"))
        self.power_reset_btn.grid(row=0,column=2,**pad_option)
    

    def _setup_dns_widget(self):
        pad_option = {"padx":5,"pady":5,"ipadx":5,"ipady":5}
        entry_setting = {"font":('helvetica', 10, 'bold'),"justify":"center"}

        dns_frm = ttk.Labelframe(self.content_frm,text=_("DNS"),labelanchor=tk.NW)
        dns_frm.grid(row=0,column=1,sticky=tk.NSEW,padx=10)
        dns_frm.columnconfigure(1,weight=1)

        self.dns_ip_v = tk.StringVar()
        ttk.Label(dns_frm,text=_("IP"),style="n.TLabel",anchor=tk.CENTER).grid(row=0,column=0,sticky=tk.NSEW)
        ttk.Entry(dns_frm,textvariable=self.dns_ip_v,**entry_setting).grid(row=0,column=1,sticky=tk.NSEW)

        self.dns_primary_v = tk.StringVar()
        ttk.Label(dns_frm,text=_("Primary"),style="n.TLabel",anchor=tk.CENTER).grid(row=1,column=0,sticky=tk.NSEW)
        ttk.Entry(dns_frm,textvariable=self.dns_primary_v,**entry_setting).grid(row=1,column=1,sticky=tk.NSEW)

        self.dns_secondary_v = tk.StringVar()
        ttk.Label(dns_frm,text=_("Secondary"),style="n.TLabel",anchor=tk.CENTER).grid(row=2,column=0,sticky=tk.NSEW)
        ttk.Entry(dns_frm,textvariable=self.dns_secondary_v,**entry_setting).grid(row=2,column=1,sticky=tk.NSEW)

        self.dns_apply_btn = ttk.Button(dns_frm,text=_("Apply"))
        self.dns_apply_btn.grid(row=3,column=0,**pad_option)

        self.dns_reset_btn = ttk.Button(dns_frm,text=_("Reset"))
        self.dns_reset_btn.grid(row=3,column=1,**pad_option)