import unittest
from src.shared.settings.validator import _validate_conn_settings, _validate_lang_settings, _validate_ui_settings, SettingsDataInvalid




class TestConnValidator(unittest.TestCase):
    def test_data_empty(self):
        with self.assertRaises(SettingsDataInvalid):
            data = {}
            _validate_conn_settings(data)
    
    def test_data_empty_2(self):
        with self.assertRaises(SettingsDataInvalid):
            data = {"connection": {"ip": ""}}
            _validate_conn_settings(data)
    
    def test_ip_type_wrong(self):
        with self.assertRaises(SettingsDataInvalid):
            data = {"connection": {"ip": 1,"user": "","password": "","keep_conn": False}}
            _validate_conn_settings(data)

    def test_user_type_wrong(self):
        with self.assertRaises(SettingsDataInvalid):
            data = {"connection": {"ip": "","user": 1,"password": "","keep_conn": False}}
            _validate_conn_settings(data)

    def test_password_type_wrong(self):
        with self.assertRaises(SettingsDataInvalid):
            data = {"connection": {"ip": "","user": "","password": 1,"keep_conn": False}}
            _validate_conn_settings(data)
    
    def test_keep_conn_type_wrong(self):
        with self.assertRaises(SettingsDataInvalid):
            data = {"connection": {"ip": "","user": "","password": "","keep_conn": 1}}
            _validate_conn_settings(data)



if __name__ == '__main__':
    unittest.main()