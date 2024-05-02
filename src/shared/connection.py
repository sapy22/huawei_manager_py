from huawei_lte_api.Connection import Connection
from huawei_lte_api.exceptions import LoginErrorUsernameWrongException, LoginErrorPasswordWrongException, \
     LoginErrorAlreadyLoginException, LoginErrorUsernamePasswordWrongException, \
     LoginErrorUsernamePasswordOverrunException, LoginErrorUsernamePasswordModifyException

from requests.exceptions import ConnectTimeout

from .exceptions import ConnectError, ConnectIpUsernamePasswordEmpty, ConnectUsernamePasswordWrong, ConnectPasswordOverrun, ConnectRequestTimeout




def connect(conn_data):
    try :
        ip = conn_data.get("ip")
        user = conn_data.get("user")
        password = conn_data.get("password")

        if (not ip) or (not user) or (not password):
            raise ConnectIpUsernamePasswordEmpty

        return Connection(f"http://{ip}", username=user, password=password)


    except ConnectIpUsernamePasswordEmpty:
        raise ConnectIpUsernamePasswordEmpty(_("IP or User or Password is empty!"))
    
    except (LoginErrorUsernameWrongException, LoginErrorPasswordWrongException, LoginErrorUsernamePasswordWrongException):
        raise ConnectUsernamePasswordWrong(_("Username or Password is wrong!"))

    except LoginErrorUsernamePasswordOverrunException:
        raise ConnectPasswordOverrun(_("Password is overrun wait a few minutes."))
    
    except ConnectTimeout:
        raise ConnectRequestTimeout(_("Request timed out while trying to connect."))
        
    except:
        raise ConnectError(_("Connect Error!"))