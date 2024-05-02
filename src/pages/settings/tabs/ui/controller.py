from .view import UIView




class UIController(UIView):
    def __init__(self, master):
        super().__init__(master)
        pass


    # logic
    def save_data(self,data):
        data["ui"] = {
            "nr_5g" : self.nr_5g_mode_v.get(),
            "rsrq_graph" : self.rsrq_graph_v.get(),
            "rsrp_graph" : self.rsrp_graph_v.get(),
            "sinr_graph" : self.sinr_graph_v.get(),
            "dl_ul_graph" : self.dl_ul_graph_v.get()
        }
        

    def load_data(self, data):
        data = data.get("ui")
        
        self.nr_5g_mode_v.set(data.get("nr_5g"))
        self.rsrq_graph_v.set(data.get("rsrq_graph"))
        self.rsrp_graph_v.set(data.get("rsrp_graph"))
        self.sinr_graph_v.set(data.get("sinr_graph"))
        self.dl_ul_graph_v.set(data.get("dl_ul_graph"))