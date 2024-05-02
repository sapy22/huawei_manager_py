from .view import SMSView
from .utils import content_preview
from .task import SMSTask

from src.shared.localize import lc_is_rtl_layout, regrid_frame
from src.shared.utils import show_message, center_window_on_master
from src.shared.widgets import Notification




class SMSController(SMSView):
    def __init__(self, master, settings_data):
        super().__init__(master)
        self.sms_task = SMSTask(settings_data.get("connection"))

        self.setup_vars()
        self.setup_event_handler()
        
        self.check_locale()

        self.get_all_sms()


    # init
    def setup_vars(self):
        self.all_sms_dict = dict()

    
    def setup_event_handler(self):
        self.inbox_rd_btn.configure(command=self.on_box_type_rd_btn_pressed)
        self.outbox_rd_btn.configure(command=self.on_box_type_rd_btn_pressed)
        self.tree.bind("<Double-1>", self.on_tree_double_click)
        self.msg_text.bind("<KeyRelease>", self.on_msg_text_key_release)
        self.send_btn.configure(command=self.on_send_btn_pressed)


    # event handler
    def on_box_type_rd_btn_pressed(self):
        self.tree.delete(*self.tree.get_children())
        self.get_all_sms()

    
    def on_tree_double_click(self,event):
        item = self.tree.identify_row(event.y)
        
        if not item:
                return

        i = 0
        if lc_is_rtl_layout():
            i = 2
            
        phone = self.tree.item(item, "values")[i]
        msg_list = self.all_sms_dict[phone]
    
        self.setup_content_window(msg_list, phone)


    def on_msg_text_key_release(self, event):
        msg_lenght = len(self.msg_text.get("1.0","end-1c"))

        if msg_lenght <= 160:
            self.msg_lenght_lbl.configure(text=f"{160-msg_lenght}")
            return

        i = self.msg_text.index("1.0+160c")
        self.msg_text.delete(i,"end")


    def on_send_btn_pressed(self):
        if not show_message(3, _("Send SMS. Continue?"),self):
            return

        num = self.number_v.get()
        msg = self.msg_text.get("1.0","end-1c")

        if (not num ) or (not msg):
            show_message(0, _("The Number\\s or Message is empty!"))
            return

        if len(msg) > 160:
            show_message(0, _("Message length cannot exceed 160 characters!"))
            return
        
        self.send_btn.configure(state="disabled")

        self.send_sms(num,msg)


    # logic
    def get_all_sms(self):
        Notification(text="Connecting!")
        
        box_type = self.box_type_v.get()

        # task
        self.sms_task.get_all_sms(box_type)

        self.update_ui()
    

    def update_ui(self):
        if self.sms_task.error:
            show_message(0, self.sms_task.error, self)
            self.sms_task.error = ""
            return

        if not self.sms_task.data_ready:
            self.after(10, self.update_ui)
            return

        self.sms_task.data_ready = False

        self._load_data(self.sms_task.sms_data)
        self._update_ui()


    def _load_data(self, data):
        self.all_sms_dict.clear()
        for obj in data:
            if not obj.phone in self.all_sms_dict:
                self.all_sms_dict[obj.phone] = []
            self.all_sms_dict[obj.phone].append((obj.content, obj.date_time))
    

    def _update_ui(self):
        for phone in self.all_sms_dict.keys():
            msg = self.all_sms_dict[phone][0]
            content = content_preview(msg[0])
            date = msg[1].date()
            
            v = (phone, content, date)
            if lc_is_rtl_layout():
                v = tuple(reversed(v))

            self.tree.insert("", "end", values=v)


    def send_sms(self, num, msg):
        nums = num.split(";")

        # task
        self.sms_task.send_sms(nums, msg)

        self._show_send_sms_response()


    def _show_send_sms_response(self):
        if self.sms_task.error:
            show_message(0, self.sms_task.error, self)
            self.sms_task.error = ""
            self.send_btn.configure(state="normal")
            return

        if not self.sms_task.send_sms_response:
            self.after(100, self._show_send_sms_response)
            return

        show_message(2, self.sms_task.send_sms_response)
        self.sms_task.send_sms_response = ""

        self.send_btn.configure(state="normal")
        

    def check_locale(self):
        if lc_is_rtl_layout():
            regrid_frame(self)