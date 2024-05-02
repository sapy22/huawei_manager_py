from .view import SetView

from .task import SetTask

from src.shared.utils import show_message ,disable_children_widgets ,enable_children_widgets
from src.shared.settings import get_ip_address




class SetController(SetView):
    def __init__(self, master, settings_data):
        super().__init__(master)
        self.set_task = SetTask(settings_data.get("connection"))

        self.setup_vars()
        self.setup_event_handler()


    # init
    def setup_vars(self):
        self.dns_ip_v.set(get_ip_address())

    
    def setup_event_handler(self):
        self.power_shutdown_btn.configure(command=lambda: self.on_power_btn_pressed("shutdown"))
        self.power_restart_btn.configure(command=lambda: self.on_power_btn_pressed("restart"))
        self.power_reset_btn.configure(command=lambda: self.on_power_btn_pressed("reset"))

        self.dns_apply_btn.configure(command=lambda: self.on_dns_btn_pressed("apply"))
        self.dns_reset_btn.configure(command=lambda: self.on_dns_btn_pressed("reset"))


    # event handler
    def on_power_btn_pressed(self, btn_name: str):
        if btn_name == "shutdown":
            msg = _("The device will shutdown. Continue??")
            value = 4
        elif btn_name == "restart":
            msg = _("The device will restart. Continue?")
            value = 1
        elif btn_name == "reset":
            msg = _("All configurations will be restored to factory settings. Continue?")
            value = 2
        
        if not show_message(3, msg, self):
            return
        
        self.set_power(value)


    def on_dns_btn_pressed(self, btn_name: str):
        if btn_name == "apply":
            msg = _("Apply dns settings. Continue?")
            ip = self.dns_ip_v.get()
            primary = self.dns_primary_v.get()
            secondary = self.dns_secondary_v.get()
            dns_status = 0

        elif btn_name == "reset":
            msg = _("Reset dns settings. Continue?")
            ip = self.dns_ip_v.get()
            primary = ""
            secondary = ""
            dns_status = 1

        if not show_message(3, msg, self):
            return

        self.set_dns(ip,primary,secondary,dns_status)


    # logic
    def set_power(self, value: int):
        self.set_task.set_power(value)

        self._show_set_response()
    

    def set_dns(self, ip, primary, secondary, dns_status):
        self.set_task.set_dns(ip, primary, secondary, dns_status)

        self._show_set_response()


    def _show_set_response(self):
        if self.set_task.error:
            show_message(0, self.set_task.error, self)
            self.set_task.error = ""
            return

        if not self.set_task.set_response:
            self.after(100, self._show_set_response)
            return

        show_message(2, self.set_task.set_response)
        self.set_task.set_response = ""