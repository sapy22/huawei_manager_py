import unittest
from src.shared.connection import connect, ConnectError, ConnectIpUsernamePasswordEmpty, ConnectUsernamePasswordWrong, ConnectPasswordOverrun, ConnectRequestTimeout




class TestConnect(unittest.TestCase):
    def test_ip_user_password_empty(self):
        with self.assertRaises(ConnectIpUsernamePasswordEmpty):
            data = {"ip":"","user":"","password":""}
            connect(data)

        with self.assertRaises(ConnectIpUsernamePasswordEmpty):
            data = {"ip":"1","user":"","password":""}
            connect(data)

        with self.assertRaises(ConnectIpUsernamePasswordEmpty):
            data = {"ip":"1","user":"a","password":""}
            connect(data)


    def test_ip_wrong(self):
        with self.assertRaises(ConnectError):
            data = {"ip":"1","user":"a","password":"a"}
            connect(data)
        
        with self.assertRaises(ConnectError):
            data = {"ip":"1.1","user":"a","password":"a"}
            connect(data)

        with self.assertRaises(ConnectError):
            data = {"ip":"1.1.1","user":"a","password":"a"}
            connect(data)
    

    # def test_request_timeout(self):
    #     with self.assertRaises(ConnectRequestTimeout):
    #         data = {"ip":"192.168.192.168","user":"a","password":"a"}
    #         connect(data)


    def test_user_or_password_wrong_or_overrun(self):
        with self.assertRaises((ConnectUsernamePasswordWrong, ConnectPasswordOverrun)):
            data = {"ip":"192.168.8.1","user":"a","password":"a"}
            connect(data)


if __name__ == '__main__':
    unittest.main()