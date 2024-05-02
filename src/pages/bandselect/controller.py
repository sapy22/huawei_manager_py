from .view import BandSelectView

from .task import BandSelectTask

from src.shared.localize import lc_is_rtl_layout, regrid_frame
from src.shared.constant import StyleDict
from src.shared.utils import disable_children_widgets, enable_children_widgets, show_message
from src.shared.widgets import Notification




class BandSelectController(BandSelectView):
    def __init__(self, master, settings_data):
        super().__init__(master)
        self.band_select_task = BandSelectTask(settings_data.get("connection"))

        self.setup_vars()
        self.setup_event_handler()
        
        self.check_locale()

        self.get_net_mode()


    # init
    def setup_vars(self):
        self.selected_lte_band: list[str] = []
 
        self.current_hinted_btns: tuple = ()

        self.stc_btns = (self.b1_chk_btn,self.b3_chk_btn,self.b8_chk_btn,self.b28_chk_btn,self.b40_chk_btn)
        self.mobily_btns = (self.b1_chk_btn,self.b3_chk_btn,self.b20_chk_btn,self.b38_chk_btn,self.b41_chk_btn)
        self.zain_btns = (self.b1_chk_btn,self.b3_chk_btn,self.b8_chk_btn,self.b20_chk_btn,self.b38_chk_btn)

    
    def setup_event_handler(self):
        for chk_btn in self.lte_band_frm.grid_slaves():
            btn_text = chk_btn["text"].split("-")[0]
            chk_btn.configure(command=lambda t=btn_text : self.on_lte_band_chk_btn_pressed(t))

        self.apply_btn.configure(command=self.on_apply_btn_pressed)
        self.clear_btn.configure(command=self.on_clear_btn_pressed)


    # event handler
    def on_lte_band_chk_btn_pressed(self,btn_text: str):
        if btn_text in self.selected_lte_band:
            self.selected_lte_band.remove(btn_text)
            return
        
        self.selected_lte_band.append(btn_text)
    

    def on_lte_band_rd_btn_pressed(self,value):
        match value:
            case "auto":
                disable_children_widgets(self.lte_band_frm)
            case "manual":
                enable_children_widgets(self.lte_band_frm)


    def on_band_hint_rd_btn_pressed(self,value):
        match value:
            case "none":
                self._clear_band_hint()
            case "stc":
                self._clear_band_hint()
                self._apply_band_hint(self.stc_btns)
            case "mobily":
                self._clear_band_hint()
                self._apply_band_hint(self.mobily_btns)
            case "zain":
                self._clear_band_hint()
                self._apply_band_hint(self.zain_btns)
    

    def on_clear_btn_pressed(self):
        if not self.selected_lte_band:
            return
        
        for btn_txt in self.selected_lte_band:
            btn_txt = btn_txt.lower()
            getattr(self,f"{btn_txt}_v").set(False)
        
        self.selected_lte_band.clear()


    def on_apply_btn_pressed(self):
        if not show_message(3,_("Apply band settings. Continue?")):
            return

        if self.lte_band_v.get() == "manual" and not self.selected_lte_band:
            show_message(0,_("Choose at least one lte band!"))
            return

        self.apply_btn.configure(state="disabled")

        self.set_net_mode()

    
    # logic
    def get_net_mode(self):
        Notification(text="Connecting!")

        
        # task
        self.band_select_task.get_net_mode()
        
        self.update_ui()
    

    def update_ui(self):
        if self.band_select_task.error:
            show_message(0,self.band_select_task.error)
            self.band_select_task.error = ""
            return

        if not self.band_select_task.data_ready:
            self.after(100, self.update_ui)
            return
        
        self.band_select_task.data_ready = False

        self._update_ui(self.band_select_task.net_mode_data)


    def _update_ui(self,data):
        try:
            networkmode = data["NetworkMode"]
            networkband = data["NetworkBand"]
            lteband = data["LTEBand"]

            #
            lteband_dict = {
                    "7E288080095":"1+3+5+8+20+28+32+34+38+39+40+41+42+43",
                    "7E2880800D5":"Auto",
                    "1":"B1",
                    "4":"B3",
                    "8000000":"B28",
                    "8000000000":"B40",
                    "5":"1+3",
                    "8000001":"1+28",
                    "8000004":"3+28",
                    "8000005":"1+3+28"
                }
            networkband_dict = {"3FFFFFFF":"Auto"}
            networkmode_dict = {"00":"Auto","03":"4G only","08":"NR"}
            
            networkmode = networkmode_dict.get(networkmode,networkmode)
            networkband = networkband_dict.get(networkband,networkband)
            lteband = lteband_dict.get(lteband,lteband)

            #
            self.network_mode_lbl_v.set(networkmode)
            self.network_band_lbl_v.set(networkband)
            self.lte_band_lbl_v.set(lteband)
        
        except:
            pass


    def _clear_band_hint(self):
        if not self.current_hinted_btns:
            return
        
        s = "TCheckbutton"
        if lc_is_rtl_layout():
            s = StyleDict.get("RTL Checkbutton")

        for btn in self.current_hinted_btns:
            btn.configure(style=s)
        
        self.current_hinted_btns = ()


    def _apply_band_hint(self, btns: tuple):
        self.current_hinted_btns = btns

        s = "hint.TCheckbutton"
        if lc_is_rtl_layout():
            s = StyleDict.get("Hint RTL Checkbutton")

        for btn in btns:
            btn.configure(style=s)
    

    def set_net_mode(self):
        band_data = {"lteband":self._get_lte_band_hex(),"networkband":self.network_band_v.get(),"networkmode":self.network_mode_v.get()}

        # task
        self.band_select_task.set_net_mode(band_data)

        self._show_set_net_mode_response()


    def _get_lte_band_hex(self) -> str:
        if self.lte_band_v.get() == "auto":
            return "7fffffffffffffff" # 7E2880800D5"
        
        l = []
        for band in self.selected_lte_band:
            band_num = int(band[1:]) # B1 -> 1
            l.append(2 ** (band_num - 1))

        return hex(sum(l))[2:] # 0x10... -> 10...


    def _show_set_net_mode_response(self):
        if self.band_select_task.error:
            show_message(0, self.band_select_task.error, self)
            self.band_select_task.error = ""
            self.apply_btn.configure(state="normal")
            return

        if not self.band_select_task.set_net_mode_response:
            self.after(100, self._show_set_net_mode_response)
            return

        show_message(2, self.band_select_task.set_net_mode_response)
        self.band_select_task.set_net_mode_response = ""

        self.apply_btn.configure(state="normal")
        
        self.after(100, self.get_net_mode)
    

    def check_locale(self):
        if lc_is_rtl_layout():
            regrid_frame(self)