import datetime

from src.shared.utils import show_message
from src.shared.localize import lc_is_rtl_layout, regrid_frame
from src.shared.widgets import Notification

from .view import SignalView
from .task import MonitoringTask




class SignalController(SignalView):
    def __init__(self, master, settings_data):
        super().__init__(master, settings_data)
        self.setup_vars()
        self.setup_event_handler()
        
        self.check_locale()
    

    # init
    def setup_event_handler(self):
        self.start_btn.configure(command=self.on_start_btn_pressed)
        self.stop_btn.configure(command=self.on_stop_btn_pressed)


    def setup_vars(self):
        self.active_btn: str = "stop"
        self.loop_chk_btn_value = True
        self.update_ui_flag = True
    
    
    # event handlers
    def on_start_btn_pressed(self):
        if self.active_btn != "stop":
            return

        self.active_btn = "start"
        self.start_btn.configure(state="disabled")
        self.stop_btn.configure(state="normal")
        self.update_ui_flag = True

        Notification(text="Connecting!")

        conn_data = self.settings_data.get("connection")
        
        self.monitoring_task = MonitoringTask(conn_data)
        self.monitoring_task.start()

        self.update_ui()


    def on_stop_btn_pressed(self):
        if self.active_btn != "start":
            return

        self.active_btn = "stop"
        self.stop_btn.configure(state="disabled")
        self.start_btn.configure(state="normal")

        self.monitoring_task.stop_task()
        self.update_ui_flag = False # self.after_cancel(self.next_ui_update_id)

        self.monitor_tab.reset()
        self.Statistics_tab.reset()


    # logic
    def update_ui(self):
        if not self.update_ui_flag:
            return

        if self.monitoring_task.error:
            show_message(0,self.monitoring_task.error,parent=self)

            self.on_stop_btn_pressed()
            return

        if not self.monitoring_task.data_ready:
            self.after(100, self.update_ui)
            return
        
        # update ui
        app_run_time = int(self.monitoring_task.app_runtime)
        
        self.app_runtime_v.set(datetime.timedelta(seconds=app_run_time))

        #
        self.monitor_tab.time = app_run_time
        self.monitor_tab.update_network_info(self.monitoring_task.network_data)
        self.monitor_tab.update_signal_info(self.monitoring_task.signal_data)
        self.monitor_tab.update_conn_endc_info(self.monitoring_task.conn_endc_data)

        self.Statistics_tab.time = app_run_time
        self.Statistics_tab.update_traffic_info(self.monitoring_task.traffic_data)

        #
        self.monitoring_task.data_ready = False
        
        self.after(100, self.update_ui)


    def check_locale(self):
        if lc_is_rtl_layout():
            regrid_frame(self)