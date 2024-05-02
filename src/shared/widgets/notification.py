import tkinter as tk
import tkinter.ttk as ttk

from src.shared.utils import center_window_on_master




class Notification(tk.Toplevel):
    """ delay in ms """
    def __init__(self ,master=None, text="",delay=0, **kwargs):
        super().__init__(master, **kwargs)
        self.text = text

        self.setup_window()

        center_window_on_master(self)

        self.after(delay,self.animate)
        

    def setup_window(self):
        self.attributes("-topmost", True, "-alpha", 0)
        self.overrideredirect(1)

        label = ttk.Label(self,style="notification.TLabel",text=self.text)
        label.grid()

    
    def animate(self):
        start_alpha = 1.0
        self.alpha = start_alpha
        end_alpha = 0.0
        steps = 20
        self.alpha_step = (start_alpha - end_alpha) / steps

        self.x = self.winfo_rootx()
        self.y = self.winfo_rooty()

        self._animate()


    def _animate(self):
        self.alpha -= self.alpha_step
        
        self.attributes("-alpha", self.alpha)
        
        self.y -= 5
        self.geometry(f"+{self.x}+{self.y}")
        
        if self.alpha <= 0.0:
            self.destroy()
        else:
            self.after(100,self._animate)