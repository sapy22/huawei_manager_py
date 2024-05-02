from src.shared.exceptions import SettingsDataInvalid




def _validate_conn_settings(data):
    try:
        data = data.get("connection")
        err = False
        
        ip = data.get("ip")
        if not type(ip) is str:
            err = True
        
        user = data.get("user")
        if not type(user) is str:
            err = True
        
        password = data.get("password")
        if not type(password) is str:
            err = True
        
        keep_conn = data.get("keep_conn")
        if not type(keep_conn) is bool:
            err = True
        
        if err:
            raise SettingsDataInvalid(_("Connection settings invalid!"))
    except:
        raise SettingsDataInvalid(_("Connection settings invalid!"))


def _validate_lang_settings(data):
    try:
        data = data.get("language")
        err = False

        lang = data.get("language")
        if not type(lang) is str:
            err = True

        direc = data.get("direction")
        if not type(direc) is str:
            err = True
        
        if err:
            raise SettingsDataInvalid(_("Language settings invalid!"))
    except:
        raise SettingsDataInvalid(_("Language settings invalid!"))


def _validate_ui_settings(data):
    try:
        data = data.get("ui")
        err = False

        nr_5g = data.get("nr_5g")
        if not type(nr_5g) is bool:
            err = True

        rsrq_graph = data.get("rsrq_graph")
        if not type(rsrq_graph) is bool:
            err = True

        rsrp_graph = data.get("rsrp_graph")
        if not type(rsrp_graph) is bool:
            err = True

        sinr_graph = data.get("sinr_graph")
        if not type(sinr_graph) is bool:
            err = True
        
        dl_ul_graph = data.get("dl_ul_graph")
        if not type(dl_ul_graph) is bool:
            err = True
        
        if err:
            raise SettingsDataInvalid(_("UI settings invalid!"))
    except:
        raise SettingsDataInvalid(_("UI settings invalid!"))


def validate_settings(data):
    try:
        _validate_conn_settings(data)
        _validate_lang_settings(data)
        _validate_ui_settings(data)

    except:
        raise