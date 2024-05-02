from .view import MonitorView
from . utils import split_tx, split_k, split_d




class MonitorController(MonitorView):
    def __init__(self, master, settings_data):
        super().__init__(master, settings_data)
        self.color_list = ["#1FC600","lightgreen","yellow","orange"]
        self.rsrq_value_list = [-4,-8,-12,-16]
        self.rsrp_value_list = [-74,-78,-82,-86]
        self.sinr_value_list = [16,12,8,4]

        self.rsrq = 0
        self.rsrp = 0
        self.sinr = 0
        self.nrrsrq = 0
        self.nrrsrp = 0
        self.nrsinr = 0

        self.time = 0
        
        self.time_list = []
        self.rsrq_v_list = []
        self.nrrsrq_v_list = []
        self.rsrp_v_list = []
        self.nrrsrp_v_list = []
        self.sinr_v_list = []
        self.nrsinr_v_list = []


    def update_network_info(self,data):
        try:
            fullname = data.get("FullName","")

            # adding the data to the ui
            self.fullname_v.set(fullname)
        except Exception as e:
            print(e)


    def _lte_4g_info(self,data):
        try:
            # get data
            rsrq = data["rsrq"]
            rsrp = data["rsrp"]
            sinr = data["sinr"]
            txpower = data["txpower"]
            band = data.get("band","")
            dlbandwidth = data.get("dlbandwidth","")
            rssi = data.get("rssi","")

            # data cleaning
            self.rsrq = split_d(rsrq)
            self.rsrp = split_d(rsrp)
            self.sinr = split_d(sinr)
            txpower = split_tx(txpower)
            if band:
                band = f"B{band}"
            
            # adding data to the ui
            self.rsrq_lbl_v["text"] = self.rsrq
            self.rsrp_lbl_v["text"] = self.rsrp
            self.sinr_lbl_v["text"] = self.sinr
            self.txpower_v.set(txpower)
            self.band_v.set(band)
            self.dlbandwidth_v.set(dlbandwidth)
            self.rssi_v.set(rssi)

        except Exception as e:
            print(e)


    def _lte_4g_coloring(self):
        try:
            if self.rsrq == 0:
                self.rsrq_lbl_v["background"] = "white"
                self.rsrp_lbl_v["background"] = "white"
                self.sinr_lbl_v["background"] = "white"
                return
            
            if self.rsrq >= self.rsrq_value_list[-1]:
                for value, color in zip(self.rsrq_value_list,self.color_list):
                    if self.rsrq >= value:
                        self.rsrq_lbl_v["background"] = color
                        break
            else:
                self.rsrq_lbl_v["background"] = "red"
            #
            if self.rsrp >= self.rsrp_value_list[-1]:
                for value, color in zip(self.rsrp_value_list,self.color_list):
                    if self.rsrp >= value:
                        self.rsrp_lbl_v["background"] = color
                        break
            else:
                self.rsrp_lbl_v["background"] = "red"
            #
            if self.sinr >= self.sinr_value_list[-1]:
                for value, color in zip(self.sinr_value_list,self.color_list):
                    if self.sinr >= value:
                        self.sinr_lbl_v["background"] = color
                        break
                else:
                    self.sinr_lbl_v["background"] = "red"

        except Exception as e:
            print(e,"_lte_4g_coloring")


    def _nr_5g_info(self,data):
        try:
            # get data
            nrrsrq = data["nrrsrq"]
            nrrsrp = data["nrrsrp"]
            nrsinr = data["nrsinr"]
            nrtxpower = data["nrtxpower"]
            nrdlfreq = data["nrdlfreq"]
            nrdlbandwidth = data["nrdlbandwidth"]
            mode = data.get("mode","")

            # data cleaning
            self.nrrsrq = split_d(nrrsrq)
            self.nrrsrp = split_d(nrrsrp)
            self.nrsinr = split_d(nrsinr)
            nrtxpower = split_tx(nrtxpower)
            nrdlfreq = split_k(nrdlfreq)
            
            
            if nrdlfreq >= 3300 <=3800:
                nrband = "N78 or N77"
            elif nrdlfreq > 3800 <=4200:
                nrband = "N77"
            elif nrdlfreq >= 2496 <=2690:
                nrband = "N41"
            elif nrdlfreq == 0:
                nrband = ""
            else:
                nrband = str(nrdlfreq)

            # adding data to the ui
            self.nrrsrq_lbl_v["text"] = self.nrrsrq
            self.nrrsrp_lbl_v["text"] = self.nrrsrp
            self.nrsinr_lbl_v["text"] = self.nrsinr
            self.nrtxpower_v.set(nrtxpower)
            self.nrband_v.set(nrband)
            self.nrdlbandwidth_v.set(nrdlbandwidth)
            self.mode_v.set(mode)

        except Exception as e:
            print(e,type(e))


    def _nr_5g_coloring(self):
        try:
            if self.nrrsrq == 0:
                self.nrrsrq_lbl_v["background"] = "white"
                self.nrrsrp_lbl_v["background"] = "white"
                self.nrsinr_lbl_v["background"] = "white"
                return

            if self.nrrsrq >= self.rsrq_value_list[-1]:
                for value, color in zip(self.rsrq_value_list,self.color_list):
                    if self.nrrsrq >= value:
                        self.nrrsrq_lbl_v["background"] = color
                        break
            else:
                self.nrrsrq_lbl_v["background"] = "red"
            #
            if self.nrrsrp >= self.rsrp_value_list[-1]:
                for value, color in zip(self.rsrp_value_list,self.color_list):
                    if self.nrrsrp >= value:
                        self.nrrsrp_lbl_v["background"] = color
                        break
            else:
                self.nrrsrp_lbl_v["background"] = "red"
            #   
            if self.nrsinr >= self.sinr_value_list[-1]:
                for value, color in zip(self.sinr_value_list,self.color_list):
                    if self.nrsinr >= value:
                        self.nrsinr_lbl_v["background"] = color
                        break
            else:
                self.nrsinr_lbl_v["background"] = "red"
        
        except Exception as e:
            print(e,"_nr_5g_coloring")


    def _tower_info(self,data):
        try:
            # get data
            pci = data.get("pci","")
            cell_id = data["cell_id"]
            enodeb_id = data["enodeb_id"]
            try:
                cid = str(int(cell_id)-(int(enodeb_id)*256))
            except:
                cid = ""

            # adding data to the ui
            self.pci_v.set(pci)
            self.cid_v.set(cid)

        except Exception as e:
            print(e)


    def _4g_5g_graph_info(self):
        try:
            settings = self.settings_data.get("ui")
            nr_5g = settings.get("nr_5g")
            rsrq_graph = settings.get("rsrq_graph")
            rsrp_graph = settings.get("rsrp_graph")
            sinr_graph = settings.get("sinr_graph")
            
            if (not rsrq_graph) and (not rsrp_graph) and (not sinr_graph):
                return

            self.time_list.append(self.time)

            if nr_5g:
                if rsrq_graph:
                    self.rsrq_v_list.append(self.rsrq)
                    self.nrrsrq_v_list.append(self.nrrsrq)
                    self.rsrq_graph.update_graph(self.time_list, (self.rsrq_v_list,self.nrrsrq_v_list))

                if rsrp_graph:
                    self.rsrp_v_list.append(self.rsrp)
                    self.nrrsrp_v_list.append(self.nrrsrp)
                    self.rsrp_graph.update_graph(self.time_list, (self.rsrp_v_list,self.nrrsrp_v_list))

                if sinr_graph:
                    self.sinr_v_list.append(self.sinr)
                    self.nrsinr_v_list.append(self.nrsinr)
                    self.sinr_graph.update_graph(self.time_list, (self.sinr_v_list,self.nrsinr_v_list))
            else: # 4g only
                if rsrq_graph:
                    self.rsrq_v_list.append(self.rsrq)
                    self.rsrq_graph.update_graph(self.time_list, (self.rsrq_v_list,))

                if rsrp_graph:
                    self.rsrp_v_list.append(self.rsrp)
                    self.rsrp_graph.update_graph(self.time_list, (self.rsrp_v_list,))

                if sinr_graph:
                    self.sinr_v_list.append(self.sinr)
                    self.sinr_graph.update_graph(self.time_list, (self.sinr_v_list,))

        except Exception as e:
                print(e)


    def update_signal_info(self,data):
        self._lte_4g_info(data)
        self._lte_4g_coloring()

        if self.settings_data.get("ui").get("nr_5g"):
            self._nr_5g_info(data)
            self._nr_5g_coloring()
    
        self._4g_5g_graph_info()

        self._tower_info(data)

    

    def update_conn_endc_info(self,data):
        try:
            connectionstatus = data["ConnectionStatus"]
            endcstatus = data["EndcStatus"]
            signalicon = data["SignalIcon"]
            signaliconnr = data["SignalIconNr"]
            currentnetworktype = data["CurrentNetworkType"]
            currentnetworktypeex = data["CurrentNetworkTypeEx"]

            #
            connection_status_dict = {"900":_("connecting"),"901":_("connected"),"902":_("disconnected"),"905":_("no connection"),"906":_("connection error")}
            endc_status_dict = {"0":_("restricted"),"1":_("unrestricted")} #  NSA_DC 4G5G_DC
            network_type_dict = {"19":"LTE","20":"LTE_NR","101":"LTE","1011":"LTE CA","111":"NR"}

            # adding the data to the ui
            self.conn_v.set(connection_status_dict.get(connectionstatus,connectionstatus))
            self.endc_v.set(endc_status_dict.get(endcstatus,endcstatus))
            self.signal_bar.update_value(signalicon)
            self.nr_signal_bar.update_value(signaliconnr)
            self.current_network_type_v.set(network_type_dict.get(currentnetworktype,currentnetworktype))
            self.current_network_type_ex_v.set(network_type_dict.get(currentnetworktypeex,currentnetworktypeex))

            # coloring
            # conn
            if connectionstatus == "901":
                self.conn_lbl_v["background"] = "lightgreen"
            else:
                self.conn_lbl_v["background"] = "red"
            # endc
            if endcstatus == "1":
                self.endc_lbl_v["background"] = "lightgreen"
            else:
                self.endc_lbl_v["background"] = "red"
        except Exception as e:
            print(e)


    def reset(self):
        self.time_list.clear()
        self.rsrq_v_list.clear()
        self.nrrsrq_v_list.clear()
        self.rsrp_v_list.clear()
        self.nrrsrp_v_list.clear()
        self.sinr_v_list.clear()
        self.nrsinr_v_list.clear()