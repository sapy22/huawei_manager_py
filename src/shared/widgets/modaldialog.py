import tkinter as tk
import tkinter.ttk as ttk




class Message(tk.Toplevel):
    def __init__(self,master=None,title="",msg=""):
        super().__init__(master,background="white")
        self.msg = msg

        
        self.title(title)
        self.resizable(0,0)
        self.minsize(320,100)
        self.columnconfigure(0,weight=1)

        m_frm = ttk.Frame(self)
        m_frm.grid(pady=20)
        ttk.Label(m_frm,text=self.msg).grid()

        b_frm = ttk.Frame(self)
        b_frm.grid(pady=0)
        ttk.Button(b_frm,text="Ok",command=self.destroy).grid()