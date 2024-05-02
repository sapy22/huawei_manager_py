from .view import StatisticsView
from .utils import convert_bytes, convert_to_mb
import datetime




class StatisticsController(StatisticsView):
    def __init__(self, master, settings_data):
        super().__init__(master, settings_data)
        self.dl_speed = 0
        self.ul_speed = 0

        self.time = 0

        self.time_list = []
        self.dl_speed_v_list = []
        self.ul_speed_v_list = []


    def update_traffic_info(self,data):
        self._traffic_info(data)
        self._dl_ul_graph_info()


    def _traffic_info(self,data):
        try:
            CurrentDownloadRate = data.get("CurrentDownloadRate")
            CurrentDownload = data.get("CurrentDownload")
            TotalDownload = data.get("TotalDownload")

            CurrentUploadRate = data.get("CurrentUploadRate")
            CurrentUpload = data.get("CurrentUpload")
            TotalUpload = data.get("TotalUpload")

            CurrentConnectTime = data.get("CurrentConnectTime")
            TotalConnectTime = data.get("TotalConnectTime")

            # data cleaning
            self.dl_speed = convert_to_mb(CurrentDownloadRate)
            self.ul_speed = convert_to_mb(CurrentUploadRate)

            CurrentDownloadRate = convert_bytes(CurrentDownloadRate)
            CurrentDownload = convert_bytes(CurrentDownload)
            TotalDownload = convert_bytes(TotalDownload)

            CurrentUploadRate = convert_bytes(CurrentUploadRate)
            CurrentUpload = convert_bytes(CurrentUpload)
            TotalUpload = convert_bytes(TotalUpload)

            CurrentConnectTime = str(datetime.timedelta(seconds=int(CurrentConnectTime)))
            TotalConnectTime = str(datetime.timedelta(seconds=int(TotalConnectTime)))


            # adding the data to the ui
            self.current_dl_rate_v.set(CurrentDownloadRate)
            self.current_dl_v.set(CurrentDownload)
            self.total_dl_v.set(TotalDownload)

            self.current_ul_rate_v.set(CurrentUploadRate)
            self.current_ul_v.set(CurrentUpload)
            self.total_ul_v.set(TotalUpload)

            self.current_conn_time_v.set(CurrentConnectTime)
            self.total_conn_time_v.set(TotalConnectTime)

        except Exception as e:
            print(e)
        

    def _dl_ul_graph_info(self):
        try:
            dl_ul_graph = self.settings_data.get("ui").get("dl_ul_graph")
            
            if not dl_ul_graph:
                return

            self.time_list.append(self.time)

            self.dl_speed_v_list.append(self.dl_speed)
            self.dl_graph.update_graph(self.time_list, (self.dl_speed_v_list,))

            self.ul_speed_v_list.append(self.ul_speed)
            self.ul_graph.update_graph(self.time_list, (self.ul_speed_v_list,))

        except Exception as e:
                print(e)
    

    def reset(self):
        self.time_list.clear()
        self.dl_speed_v_list.clear()
        self.ul_speed_v_list.clear()