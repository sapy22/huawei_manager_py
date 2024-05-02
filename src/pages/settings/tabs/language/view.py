import tkinter as tk
import tkinter.ttk as ttk




class LanguageView(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=10)
        self.setup_widgets()
    

    def setup_widgets(self):
        self._setup_lang_widget()
        self._setup_direction_widget()
        

    def _setup_lang_widget(self):
        pad_option = {"padx":5,"pady":5,"ipadx":5,"ipady":5}
        
        lang_lbl_frm = ttk.Labelframe(self,padding=5,text=_("Language"),labelanchor=tk.NW)
        lang_lbl_frm.grid(row=0,column=0,sticky=tk.NSEW)
        lang_lbl_frm.columnconfigure(0,weight=1)

        continer_frm = ttk.Frame(lang_lbl_frm)
        continer_frm.grid(row=0,column=0,sticky=tk.W)

        self.lang_v = tk.StringVar(value="en")
        self.en_rd_btn = ttk.Radiobutton(continer_frm,text=_("English"),variable=self.lang_v,value="en")
        self.en_rd_btn.grid(row=0,column=0,**pad_option)
        self.ar_rd_btn = ttk.Radiobutton(continer_frm,text=_("Arabic"),variable=self.lang_v,value="ar_SA")
        self.ar_rd_btn.grid(row=0,column=1,**pad_option)
    

    def _setup_direction_widget(self):
        pad_option = {"padx":5,"pady":5,"ipadx":5,"ipady":5}
        
        direction_lbl_frm = ttk.Labelframe(self,padding=5,text=_("Layout Direction"),labelanchor=tk.NW)
        direction_lbl_frm.grid(row=1,column=0,sticky=tk.NSEW)
        direction_lbl_frm.columnconfigure(0,weight=1)

        continer_frm = ttk.Frame(direction_lbl_frm)
        continer_frm.grid(row=0,column=0,sticky=tk.W)

        self.dir_v = tk.StringVar(value="ltr")
        self.ltr_rd_btn = ttk.Radiobutton(continer_frm,text=_("Left to Right"),variable=self.dir_v,value="ltr")
        self.ltr_rd_btn.grid(row=0,column=0,**pad_option)
        self.rtl_rd_btn = ttk.Radiobutton(continer_frm,text=_("Right to Left"),variable=self.dir_v,value="rtl")
        self.rtl_rd_btn.grid(row=0,column=1,**pad_option)