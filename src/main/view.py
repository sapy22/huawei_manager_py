import tkinter as tk
import tkinter.ttk as ttk

from src.shared.utils import center_window_on_screen, center_window_on_master
from src.shared.constant import ResolutionDict, StyleDict, RTLStyle
from src.shared.settings import resources_dir




class MainView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.setup_view()
        self.setup_style()

        self.setup_frames()

        center_window_on_screen(self)

    
    def setup_view(self):
        self.title("HManagerPy")
        self.app_icon = tk.PhotoImage(file = resources_dir / "icons/app_24.png")
        self.wm_iconphoto(True, self.app_icon)
        self.minsize(*ResolutionDict.get("HD"))
        self.columnconfigure(0,weight=1)
        self.rowconfigure(1,weight=1)


    def setup_frames(self):
        self.nav_frame = ttk.Frame(self)
        self.nav_frame.grid(row=0,column=0,sticky=tk.NSEW)
        self.nav_frame.columnconfigure(0,weight=1)
        
        self.content_frame = ttk.Frame(self)
        self.content_frame.grid(row=1,column=0,sticky=tk.NSEW)
        self.content_frame.columnconfigure(0,weight=1)
        self.content_frame.rowconfigure(0,weight=1)


    def setup_toplevel_window(self, title: str, geometry: str):
        window = tk.Toplevel(self)
        window.title(title)
        window.geometry(geometry)
        window.resizable(0,0)
        window.rowconfigure(0,weight=1)
        window.columnconfigure(0,weight=1)
        center_window_on_master(window)
        return window

    
    def setup_style(self):
        style = ttk.Style() # justify, anchor, sticky not working
        style.theme_use("clam") #  clam, alt, default, classic
        style.configure(".",background="white")
        
        # style.configure("g.TEntry",foreground="green", fieldbackground="lightyellow", bordercolor="red")
        # print(style.lookup("g.TEntry","fieldbackground"))
        # print(style.layout("TLabelframe.Label"))
        # print(style.element_options("Label.text"))
        
        style.configure("nav.TFrame",background="#a7a299")
        style.configure("nav.TButton",background="#a7a299",relief=tk.FLAT)

        style.configure("n.TLabel",background="#e9e9e7",font="helvetica 12 bold",padding=5,relief=tk.RIDGE)
        style.configure("v.TLabel",font="helvetica 10 bold",padding=5,relief=tk.SUNKEN)
        style.configure("notification.TLabel",font="helvetica 10 bold",padding=2,relief=tk.RIDGE)
        style.configure("tooltip.TLabel",font="helvetica 10 bold",padding=2,relief=tk.RIDGE)
        style.configure("date.TLabel",font=("helvetica 10"))
        style.configure("content.TLabel",font=("helvetica 12"),background="#e9e9e7")

        style.configure("TRadiobutton",font="helvetica 10")

        style.configure("TCheckbutton",font="helvetica 10")
        style.configure("hint.TCheckbutton",foreground="red",font="helvetica 10 bold")

        self._setup_rtl_style(style)


    def _setup_rtl_style(self,s):
        s.configure(RTLStyle.RTLNotebook.value, tabposition=tk.NE)

        s.layout(RTLStyle.RTLRadiobutton.value,
            [("Radiobutton.padding",{"sticky": "nswe","children":
                [("Radiobutton.indicator", {"side": "right", "sticky": ""}),("Radiobutton.focus", {"side": "left","sticky": "","children":
                    [("Radiobutton.label", {"sticky": "nswe"})]})]})])

        s.layout(RTLStyle.RTLCheckbutton.value,
            [("Checkbutton.padding",{"sticky": "nswe","children":
                    [("Checkbutton.indicator", {"side": "right", "sticky": ""}),("Checkbutton.focus", {"side": "left", "sticky": "w", "children": 
                        [("Checkbutton.label", {"sticky": "nswe"})]})]})])

        s.configure(RTLStyle.HintRTLCheckbutton.value,foreground="red",font="helvetica 10 bold")