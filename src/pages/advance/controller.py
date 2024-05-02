from .view import AdvanceView

from src.shared.localize import lc_is_rtl_layout, regrid_frame




class AdvanceController(AdvanceView):
    def __init__(self, master, settings_data):
        super().__init__(master, settings_data)
        self.check_locale()


    def check_locale(self):
        if lc_is_rtl_layout():
            regrid_frame(self)