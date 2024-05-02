import gettext

from .view import MainView
from .navbar import NavBar

from src.shared.settings import load_settings, get_language, resources_dir
from src.shared.utils import disable_children_widgets, show_message
from src.shared.exceptions import SettingsError, SettingsFileNotExist, SettingsFileInvalid, SettingsDataInvalid

from src.pages import SignalController, BandSelectController, SMSController, AdvanceController, SettingsController, AboutController




class MainController(MainView):
    def __init__(self):
        super().__init__()
        self.setup_vars()
        self.setup_translation()

        self.load_settings_data()


    # init
    def setup_vars(self):
        self.settings_data = None
        self.translation_dict = {}

        self.nav_bar = None
        self.pressed_btn = None
        self.active_page = None
        self.signal_page = None


    def setup_translation(self):
        en = gettext.translation("messages", localedir= resources_dir / "locale", languages=["en"])
        ar = gettext.translation("messages", localedir= resources_dir / "locale", languages=["ar_SA"])
        self.translation_dict["en"] = en
        self.translation_dict["ar_SA"] = ar


    def setup_nav_bar(self):
        self.nav_bar = NavBar(self.nav_frame)
        self.nav_bar.grid(row=0,column=0,sticky="nswe")
        self.nav_bar.columnconfigure(0,weight=1)
        
        self.nav_bar.signal_btn.configure(command=self.on_signal_btn_pressed)
        self.nav_bar.band_select_btn.configure(command=self.on_band_select_btn_pressed)
        self.nav_bar.sms_btn.configure(command=self.on_sms_btn_pressed)
        self.nav_bar.advance_btn.configure(command=self.on_advance_btn_pressed)
        self.nav_bar.settings_btn.configure(command=self.on_settings_btn_pressed)
        self.nav_bar.about_btn.configure(command=self.on_about_btn_pressed)


    # event handler
    def on_signal_btn_pressed(self):
        self._on_page_switch()

        self._disable_pressed_btn(self.nav_bar.signal_btn)

        if self.signal_page:
            self.signal_page.grid()
            self.active_page = self.signal_page
            return

        self.signal_page = SignalController(self.content_frame,self.settings_data)
        self.signal_page.grid(row=0,column=0,sticky="nswe")
        self.signal_page.rowconfigure(1,weight=1)
        self.signal_page.columnconfigure(0,weight=1)

        self.active_page = self.signal_page


    def on_band_select_btn_pressed(self):
        self._on_page_switch()
        
        self._disable_pressed_btn(self.nav_bar.band_select_btn)

        band_select_page = BandSelectController(self.content_frame,self.settings_data)
        band_select_page.grid(row=0,column=0,sticky="nswe")
        band_select_page.columnconfigure(0,weight=1)

        self.active_page = band_select_page


    def on_sms_btn_pressed(self):
        self._on_page_switch()
        
        self._disable_pressed_btn(self.nav_bar.sms_btn)

        sms_page = SMSController(self.content_frame,self.settings_data)
        sms_page.grid(row=0,column=0,sticky="nswe")
        sms_page.columnconfigure(0,weight=1)

        self.active_page = sms_page


    def on_advance_btn_pressed(self):
        self._on_page_switch()
        
        self._disable_pressed_btn(self.nav_bar.advance_btn)

        advance_page = AdvanceController(self.content_frame,self.settings_data)
        advance_page.grid(row=0,column=0,sticky="nswe")
        advance_page.columnconfigure(0,weight=1)

        self.active_page = advance_page


    def on_settings_btn_pressed(self):
        window = self.setup_toplevel_window(_("Settings"),"480x300")

        settings_page = SettingsController(window,self.settings_data)
        settings_page.grid(row=0,column=0,sticky="nswe")
        settings_page.columnconfigure(0,weight=1)

        window.grab_set()
        window.wait_window()

        if settings_page.btn_pressed == "save":
            self.load_settings_data()


    def on_about_btn_pressed(self):
        window = self.setup_toplevel_window(_("About"),"400x200")

        about_page = AboutController(window)
        about_page.grid(row=0,column=0,sticky="nswe")
        about_page.columnconfigure(0,weight=1)

        window.grab_set()


    # logic
    def _on_page_switch(self):
        if self.active_page:
            if isinstance(self.active_page, SignalController):
                self.active_page.on_stop_btn_pressed() # stop the bg task
                self.active_page.grid_remove() # hide
                return
                
            self.active_page.destroy()
    
    
    def _disable_pressed_btn(self,current_pressed_btn):
        if self.pressed_btn:
            self.pressed_btn.configure(state="normal")

        current_pressed_btn.configure(state="disable")
        self.pressed_btn = current_pressed_btn


    def load_settings_data(self):
        try:
            self.settings_data = load_settings()
            self._load_translation()

            
            if self.nav_bar:
                self.nav_bar.destroy()
                self.nav_bar = None

            self.setup_nav_bar()
            
            
            # reload after saving new settings
            if self.active_page:
                self._reload_active_page()

        except (SettingsError, SettingsFileNotExist, SettingsFileInvalid, SettingsDataInvalid) as e:
            show_message(0, e, self)

            if self.nav_bar:
                self.nav_bar.destroy()
                self.nav_bar = None

            self.setup_nav_bar()

            disable_children_widgets(self.nav_frame, (self.nav_bar.settings_btn,self.nav_bar.about_btn))

            self.on_settings_btn_pressed()


    def _load_translation(self):
        language = get_language()
        self.translation_dict[language].install()


    def _reload_active_page(self):
        # cleaning
        page = ""
        self.pressed_btn = None

        if isinstance(self.active_page, SignalController):
            self.signal_page = None
            self.active_page.on_stop_btn_pressed() # stop the bg task

            self.active_page.destroy()
            self.active_page = None
            page = "signal"
    
        elif isinstance(self.active_page, BandSelectController):
            self.active_page.destroy()
            self.active_page = None
            page = "bandselect"

        elif isinstance(self.active_page, SMSController):
            self.active_page.destroy()
            self.active_page = None
            page = "sms"
        
        elif isinstance(self.active_page, AdvanceController):
            self.active_page.destroy()
            self.active_page = None
            page = "advance"
        
        if self.signal_page:
            self.signal_page.destroy()
            self.signal_page = None
        
        # reload
        match page:
            case "signal":
                self.on_signal_btn_pressed()
            case "bandselect":
                self.on_band_select_btn_pressed()
            case "sms":
                self.on_sms_btn_pressed()
            case "advance":
                self.on_advance_btn_pressed()