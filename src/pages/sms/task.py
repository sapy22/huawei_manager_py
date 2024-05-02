from threading import Thread

from huawei_lte_api.Client import Client
from huawei_lte_api.enums.sms import BoxTypeEnum

from src.shared.connection import connect




class SMSTask:
    def __init__(self,conn_data):
        self.conn_data = conn_data
        self.sms_data = None
        self.error = ""
        self.data_ready = False
        self.send_sms_response = ""


    def get_all_sms(self, box_type):
        if box_type == "inbox":
            box_type = BoxTypeEnum.LOCAL_INBOX
        elif box_type == "outbox":
            box_type = BoxTypeEnum.LOCAL_SENT

        Thread(target=self._get_all_sms,args=[box_type],daemon=True).start()

    def _get_all_sms(self, box_type):
        
        try:
            connection = connect(self.conn_data)
            client = Client(connection)

            try:
                self.sms_data = list(client.sms.get_messages(box_type=box_type))
                self.data_ready = True
            except:
                raise
            finally:
                connection.close()

        except Exception as e:
            self.error = e
    

    def send_sms(self, numbers: list[str,...], msg: str):
        Thread(target=self._send_sms,args=[numbers,msg],daemon=True).start()
    

    def _send_sms(self, numbers, msg):
        try:
            connection = connect(self.conn_data)
            client = Client(connection)

            try:
                self.send_sms_response = client.sms.send_sms(phone_numbers=numbers, message=msg)
            except:
                raise
            finally:
                connection.close()

        except Exception as e:
            self.error = e