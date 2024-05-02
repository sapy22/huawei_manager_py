import tkinter.ttk as ttk

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk




class CustomNavigationToolbar(NavigationToolbar2Tk):
    """ A custom subclass of NavigationToolbar2Tk that suppresses the display of coordinates on the toolbar."""
    def set_message(self, s):
        pass


class GraphFrame(ttk.Frame):
    def __init__(self, master, title="", lines_qty=1, lines_lbl: tuple[str, ...] | None=None, lines_color: tuple[str, ...] | None=None, **kwargs):
        super().__init__(master, class_="GraphFrame", **kwargs)
        self.title = title
        self.lines_qty = lines_qty
        self.lines_lbl = lines_lbl
        self.lines_color = lines_color

        self.setup_figure()
        self.setup_lines()


    def setup_figure(self):
        self.fig = Figure(figsize=(1,2),layout="constrained")
        self.ax = self.fig.add_subplot()
        self.ax.set_title(self.title)
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().grid(row=0,column=0,sticky="nsew")

        toolbar = CustomNavigationToolbar(self.canvas, self, pack_toolbar=False)
        toolbar.grid(row=1,column=0)
        

    def setup_lines(self):
        x = []
        y = []
        self.plt_lines = []
        
        for i in range(self.lines_qty):
            self.plt_lines.append(self.ax.plot(x, y)[0])
            if self.lines_color:
                self.plt_lines[i].set_color(self.lines_color[i])

        if self.lines_lbl:
            self.ax.legend(self.plt_lines, self.lines_lbl)



    def update_graph(self, x: list, y: tuple[list, ...]):
        for i, line in enumerate(self.plt_lines):
            line.set_data(x, y[i])
        
        self.ax.relim()
        self.ax.autoscale_view()
        self.canvas.draw()