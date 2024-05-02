from .view import GetView

from .task import GetTask

from src.shared.localize import lc_is_rtl_layout, regrid_frame
from src.shared.utils import show_message, center_window_on_master ,disable_children_widgets ,enable_children_widgets
from src.shared.widgets import Notification




class GetController(GetView):
    def __init__(self, master, settings_data):
        super().__init__(master)
        self.get_task = GetTask(settings_data.get("connection"))

        self.setup_event_handler()


    # init
    def setup_event_handler(self):
        self.signal_btn.configure(command=lambda:self.on_btn_pressed("signal"))
        self.information_btn.configure(command=lambda:self.on_btn_pressed("information"))
        self.plmn_btn.configure(command=lambda:self.on_btn_pressed("plmn"))
        self.plmn_list_btn.configure(command=lambda:self.on_btn_pressed("plmn_list"))
        self.net_mode_btn.configure(command=lambda:self.on_btn_pressed("net_mode"))
        self.net_mode_list_btn.configure(command=lambda:self.on_btn_pressed("net_mode_list"))
        self.status_btn.configure(command=lambda:self.on_btn_pressed("status"))
        self.settings_btn.configure(command=lambda:self.on_btn_pressed("settings"))

        self.tree.bind("<Double-1>", self.on_tree_double_click)


    # event handler
    def on_btn_pressed(self, btn_name):
        if btn_name == "plmn_list":
            if not show_message(3,_("Internet connection will reset. Continue?")):
                return
                
        disable_children_widgets(self.side_bar)

        Notification(text="Connecting!")

        self.get_task.get_data(btn_name)

        self.clear_tree()

        self.update_ui()
    

    def on_tree_double_click(self,event):
        item = self.tree.identify_row(event.y)
        
        if not item:
            return
        
        col = self.tree.identify_column(event.x)

        self.setup_content_window(self.tree.set(item,col))


    # logic
    def clear_tree(self):
        self.tree.delete(*self.tree.get_children())
    

    def update_ui(self):
        if self.get_task.error:
            show_message(0, self.get_task.error, self)
            self.get_task.error = ""
            enable_children_widgets(self.side_bar)
            return

        if not self.get_task.data_ready:
            self.after(10, self.update_ui)
            return

        self.get_task.data_ready = False

        self._update_ui(self.get_task.data)

        enable_children_widgets(self.side_bar)
    

    def _update_ui(self, data):
        for item in data.items():
            v = (item[0], str(item[1]))

            if lc_is_rtl_layout():
                v = tuple(reversed(v))

            self.tree.insert("", "end", values=v)