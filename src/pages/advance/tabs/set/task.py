from threading import Thread

from huawei_lte_api.Client import Client
from huawei_lte_api.enums.device import ControlModeEnum

from src.shared.connection import connect




class SetTask:
    def __init__(self, conn_data):
        self.conn_data = conn_data
        self.error = ""
        self.set_response = ""


    def set_power(self, value: int):
        if value == 4:
            control = ControlModeEnum.POWER_OFF
        elif value == 1:
            control = ControlModeEnum.REBOOT
        elif value == 2:
            control = ControlModeEnum.RESET
        
        Thread(target=self._set_power,args=[control],daemon=True).start()
    
    def _set_power(self, control):
        try:
            connection = connect(self.conn_data)
            client = Client(connection)

            try:
                self.set_response = client.device.set_control(control=control)
            except:
                raise
            finally:
                connection.close()

        except Exception as e:
            self.error = e


    def set_dns(self, ip: str, primary: str, secondary: str, dns_status: int):
        Thread(target=self._set_dns,args=[ip,primary,secondary,dns_status],daemon=True).start()

    def _set_dns(self, ip, primary, secondary, dns_status):
        try:
            connection = connect(self.conn_data)
            client = Client(connection)

            try:
                self.set_response = client.dhcp.set_settings(dhcp_ip_address=ip,dns_status=dns_status,primary_dns=primary,secondary_dns=secondary)
            except:
                raise
            finally:
                connection.close()

        except Exception as e:
            self.error = e