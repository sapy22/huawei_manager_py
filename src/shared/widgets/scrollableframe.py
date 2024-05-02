import tkinter as tk
import tkinter.ttk as ttk




class ScrollableFrame(ttk.Labelframe):
    def __init__(self, master, **kwargs):
        super().__init__(master, class_="ScrollableFrame", **kwargs)
        self.setup_widgets()
        self.setup_event_handler()

    # init
    def setup_widgets(self):
        self.canvas = tk.Canvas(self,highlightthickness=0,background="white")
        self.canvas.grid(row=0,column=0,sticky=tk.NSEW)

        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollbar.grid(row=0,column=1,sticky=tk.NSEW)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.inner_frame = ttk.Frame(self.canvas)
        # self.inner_frame.columnconfigure(0,weight=1)

        self.inner_frm_id = self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")

    
    def setup_event_handler(self):
        self.inner_frame.bind("<Configure>", self.on_frame_configure)
        # self.canvas.bind("<Configure>", self.on_canvas_configure) 

        self.inner_frame.bind('<Enter>', self.on_mouse_enter)
        self.inner_frame.bind('<Leave>', self.on_mouse_leave)

    #
    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"), width=event.width) # canvas width = frm width
        
    
    def on_canvas_configure(self, event):
        self.canvas.itemconfig(self.inner_frm_id, width=event.width) # frm width = canvas width


    def on_mouse_enter(self, event):
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)


    def on_mouse_leave(self, event):
        self.canvas.unbind_all("<MouseWheel>")


    def _on_mousewheel(self, event):
        v = -1 * (event.delta//120)
        self.canvas.yview_scroll(v, "units")
    

    def change_to_rtl_layout(self):
        self.canvas.grid(column=1)
        self.scrollbar.grid(column=0)