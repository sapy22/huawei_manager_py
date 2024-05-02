import tkinter as tk
import tkinter.ttk as ttk




class ToolTip():
    def __init__(self, master, **kwargs):
        self.master = master

        self.window = tk.Toplevel(self.master)
        self.window.attributes('-topmost', True)
        self.window.overrideredirect(1)

        self.label = ttk.Label(self.window, style="tooltip.TLabel")
        self.label.grid()

        self.window.withdraw()
    

    def bind(self, widget, text:str):
        widget.bind('<Enter>', lambda e: self.show(text, e))
        widget.bind('<Leave>', lambda e: self.hide(e))
        

    def show(self,text, event):
        self.label.configure(text=text)

        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenwidth()

        w = self.label.winfo_reqwidth()
        h = self.label.winfo_reqheight()
    
        x = event.x_root
        y = event.widget.winfo_rooty() + (event.widget.winfo_height() + 5)
        
        if x + w > sw:
            x = x - w
        
        self.window.geometry(f'+{x}+{y}')
        self.window.deiconify()
        
        
    def hide(self,event):
        self.window.withdraw()
        