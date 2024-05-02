import tkinter as tk
import tkinter.ttk as ttk

from src.shared.widgets import SignalBar, GraphFrame, ToolTip




class MonitorView(ttk.Frame):
    def __init__(self, master, settings_data):
        super().__init__(master)
        self.settings_data = settings_data
        
        self.tooltip = ToolTip(self)

        self.setup_frames()
        self.setup_widgets()
    

    def setup_frames(self):
        top_frm = ttk.Frame(self)
        top_frm.grid(row=0,column=0,sticky=tk.NSEW)
        top_frm.columnconfigure(0,weight=1)
        top_frm.columnconfigure(1,weight=1)

        self.top_start_frm = ttk.Frame(top_frm)
        self.top_start_frm.grid(row=0,column=0,sticky=tk.NSEW)

        col = 2 if self.settings_data.get("ui").get("nr_5g") else 1
        for i in range(col):
            self.top_start_frm.columnconfigure(i,weight=1)
        
        self.top_end_frm = ttk.Frame(top_frm)
        self.top_end_frm.grid(row=0,column=1,sticky=tk.NSEW)
        self.top_end_frm.columnconfigure(0,weight=1)
        

        self.bottom_frm = ttk.Frame(self)
        self.bottom_frm.grid(row=1,column=0,sticky=tk.NSEW)
        self.bottom_frm.columnconfigure(0,weight=1)
        self.bottom_frm.rowconfigure(0,weight=1)


    def setup_widgets(self):
        self._setup_network_widget()
        self._setup_lte_4g_widget()

        if self.settings_data.get("ui").get("nr_5g"):
            self._setup_nr_5g_widget()
        
        self._setup_lte_tower_widget()
        self._setup_conn_endc_widget()
        
        self._setup_graph_widget()
        

    def _setup_network_widget(self):
        network_frm = ttk.Labelframe(self.top_end_frm,text=_("Network"),padding=5)
        network_frm.grid(row=0,column=0,sticky=tk.NSEW)
        network_frm.columnconfigure(0,weight=1)
        network_frm.columnconfigure(1,weight=2)
        
        ttk.Label(network_frm,text=_("FullName"),style="n.TLabel",anchor=tk.CENTER,justify=tk.CENTER).grid(row=0,column=0,sticky=tk.NSEW)
        self.fullname_v = tk.StringVar(value="FullName")
        ttk.Label(network_frm,textvariable=self.fullname_v,style="v.TLabel",anchor=tk.CENTER).grid(row=0,column=1,sticky=tk.NSEW)
    

    def _setup_lte_4g_widget(self):
        lte_4g_frm = ttk.Labelframe(self.top_start_frm,text=_("LTE 4G"),padding=5)
        lte_4g_frm.grid(row=0,column=0,sticky=tk.NSEW)
        lte_4g_frm.columnconfigure(0,weight=1)
        lte_4g_frm.columnconfigure(1,weight=2)
        
        rsrq = ttk.Label(lte_4g_frm,text=_("rsrq"),style="n.TLabel",anchor=tk.CENTER)
        rsrq.grid(row=0,column=0,sticky=tk.NSEW)
        self.rsrq_lbl_v = ttk.Label(lte_4g_frm,text="rsrq",style="v.TLabel",anchor=tk.CENTER,width=15)  # min width for the col
        self.rsrq_lbl_v.grid(row=0,column=1,sticky=tk.NSEW)
        self.tooltip.bind(rsrq,_("signal qualty"))
        self.tooltip.bind(self.rsrq_lbl_v,_("-20 to 0, lower is better"))
        
        rsrp = ttk.Label(lte_4g_frm,text=_("rsrp"),style="n.TLabel",anchor=tk.CENTER)
        rsrp.grid(row=1,column=0,sticky=tk.NSEW)
        self.rsrp_lbl_v = ttk.Label(lte_4g_frm,text="rsrp",style="v.TLabel",anchor=tk.CENTER)
        self.rsrp_lbl_v.grid(row=1,column=1,sticky=tk.NSEW)
        self.tooltip.bind(rsrp,_("signal power"))
        self.tooltip.bind(self.rsrp_lbl_v,_("-90 to -70, lower is better"))

        sinr = ttk.Label(lte_4g_frm,text=_("sinr"),style="n.TLabel",anchor=tk.CENTER)
        sinr.grid(row=2,column=0,sticky=tk.NSEW)
        self.sinr_lbl_v = ttk.Label(lte_4g_frm,text="sinr",style="v.TLabel",anchor=tk.CENTER)
        self.sinr_lbl_v.grid(row=2,column=1,sticky=tk.NSEW)
        self.tooltip.bind(sinr,_("signal to noise ratio"))
        self.tooltip.bind(self.sinr_lbl_v,_("0 to 20, higher is better"))

        ttk.Label(lte_4g_frm,text=_("txpower"),style="n.TLabel",anchor=tk.CENTER).grid(row=3,column=0,sticky=tk.NSEW)
        self.txpower_v = tk.StringVar(value="txpower")
        ttk.Label(lte_4g_frm,textvariable=self.txpower_v,style="v.TLabel",anchor=tk.CENTER).grid(row=3,column=1,sticky=tk.NSEW)

        ttk.Label(lte_4g_frm,text=_("band"),style="n.TLabel",anchor=tk.CENTER).grid(row=4,column=0,sticky=tk.NSEW)
        self.band_v = tk.StringVar(value="band")
        ttk.Label(lte_4g_frm,textvariable=self.band_v,style="v.TLabel",anchor=tk.CENTER).grid(row=4,column=1,sticky=tk.NSEW)

        ttk.Label(lte_4g_frm,text=_("dlbandwidth"),style="n.TLabel",anchor=tk.CENTER).grid(row=5,column=0,sticky=tk.NSEW)
        self.dlbandwidth_v = tk.StringVar(value="dlbandwidth")
        ttk.Label(lte_4g_frm,textvariable=self.dlbandwidth_v,style="v.TLabel",anchor=tk.CENTER).grid(row=5,column=1,sticky=tk.NSEW)

        ttk.Label(lte_4g_frm,text=_("rssi"),style="n.TLabel",anchor=tk.CENTER).grid(row=6,column=0,sticky=tk.NSEW)
        self.rssi_v = tk.StringVar(value="rssi")
        ttk.Label(lte_4g_frm,textvariable=self.rssi_v,style="v.TLabel",anchor=tk.CENTER).grid(row=6,column=1,sticky=tk.NSEW)
    

    def _setup_nr_5g_widget(self):
        nr_5g_frm = ttk.Labelframe(self.top_start_frm,text=_("NR 5G"),padding=5)
        nr_5g_frm.grid(row=0,column=1,sticky=tk.NSEW)
        nr_5g_frm.columnconfigure(0,weight=1)
        nr_5g_frm.columnconfigure(1,weight=2)
        
        nrrsrq = ttk.Label(nr_5g_frm,text=_("nrrsrq"),style="n.TLabel",anchor=tk.CENTER)
        nrrsrq.grid(row=0,column=0,sticky=tk.NSEW)
        self.nrrsrq_lbl_v = ttk.Label(nr_5g_frm,text="nrrsrq",style="v.TLabel",anchor=tk.CENTER,width=15)  # min width for the col
        self.nrrsrq_lbl_v.grid(row=0,column=1,sticky=tk.NSEW)
        self.tooltip.bind(nrrsrq,_("signal qualty"))
        self.tooltip.bind(self.nrrsrq_lbl_v,_("-20 to 0, lower is better"))

        nrrsrp = ttk.Label(nr_5g_frm,text=_("nrrsrp"),style="n.TLabel",anchor=tk.CENTER)
        nrrsrp.grid(row=1,column=0,sticky=tk.NSEW)
        self.nrrsrp_lbl_v = ttk.Label(nr_5g_frm,text="nrrsrp",style="v.TLabel",anchor=tk.CENTER)
        self.nrrsrp_lbl_v.grid(row=1,column=1,sticky=tk.NSEW)
        self.tooltip.bind(nrrsrp,_("signal power"))
        self.tooltip.bind(self.nrrsrp_lbl_v,_("-90 to -70, lower is better"))

        nrsinr = ttk.Label(nr_5g_frm,text=_("nrsinr"),style="n.TLabel",anchor=tk.CENTER)
        nrsinr.grid(row=2,column=0,sticky=tk.NSEW)
        self.nrsinr_lbl_v = ttk.Label(nr_5g_frm,text="nrsinr",style="v.TLabel",anchor=tk.CENTER)
        self.nrsinr_lbl_v.grid(row=2,column=1,sticky=tk.NSEW)
        self.tooltip.bind(nrsinr,_("signal to noise ratio"))
        self.tooltip.bind(self.nrsinr_lbl_v,_("0 to 20, higher is better"))

        ttk.Label(nr_5g_frm,text=_("nrtxpower"),style="n.TLabel",anchor=tk.CENTER).grid(row=3,column=0,sticky=tk.NSEW)
        self.nrtxpower_v = tk.StringVar(value="nrtxpower")
        ttk.Label(nr_5g_frm,textvariable=self.nrtxpower_v,style="v.TLabel",anchor=tk.CENTER).grid(row=3,column=1,sticky=tk.NSEW)

        ttk.Label(nr_5g_frm,text=_("nrband"),style="n.TLabel",anchor=tk.CENTER).grid(row=4,column=0,sticky=tk.NSEW)
        self.nrband_v = tk.StringVar(value="nrband")
        ttk.Label(nr_5g_frm,textvariable=self.nrband_v,style="v.TLabel",anchor=tk.CENTER).grid(row=4,column=1,sticky=tk.NSEW)

        ttk.Label(nr_5g_frm,text=_("nrdlbandwidth"),style="n.TLabel",anchor=tk.CENTER).grid(row=5,column=0,sticky=tk.NSEW)
        self.nrdlbandwidth_v = tk.StringVar(value="nrdlbandwidth")
        ttk.Label(nr_5g_frm,textvariable=self.nrdlbandwidth_v,style="v.TLabel",anchor=tk.CENTER).grid(row=5,column=1,sticky=tk.NSEW)

        ttk.Label(nr_5g_frm,text=_("mode"),style="n.TLabel",anchor=tk.CENTER).grid(row=6,column=0,sticky=tk.NSEW)
        self.mode_v = tk.StringVar(value="mode")
        ttk.Label(nr_5g_frm,textvariable=self.mode_v,style="v.TLabel",anchor=tk.CENTER).grid(row=6,column=1,sticky=tk.NSEW)
    

    def _setup_lte_tower_widget(self):
        lte_tower_frm = ttk.Labelframe(self.top_end_frm,text=_("LTE Tower"),padding=5)
        lte_tower_frm.grid(row=1,column=0,sticky=tk.NSEW)
        lte_tower_frm.columnconfigure(0,weight=1)
        lte_tower_frm.columnconfigure(1,weight=2)
        lte_tower_frm.columnconfigure(2,weight=1)
        lte_tower_frm.columnconfigure(3,weight=2)
        
        pci_lbl = ttk.Label(lte_tower_frm,text=_("pci"),style="n.TLabel",anchor=tk.CENTER)
        pci_lbl.grid(row=0,column=0,sticky=tk.NSEW)
        self.pci_v = tk.StringVar(value="pci")
        ttk.Label(lte_tower_frm,textvariable=self.pci_v,style="v.TLabel",anchor=tk.CENTER).grid(row=0,column=1,sticky=tk.NSEW)
        self.tooltip.bind(pci_lbl,_("physical cell id"))

        cid_lbl = ttk.Label(lte_tower_frm,text=_("cid"),style="n.TLabel",anchor=tk.CENTER)
        cid_lbl.grid(row=0,column=2,sticky=tk.NSEW)
        self.cid_v = tk.StringVar(value="cid")
        cid_lbl_v = ttk.Label(lte_tower_frm,textvariable=self.cid_v,style="v.TLabel",anchor=tk.CENTER)
        cid_lbl_v.grid(row=0,column=3,sticky=tk.NSEW)
        self.tooltip.bind(cid_lbl,_("sector id"))
        self.tooltip.bind(cid_lbl_v,_("cid=(eci-(256*endB))"))

    def _setup_conn_endc_widget(self):
        conn_endc_frm = ttk.Labelframe(self.top_end_frm,text=_("Connection and Endc"),padding=5)
        conn_endc_frm.grid(row=2,column=0,sticky=tk.NSEW)
        conn_endc_frm.columnconfigure(0,weight=1)
        conn_endc_frm.columnconfigure(1,weight=2)
        conn_endc_frm.columnconfigure(2,weight=1)
        conn_endc_frm.columnconfigure(3,weight=2)
        
        ttk.Label(conn_endc_frm,text=_("connectionstatus"),style="n.TLabel",anchor=tk.CENTER).grid(row=0,column=0,sticky=tk.NSEW)
        self.conn_v = tk.StringVar(value="connectionstatus")
        self.conn_lbl_v = ttk.Label(conn_endc_frm,textvariable=self.conn_v,style="v.TLabel",anchor=tk.CENTER)
        self.conn_lbl_v.grid(row=0,column=1,sticky=tk.NSEW)

        ttk.Label(conn_endc_frm,text=_("endcstatus"),style="n.TLabel",anchor=tk.CENTER).grid(row=0,column=2,sticky=tk.NSEW)
        self.endc_v = tk.StringVar(value="endcstatus")
        self.endc_lbl_v = ttk.Label(conn_endc_frm,textvariable=self.endc_v,style="v.TLabel",anchor=tk.CENTER)
        self.endc_lbl_v.grid(row=0,column=3,sticky=tk.NSEW)
        
        ttk.Label(conn_endc_frm,text=_("SignalIcon"),style="n.TLabel",anchor=tk.CENTER).grid(row=1,column=0,sticky=tk.NSEW)
        self.signal_bar = SignalBar(conn_endc_frm,max_value=5,background="white")
        self.signal_bar.grid(row=1,column=1)
        
        ttk.Label(conn_endc_frm,text=_("SignalIconNr"),style="n.TLabel",anchor=tk.CENTER).grid(row=1,column=2,sticky=tk.NSEW)
        self.nr_signal_bar = SignalBar(conn_endc_frm,max_value=5,background="white")
        self.nr_signal_bar.grid(row=1,column=3)

        ttk.Label(conn_endc_frm,text=_("CurrentNetworkType"),style="n.TLabel",anchor=tk.CENTER).grid(row=2,column=0,sticky=tk.NSEW)
        self.current_network_type_v = tk.StringVar(value="CtNkTp")
        ttk.Label(conn_endc_frm,textvariable=self.current_network_type_v,style="v.TLabel",anchor=tk.CENTER).grid(row=2,column=1,sticky=tk.NSEW)

        ttk.Label(conn_endc_frm,text=_("CurrentNetworkTypeEx"),style="n.TLabel",anchor=tk.CENTER).grid(row=2,column=2,sticky=tk.NSEW)
        self.current_network_type_ex_v = tk.StringVar(value="CtNkTpEx")
        ttk.Label(conn_endc_frm,textvariable=self.current_network_type_ex_v,style="v.TLabel",anchor=tk.CENTER).grid(row=2,column=3,sticky=tk.NSEW)


    def _setup_graph_widget(self):
        data = self.settings_data.get("ui")

        nr_5g = data.get("nr_5g")
        rsrq_graph = data.get("rsrq_graph")
        rsrp_graph = data.get("rsrp_graph")
        sinr_graph = data.get("sinr_graph")

        lines = 2 if nr_5g else 1

        graph = 0
        if rsrq_graph:
            graph += 1
        if rsrp_graph:
            graph += 1
        if sinr_graph:
            graph += 1

        if graph == 0:
            return

        graph_frm = ttk.Frame(self.bottom_frm,padding=5)
        graph_frm.grid(row=0,column=0,sticky=tk.NSEW,pady=20)

        for i in range(graph):
            graph_frm.columnconfigure(i,weight=1)

        col = 0

        if rsrq_graph:
            title = ("RSRQ","RSRQ & NR-RSRQ")
            self.rsrq_graph = GraphFrame(graph_frm, title[lines-1], lines_qty=lines) # line_lbl=("4G","5G")
            self.rsrq_graph.grid(row=0,column=col,sticky=tk.NSEW)
            self.rsrq_graph.columnconfigure(0,weight=1)
            self.rsrq_graph.rowconfigure(0,weight=1)
            col += 1

        if rsrp_graph:
            title = ("RSRP","RSRP & NR-RSRP")
            self.rsrp_graph = GraphFrame(graph_frm, title[lines-1], lines_qty=lines)
            self.rsrp_graph.grid(row=0,column=col,sticky=tk.NSEW)
            self.rsrp_graph.columnconfigure(0,weight=1)
            self.rsrp_graph.rowconfigure(0,weight=1)
            col += 1
        
        if sinr_graph:
            title = ("SINR","SINR & NR-SINR")
            self.sinr_graph = GraphFrame(graph_frm, title[lines-1], lines_qty=lines)
            self.sinr_graph.grid(row=0,column=col,sticky=tk.NSEW)
            self.sinr_graph.columnconfigure(0,weight=1)
            self.sinr_graph.rowconfigure(0,weight=1)