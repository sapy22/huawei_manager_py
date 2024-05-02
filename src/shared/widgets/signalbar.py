import tkinter as tk




class SignalBar(tk.Canvas):
    def __init__(self, master, width=120, height=30, value=0, max_value=5, bar_fill_color="blue", bar_bg_color="grey", **kwargs):
        super().__init__(master, width=width, height=height, highlightthickness=0, bd=0, **kwargs)
        self.class_name = "SignalBar"
        self.max_value = max(max_value,1)
        self.value = 0
        self.update_value(value)
        self.x_pad = 5
        self.y_pad = 2
        self.bar_pad = 2
        self.bar_fill_color = bar_fill_color
        self.bar_bg_color = bar_bg_color

        self.setup_x_coordinates()
        self.setup_y_coordinates()

        self._draw_bar()


    # init
    def setup_x_coordinates(self):
        self.x_coords = []
        _width = (self.winfo_reqwidth() - (self.x_pad * 2)) - (self.bar_pad * (self.max_value - 1))
        bar_width = _width / self.max_value
        x1 = 0 + self.x_pad
        x2 = x1 + bar_width
        for i in range(self.max_value):
            self.x_coords.append((x1,x2))
            x1 = x2 + self.bar_pad
            x2 = x1 + bar_width
    

    def setup_y_coordinates(self):
        self.y_coords = []
        _height = (self.winfo_reqheight() - (self.y_pad * 2))
        segment_height = _height / self.max_value
        for i in range(self.max_value):
            num_of_segment = (self.max_value-1) - i
            y1 = (segment_height * num_of_segment) + self.y_pad
            y2 = _height + self.y_pad
            self.y_coords.append((y1,y2))

    
    #
    def _draw_bar(self):
        self.delete("all")

        for i in range(self.max_value):
            x1, x2 = self.x_coords[i]
            y1, y2 = self.y_coords[i]

            fill_color = self.bar_fill_color
            if i+1 > self.value:
                fill_color = self.bar_bg_color

            self.create_rectangle(x1, y1, x2, y2, fill=fill_color,width=0) # width = outline width


    def change_to_rtl_layout(self):
        self.x_coords = list(reversed(self.x_coords))

        self._draw_bar()

    
    def update_value(self,v):
        v = int(v)
        if v > self.max_value:
            v = self.max_value
        elif v < 0:
            v = 0
        
        if v == self.value:
            return
        
        self.value = v

        self._draw_bar()