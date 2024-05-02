from threading import Thread
import time

from huawei_lte_api.Client import Client
from huawei_lte_api.exceptions import ResponseErrorLoginRequiredException

from src.shared.connection import connect




class MonitoringTask(Thread):
    def __init__(self,conn_data):
        super().__init__(daemon=True)
        self.conn_data = conn_data
        
        self.setup_vars()
    
    # init
    def setup_vars(self):
        self.connection = None
        self.client = None

        self.stopped = False
        self.error = ""

        self.app_runtime = 0.0
        self.data_ready = False

    # logic
    def run(self):
        try:
            self.create_client()
            self.get_data()
            
        except Exception as e:
            self.error = e


    def create_client(self):
        self.connection = connect(self.conn_data)
        self.client = Client(self.connection)


    def get_data(self):
        try:
            self._loop()
        except:
            raise
        finally:
            self.connection.close()


    def _loop(self):
        app_start_time = time.time()
        while not self.stopped:
            try:
                loop_time_start = time.time()

                self.network_data = self.client.net.current_plmn()
                self.signal_data = self.client.device.signal()
                self.conn_endc_data = self.client.monitoring.status()
                self.traffic_data = self.client.monitoring.traffic_statistics()
                

                self.data_ready = True

                loop_time = (time.time() - loop_time_start)
                # print(loop_time)
                # sleep if loop time < 1 sec
                time.sleep(max(0, 1 - loop_time))

                self.app_runtime = time.time() - app_start_time
        
            except ResponseErrorLoginRequiredException:

                if self.conn_data.get("keep_conn"):
                    self.create_client()
                else:
                    raise Exception(_("login required"))
            
            except:
                raise
    

    def stop_task(self):
        self.stopped = True