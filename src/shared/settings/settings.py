from pathlib import Path
import json

from src.shared.constant import LanguageDict, DirectionDict
from src.shared.exceptions import SettingsError, SettingsFileNotExist, SettingsFileInvalid, SettingsDataInvalid

from .validator import validate_settings




settings_data = {}

root_dir = Path(__file__).parent.parent.parent.parent

resources_dir = root_dir / "src" /"resources"

settings_file_path = root_dir / "settings.json"




###
def _save_to_file_json(file_path, data):
    try:
        with open(file_path, mode="w", encoding='utf8') as f:
                json.dump(data, f,indent=2)
    except:
        raise


def save_settings(data):
    _save_to_file_json(settings_file_path, data)


###
def _load_from_file_json(file_path):
    if not file_path.exists():
        raise SettingsFileNotExist(_("Settings file does not exist!"))
    
    try:
        with open(file_path, "r", encoding='utf8') as f:
            data = json.load(f)

        return data

    except json.decoder.JSONDecodeError:
        raise SettingsFileInvalid(_("Settings file invalid!"))

    except SettingsDataInvalid:
        raise
        
    except:
        raise SettingsError(_("Settings file error!"))


def load_settings():
    data = _load_from_file_json(settings_file_path)

    validate_settings(data)
    
    settings_data.update(data)

    return settings_data


###
def get_settings_data():
    return settings_data


###
def get_language():
    default_lang = LanguageDict.get("English")

    try:
        lang = settings_data.get("language").get("language")
    except:
        lang = None
    
    if lang and lang in LanguageDict.values():
        return lang 
    
    return default_lang


def get_layout_direction():
    default_dir = DirectionDict.get("Left to Right")

    try:
        dir_ = settings_data.get("language").get("direction")
    except:
         dir_ = None
    
    if dir_ and dir_ in DirectionDict.values():
        return dir_
    
    return default_dir


def get_ip_address():
    try:
        ip = settings_data.get("connection").get("ip")
    except:
         ip = ""
    
    return ip