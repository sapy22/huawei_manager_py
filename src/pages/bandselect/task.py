from threading import Thread

from huawei_lte_api.Client import Client

from src.shared.connection import connect




class BandSelectTask:
    def __init__(self,conn_data):
        self.conn_data = conn_data
        self.net_mode_data = None
        self.error = ""
        self.data_ready = False
        self.set_net_mode_response = ""
    

    def get_net_mode(self):
        Thread(target=self._get_net_mode,daemon=True).start()
    
    def _get_net_mode(self):
        try:
            connection = connect(self.conn_data)
            client = Client(connection)

            try:
                self.net_mode_data = client.net.net_mode()
                self.data_ready = True
            except:
                raise
            finally:
                connection.close()

        except Exception as e:
            self.error = e
    

    def set_net_mode(self,band_data: dict):
        Thread(target=self._set_net_mode, args=[band_data],daemon=True).start()
    
    def _set_net_mode(self, band_data):
        try:
            connection = connect(self.conn_data)
            client = Client(connection)

            try:
                self.set_net_mode_response = client.net.set_net_mode(band_data["lteband"], band_data["networkband"], band_data["networkmode"])
            except:
                raise
            finally:
                connection.close()

        except Exception as e:
            self.error = e