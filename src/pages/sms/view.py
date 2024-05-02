import tkinter as tk
import tkinter.ttk as ttk

from src.shared.localize import lc_is_rtl_layout
from src.shared.widgets import ScrollableFrame
from src.shared.utils import center_window_on_master




class SMSView(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.setup_frames()
        self.setup_widgets()

    
    def setup_frames(self):
        self.all_sms_frm = ttk.Frame(self)
        self.all_sms_frm.grid(row=0,column=0,pady=30)
        self.all_sms_frm.columnconfigure(0,weight=1)

        self.new_sms_frm = ttk.Labelframe(self,text=_("New SMS"),padding=10,labelanchor=tk.NW)
        self.new_sms_frm.grid(row=1,column=0)


    def setup_widgets(self):
        self._setup_all_sms_widget()
        self._setup_new_sms_widget()


    def _setup_all_sms_widget(self):
        pad_option = {"padx":5,"pady":5,"ipadx":5,"ipady":5}

        continer_frm = ttk.Frame(self.all_sms_frm)
        continer_frm.grid(row=0,column=0,sticky=tk.W)

        self.box_type_v = tk.StringVar(value="inbox")
        self.inbox_rd_btn = ttk.Radiobutton(continer_frm,text=_("Inbox"),variable=self.box_type_v,value="inbox")
        self.inbox_rd_btn.grid(row=0,column=0,**pad_option)
        self.outbox_rd_btn = ttk.Radiobutton(continer_frm,text=_("Outbox"),variable=self.box_type_v,value="outbox")
        self.outbox_rd_btn.grid(row=0,column=1,**pad_option)


        v = ("contacts", "content", "date")
        if lc_is_rtl_layout():
            v = tuple(reversed(v))

        self.tree = ttk.Treeview(self.all_sms_frm, columns=v, selectmode="browse", show="headings",height=10)
        self.tree.grid(row=1,column=0)

        self.tree_scrollbar = ttk.Scrollbar(self.all_sms_frm,orient="vertical", command=self.tree.yview)
        self.tree_scrollbar.grid(row=1,column=1,sticky=tk.NSEW)
        self.tree.configure(yscrollcommand=self.tree_scrollbar.set)
        
        self.tree.heading("contacts", text=_("Contacts"), anchor=tk.CENTER)
        self.tree.heading("content", text=_("Content"), anchor=tk.CENTER)
        self.tree.heading("date", text=_("Date"), anchor=tk.CENTER)

        self.tree.column("contacts", minwidth=100, anchor=tk.CENTER)
        self.tree.column("content", minwidth=400, anchor=tk.CENTER)
        self.tree.column("date", minwidth=100, anchor=tk.CENTER)
    

    def _setup_new_sms_widget(self):
        pad_option = {"padx":5,"pady":5,"ipadx":5,"ipady":5}
        entry_setting = {"font":('helvetica', 10, 'bold'),"justify":"center"}

        num_frm = ttk.Frame(self.new_sms_frm)
        num_frm.grid(row=0,column=0,sticky=tk.NSEW)
        num_frm.columnconfigure(1,weight=1)

        self.number_v = tk.StringVar()
        ttk.Label(num_frm,text=_("use ; to separate more than one number")).grid(row=0,column=1)
        ttk.Label(num_frm,text=_("Number\\s"),style="n.TLabel").grid(row=1,column=0)
        ttk.Entry(num_frm,textvariable=self.number_v,**entry_setting).grid(row=1,column=1,**pad_option,sticky=tk.NSEW)

        self.msg_text = tk.Text(self.new_sms_frm,width=50,height=5,padx=10,pady=10,relief=tk.SOLID)
        self.msg_text.grid(row=1,column=0,**pad_option)

        self.msg_lenght_lbl = ttk.Label(self.new_sms_frm,text="160")
        self.msg_lenght_lbl.grid(row=2,column=0)

        self.send_btn = ttk.Button(self.new_sms_frm,text=_("Send"))
        self.send_btn.grid(row=3,column=0,**pad_option)


    def setup_content_window(self, msg_list, phone):
        pad_option = {"padx":5,"pady":5,"ipadx":5,"ipady":5}

        window = tk.Toplevel(self)
        window.overrideredirect(True)
        window.resizable(0,0)
        window.columnconfigure(0,weight=1)

        frm = ttk.Labelframe(window)
        frm.grid()

        ttk.Label(frm,text=phone,style="date.TLabel",wraplength=400,anchor="center").grid(**pad_option)

        sc_frm = ScrollableFrame(frm)
        sc_frm.grid(padx=15,sticky=tk.NSEW)
        sc_frm.columnconfigure(0,weight=1)
        if lc_is_rtl_layout():
            sc_frm.change_to_rtl_layout()

        for msg in msg_list:
            content = msg[0]
            date = str(msg[1])
            ttk.Label(sc_frm.inner_frame,text=date,style="date.TLabel",anchor="center").grid(**pad_option)
            ttk.Label(sc_frm.inner_frame,text=content,style="content.TLabel",width=80,wraplength=400,justify="center",anchor="center").grid(**pad_option)

        ttk.Button(frm,text=_("Exit"),command=window.destroy).grid(**pad_option)

        center_window_on_master(window)

        window.grab_set()