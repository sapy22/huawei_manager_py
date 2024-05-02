from threading import Thread

from huawei_lte_api.Client import Client

from src.shared.connection import connect




class GetTask:
    def __init__(self,conn_data):
        self.conn_data = conn_data
        self.data = None
        self.error = ""
        self.data_ready = False


    def get_data(self, btn_name: str):
        Thread(target=self._get_data,args=[btn_name],daemon=True).start()
    
    def _get_data(self, btn_name):
        
        try:
            connection = connect(self.conn_data)
            client = Client(connection)

            try:
                match btn_name:
                    case "signal":
                        self.data = client.device.signal()
                    case "information":
                        self.data = client.device.information()
                    case "plmn":
                        self.data = client.net.current_plmn()
                    case "plmn_list":
                        self.data = client.net.plmn_list()
                    case "net_mode":
                        self.data = client.net.net_mode()
                    case "net_mode_list":
                        self.data = client.net.net_mode_list()
                    case "status":
                        self.data = client.monitoring.status()
                    case "settings":
                        self.data = client.dhcp.settings()

                self.data_ready = True
            except:
                raise
            finally:
                connection.close()

        except Exception as e:
            self.error = e