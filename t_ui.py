import builtins
import tkinter as tk
import tkinter.ttk as ttk

from src.pages import SignalController, BandSelectController, SMSController, AdvanceController, SettingsController, AboutController




class App(tk.Tk): 
    def __init__(self):
        super().__init__()
        self.title("TestUi")
        self.minsize(1280,720)
        self.setup_vars()
        self.setup_frames()
        self.setup_widgets()


    def setup_vars(self):
        self.active_page = None

        password = ""
        
        self.data = {
        "connection": {
        "ip": "192.168.8.1",
        "user": "admin",
        "password": f"{password}",
        "keep_conn": False
        },
        "language": {
        "language": "en",
        "direction": "ltr"
        },
        "ui": {
        "nr_5g": True,
        "rsrq_graph": True,
        "rsrp_graph": True,
        "sinr_graph": True,
        "dl_ul_graph":True
        }
        }


    def setup_frames(self):
        self.btns_frm = ttk.Frame(self)
        self.btns_frm.grid()

        self.content_frm = ttk.Frame(self)
        self.content_frm.grid()


    def setup_widgets(self):
        ttk.Button(self.btns_frm,text="signal",command=lambda:self.on_btn_pressed("signal")).grid(row=0,column=0)
        ttk.Button(self.btns_frm,text="band",command=lambda:self.on_btn_pressed("band")).grid(row=0,column=1)
        ttk.Button(self.btns_frm,text="sms",command=lambda:self.on_btn_pressed("sms")).grid(row=0,column=2)
        ttk.Button(self.btns_frm,text="advance",command=lambda:self.on_btn_pressed("advance")).grid(row=0,column=3)
        ttk.Button(self.btns_frm,text="settings",command=lambda:self.on_btn_pressed("settings")).grid(row=0,column=4)
        ttk.Button(self.btns_frm,text="about",command=lambda:self.on_btn_pressed("about")).grid(row=0,column=5)


    def on_btn_pressed(self, btn_name):
        if self.active_page:
            self.active_page.destroy()


        match btn_name:
            case "signal":
                page = SignalController(self.content_frm, self.data)
            case "band":
                page = BandSelectController(self.content_frm, self.data)
            case "sms":
                page = SMSController(self.content_frm, self.data)
            case "advance":
                page = AdvanceController(self.content_frm, self.data)
            case "settings":
                page = SettingsController(self.content_frm, self.data)
            case "about":
                page = AboutController(self.content_frm)

        self.active_page = page
        self.active_page.grid()



def main():
    builtins._ = lambda v: v

    app = App()
    app.columnconfigure(0,weight=1)
    app.mainloop()




if __name__ == "__main__":
    main()