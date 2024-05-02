import tkinter as tk
import tkinter.ttk as ttk




class BandSelectView(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.setup_frames()
        self.setup_widgets()

    
    def setup_frames(self):
        self.selected_band_frm = ttk.Frame(self)
        self.selected_band_frm.grid(row=0,column=0,pady=30)

        self.band_select_frm = ttk.Labelframe(self,padding=10,labelanchor=tk.NW)
        self.band_select_frm.grid(row=1,column=0)


    def setup_widgets(self):
        self._setup_selected_band_widget()
        self._setup_band_select_widget()


    def _setup_selected_band_widget(self):
        ttk.Label(self.selected_band_frm,text=_("Network Mode"),style="n.TLabel",anchor=tk.CENTER,justify=tk.CENTER,width=30).grid(row=0,column=0,sticky=tk.NSEW)
        self.network_mode_lbl_v = tk.StringVar(value="Network Mode")
        ttk.Label(self.selected_band_frm,textvariable=self.network_mode_lbl_v,style="v.TLabel",anchor=tk.CENTER).grid(row=1,column=0,sticky=tk.NSEW)

        ttk.Label(self.selected_band_frm,text=_("Network Band"),style="n.TLabel",anchor=tk.CENTER,justify=tk.CENTER,width=30).grid(row=0,column=1,sticky=tk.NSEW)
        self.network_band_lbl_v = tk.StringVar(value="Network Band")
        ttk.Label(self.selected_band_frm,textvariable=self.network_band_lbl_v,style="v.TLabel",anchor=tk.CENTER).grid(row=1,column=1,sticky=tk.NSEW)

        ttk.Label(self.selected_band_frm,text=_("LTE band"),style="n.TLabel",anchor=tk.CENTER,justify=tk.CENTER,width=30).grid(row=0,column=2,sticky=tk.NSEW)
        self.lte_band_lbl_v = tk.StringVar(value="LTE band")
        ttk.Label(self.selected_band_frm,textvariable=self.lte_band_lbl_v,style="v.TLabel",anchor=tk.CENTER).grid(row=1,column=2,sticky=tk.NSEW)


    def _setup_band_select_widget(self):
        self._setup_network_mode_widget()
        self._setup_network_band_widget()
        self._setup_lte_band_widget()
        self._setup_band_hint_widget()
        self._setup_apply_widget()


    def _setup_network_mode_widget(self):
        pad_option = {"padx":5,"pady":5,"ipadx":5,"ipady":5}

        nm_frm = ttk.Labelframe(self.band_select_frm,padding=5,text=_("Network Mode"),labelanchor=tk.NW)
        nm_frm.grid(row=0,column=0,sticky=tk.NSEW)
        nm_frm.columnconfigure(0,weight=1)

        continer_frm = ttk.Frame(nm_frm)
        continer_frm.grid(row=0,column=0,sticky=tk.W)

        self.network_mode_v = tk.StringVar(value="00")
        ttk.Radiobutton(continer_frm,text=_("Auto"),variable=self.network_mode_v,value="00").grid(row=0,column=0,**pad_option)
        ttk.Radiobutton(continer_frm,text=_("4G only"),variable=self.network_mode_v,value="03").grid(row=0,column=1,**pad_option)
        ttk.Radiobutton(continer_frm,text=_("NR"),variable=self.network_mode_v,value="08").grid(row=0,column=2,**pad_option)


    def _setup_network_band_widget(self):
        pad_option = {"padx":5,"pady":5,"ipadx":5,"ipady":5}

        nb_frm = ttk.Labelframe(self.band_select_frm,padding=5,text=_("Network Band"),labelanchor=tk.NW)
        nb_frm.grid(row=1,column=0,sticky=tk.NSEW)
        nb_frm.columnconfigure(0,weight=1)

        continer_frm = ttk.Frame(nb_frm)
        continer_frm.grid(row=0,column=0,sticky=tk.W)

        self.network_band_v = tk.StringVar(value="3FFFFFFF")
        ttk.Radiobutton(continer_frm,text=_("Auto"),variable=self.network_band_v,value="3FFFFFFF").grid(row=0,column=0,**pad_option)

    
    def _setup_lte_band_widget(self):
        pad_option = {"padx":5,"pady":5,"ipadx":5,"ipady":5}

        lb_frm = ttk.Labelframe(self.band_select_frm,padding=5,text=_("LTE Band"),labelanchor=tk.NW)
        lb_frm.grid(row=2,column=0)
        lb_frm.columnconfigure(0,weight=1)

        #
        continer_frm = ttk.Frame(lb_frm)
        continer_frm.grid(row=0,column=0,sticky=tk.W)

        self.lte_band_v = tk.StringVar(value="auto")
        ttk.Radiobutton(continer_frm,text=_("Auto"),variable=self.lte_band_v,value="auto",command=lambda:self.on_lte_band_rd_btn_pressed("auto")).grid(row=0,column=0,**pad_option)
        ttk.Radiobutton(continer_frm,text=_("Manual"),variable=self.lte_band_v,value="manual",command=lambda:self.on_lte_band_rd_btn_pressed("manual")).grid(row=0,column=1,**pad_option)

        #
        self.lte_band_frm = ttk.Frame(lb_frm,padding=5)
        self.lte_band_frm.grid(row=1,column=0)

        self.b1_v = tk.BooleanVar(value=False)
        self.b1_chk_btn = ttk.Checkbutton(self.lte_band_frm,text="B1-2100",variable=self.b1_v,state="disabled")
        self.b1_chk_btn.grid(row=1,column=0,**pad_option)

        self.b3_v = tk.BooleanVar(value=False)
        self.b3_chk_btn = ttk.Checkbutton(self.lte_band_frm,text="B3-1800",variable=self.b3_v,state="disabled")
        self.b3_chk_btn.grid(row=1,column=1,**pad_option)

        self.b5_v = tk.BooleanVar(value=False)
        self.b5_chk_btn = ttk.Checkbutton(self.lte_band_frm,text="B5-850",variable=self.b5_v,state="disabled")
        self.b5_chk_btn.grid(row=1,column=2,**pad_option)
        
        self.b8_v = tk.BooleanVar(value=False)
        self.b8_chk_btn = ttk.Checkbutton(self.lte_band_frm,text="B8-900",variable=self.b8_v,state="disabled")
        self.b8_chk_btn.grid(row=1,column=3,**pad_option)

        self.b20_v = tk.BooleanVar(value=False)
        self.b20_chk_btn = ttk.Checkbutton(self.lte_band_frm,text="B20-800",variable=self.b20_v,state="disabled")
        self.b20_chk_btn.grid(row=1,column=4,**pad_option)

        self.b28_v = tk.BooleanVar(value=False)
        self.b28_chk_btn = ttk.Checkbutton(self.lte_band_frm,text="B28-700",variable=self.b28_v,state="disabled")
        self.b28_chk_btn.grid(row=1,column=5,**pad_option)

        self.b32_v = tk.BooleanVar(value=False)
        self.b32_chk_btn = ttk.Checkbutton(self.lte_band_frm,text="B32-1500",variable=self.b32_v,state="disabled")
        self.b32_chk_btn.grid(row=1,column=6,**pad_option)


        self.b34_v = tk.BooleanVar(value=False)
        self.b34_chk_btn = ttk.Checkbutton(self.lte_band_frm,text="B34-2000",variable=self.b34_v,state="disabled")
        self.b34_chk_btn.grid(row=2,column=0,**pad_option)

        self.b38_v = tk.BooleanVar(value=False)
        self.b38_chk_btn = ttk.Checkbutton(self.lte_band_frm,text="B38-2600",variable=self.b38_v,state="disabled")
        self.b38_chk_btn.grid(row=2,column=1,**pad_option)

        self.b39_v = tk.BooleanVar(value=False)
        self.b39_chk_btn = ttk.Checkbutton(self.lte_band_frm,text="B39-1900",variable=self.b39_v,state="disabled")
        self.b39_chk_btn.grid(row=2,column=2,**pad_option)

        self.b40_v = tk.BooleanVar(value=False)
        self.b40_chk_btn = ttk.Checkbutton(self.lte_band_frm,text="B40-2300",variable=self.b40_v,state="disabled")
        self.b40_chk_btn.grid(row=2,column=3,**pad_option)

        self.b41_v = tk.BooleanVar(value=False)
        self.b41_chk_btn = ttk.Checkbutton(self.lte_band_frm,text="B41-2500",variable=self.b41_v,state="disabled")
        self.b41_chk_btn.grid(row=2,column=4,**pad_option)

        self.b42_v = tk.BooleanVar(value=False)
        self.b42_chk_btn = ttk.Checkbutton(self.lte_band_frm,text="B42-3500",variable=self.b42_v,state="disabled")
        self.b42_chk_btn.grid(row=2,column=5,**pad_option)
        
        self.b43_v = tk.BooleanVar(value=False)
        self.b43_chk_btn = ttk.Checkbutton(self.lte_band_frm,text="B43-3700",variable=self.b43_v,state="disabled")
        self.b43_chk_btn.grid(row=2,column=6,**pad_option)
        

    def _setup_band_hint_widget(self):
        pad_option = {"padx":5,"pady":5,"ipadx":5,"ipady":5}

        bh_frm = ttk.Labelframe(self.band_select_frm,padding=5,text=_("Band Hint"),labelanchor=tk.NW)
        bh_frm.grid(row=3,column=0,sticky=tk.NSEW)
        bh_frm.columnconfigure(0,weight=1)

        continer_frm = ttk.Frame(bh_frm)
        continer_frm.grid(row=0,column=0,sticky=tk.W)

        self.band_hint_v = tk.StringVar(value="none") 
        ttk.Radiobutton(continer_frm,text=_("None"),variable=self.band_hint_v,value="none",command=lambda:self.on_band_hint_rd_btn_pressed("none")).grid(row=0,column=0,**pad_option)
        ttk.Radiobutton(continer_frm,text=_("STC"),variable=self.band_hint_v,value="stc",command=lambda:self.on_band_hint_rd_btn_pressed("stc")).grid(row=0,column=1,**pad_option)
        ttk.Radiobutton(continer_frm,text=_("Mobily"),variable=self.band_hint_v,value="mobily",command=lambda:self.on_band_hint_rd_btn_pressed("mobily")).grid(row=0,column=2,**pad_option)
        ttk.Radiobutton(continer_frm,text=_("Zain"),variable=self.band_hint_v,value="zain",command=lambda:self.on_band_hint_rd_btn_pressed("zain")).grid(row=0,column=3,**pad_option)


    def _setup_apply_widget(self):
        pad_option = {"padx":5,"pady":5,"ipadx":5,"ipady":5}

        apply_frm = ttk.Frame(self.band_select_frm,padding=10)
        apply_frm.grid(row=4,column=0)
       
        self.apply_btn = ttk.Button(apply_frm,text=_("Apply"))
        self.apply_btn.grid(row=0,column=0,**pad_option)

        self.clear_btn = ttk.Button(apply_frm,text=_("Clear"))
        self.clear_btn.grid(row=0,column=1,**pad_option)