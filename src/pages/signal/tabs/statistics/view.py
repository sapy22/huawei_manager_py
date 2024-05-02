import tkinter as tk
import tkinter.ttk as ttk

from src.shared.widgets import GraphFrame




class StatisticsView(ttk.Frame):
    def __init__(self, master, settings_data):
        super().__init__(master)
        self.settings_data = settings_data

        self.setup_frames()
        self.setup_widgets()
    

    def setup_frames(self):
        self.top_frm = ttk.Frame(self)
        self.top_frm.grid(row=0,column=0)

        
    def setup_widgets(self):
        self._setup_traffic_widget()
        self._setup_graph_widget()


    def _setup_traffic_widget(self):
        current_frm = ttk.Frame(self.top_frm)
        current_frm.grid(row=0,column=0,pady=10)

        ttk.Label(current_frm,text=_("CurrentDownload"),style="n.TLabel",anchor=tk.CENTER,justify=tk.CENTER,width=25).grid(row=0,column=0,sticky=tk.NSEW)
        self.current_dl_v = tk.StringVar(value="CurrentDownload")
        ttk.Label(current_frm,textvariable=self.current_dl_v,style="v.TLabel",anchor=tk.CENTER).grid(row=1,column=0,sticky=tk.NSEW)

        ttk.Label(current_frm,text=_("CurrentUpload"),style="n.TLabel",anchor=tk.CENTER,justify=tk.CENTER,width=25).grid(row=0,column=1,sticky=tk.NSEW)
        self.current_ul_v = tk.StringVar(value="CurrentUpload")
        ttk.Label(current_frm,textvariable=self.current_ul_v,style="v.TLabel",anchor=tk.CENTER).grid(row=1,column=1,sticky=tk.NSEW)

        ttk.Label(current_frm,text=_("CurrentConnectTime"),style="n.TLabel",anchor=tk.CENTER,justify=tk.CENTER,width=25).grid(row=0,column=2,sticky=tk.NSEW)
        self.current_conn_time_v = tk.StringVar(value="CurrentConnectTime")
        ttk.Label(current_frm,textvariable=self.current_conn_time_v,style="v.TLabel",anchor=tk.CENTER).grid(row=1,column=2,sticky=tk.NSEW)
        

        total_frm = ttk.Frame(self.top_frm)
        total_frm.grid(row=1,column=0,pady=10)

        ttk.Label(total_frm,text=_("TotalDownload"),style="n.TLabel",anchor=tk.CENTER,justify=tk.CENTER,width=25).grid(row=0,column=0,sticky=tk.NSEW)
        self.total_dl_v = tk.StringVar(value="TotalDownload")
        ttk.Label(total_frm,textvariable=self.total_dl_v,style="v.TLabel",anchor=tk.CENTER).grid(row=1,column=0,sticky=tk.NSEW)

        ttk.Label(total_frm,text=_("TotalUpload"),style="n.TLabel",anchor=tk.CENTER,justify=tk.CENTER,width=25).grid(row=0,column=1,sticky=tk.NSEW)
        self.total_ul_v = tk.StringVar(value="TotalUpload")
        ttk.Label(total_frm,textvariable=self.total_ul_v,style="v.TLabel",anchor=tk.CENTER).grid(row=1,column=1,sticky=tk.NSEW)

        ttk.Label(total_frm,text=_("TotalConnectTime"),style="n.TLabel",anchor=tk.CENTER,justify=tk.CENTER,width=25).grid(row=0,column=2,sticky=tk.NSEW)
        self.total_conn_time_v = tk.StringVar(value="TotalConnectTime")
        ttk.Label(total_frm,textvariable=self.total_conn_time_v,style="v.TLabel",anchor=tk.CENTER).grid(row=1,column=2,sticky=tk.NSEW)


        c_rate_frm = ttk.Frame(self.top_frm)
        c_rate_frm.grid(row=2,column=0,pady=10)

        ttk.Label(c_rate_frm,text=_("CurrentDownloadRate"),style="n.TLabel",anchor=tk.CENTER,justify=tk.CENTER,width=25).grid(row=0,column=0,sticky=tk.NSEW,padx=20)
        self.current_dl_rate_v = tk.StringVar(value="CurrentDownloadRate")
        ttk.Label(c_rate_frm,textvariable=self.current_dl_rate_v,style="v.TLabel",anchor=tk.CENTER).grid(row=1,column=0,sticky=tk.NSEW,padx=20)

        ttk.Label(c_rate_frm,text=_("CurrentUploadRate"),style="n.TLabel",anchor=tk.CENTER,justify=tk.CENTER,width=25).grid(row=0,column=1,sticky=tk.NSEW,padx=20)
        self.current_ul_rate_v = tk.StringVar(value="CurrentUploadRate")
        ttk.Label(c_rate_frm,textvariable=self.current_ul_rate_v,style="v.TLabel",anchor=tk.CENTER).grid(row=1,column=1,sticky=tk.NSEW,padx=20)


    def _setup_graph_widget(self):
        dl_ul_graph = self.settings_data.get("ui").get("dl_ul_graph")

        if not dl_ul_graph:
            return

        graph_frm = ttk.Frame(self.top_frm)
        graph_frm.grid(row=3,column=0,sticky=tk.NSEW,pady=20)
        graph_frm.columnconfigure(0,weight=1)
        graph_frm.columnconfigure(1,weight=1)
        
        self.dl_graph = GraphFrame(graph_frm,_("Download Mb"),lines_color=("green",))
        self.dl_graph.grid(row=0,column=0,sticky=tk.NSEW)
        self.dl_graph.columnconfigure(0,weight=1)
        self.dl_graph.rowconfigure(0,weight=1)

        self.ul_graph = GraphFrame(graph_frm,_("Upload Mb"),lines_color=("red",))
        self.ul_graph.grid(row=0,column=1,sticky=tk.NSEW)
        self.ul_graph.columnconfigure(0,weight=1)
        self.ul_graph.rowconfigure(0,weight=1)