from .view import SettingsView

from src.shared.settings import save_settings
from src.shared.localize import lc_is_rtl_layout, regrid_frame
from src.shared.utils import show_message




class SettingsController(SettingsView):
    def __init__(self, master, settings_data):
        super().__init__(master)
        self.btn_pressed = ""

        self.setup_event_handler()

        if settings_data:
            self.load_data(settings_data)

        self.check_locale()

        
    
    
    # init
    def setup_event_handler(self):
        self.save_btn.configure(command=self.on_save_btn_pressed)
    

    # event handler
    def on_save_btn_pressed(self):
        self.save_data()
    

    # logic
    def save_data(self):
        try:
            data_continer = {}
            self.connection_tab.save_data(data_continer)
            self.language_tab.save_data(data_continer)
            self.ui_tab.save_data(data_continer)
            
            save_settings(data_continer)

            self.btn_pressed = "save"
            self.master.destroy()
        
        except Exception as e:
            show_message(0,e,parent=self)


    def load_data(self, settings_data):
        self.connection_tab.load_data(settings_data)
        self.language_tab.load_data(settings_data)
        self.ui_tab.load_data(settings_data)
    
    
    def check_locale(self):
        if lc_is_rtl_layout():
            regrid_frame(self)