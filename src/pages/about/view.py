import tkinter as tk
import tkinter.ttk as ttk




class AboutView(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.setup_widgets()

    
    def setup_widgets(self):
        about_window_frm = ttk.Frame(self)
        about_window_frm.grid(sticky=tk.NSEW,pady=10)
        about_window_frm.columnconfigure(0,weight=1)

        txt = "Tkinter\nhuawei-lte-api\n______\nver 2.0\nhttps://github.com/sapy22/huawei_manager_py"

        ttk.Label(about_window_frm,text=txt,anchor=tk.CENTER,justify=tk.CENTER,font="helvetica 12").grid(row=0,column=0)

        # ttk.Button(about_window_frm, text="Exit",command=self.master.destroy).grid(row=1,column=0,pady=10)