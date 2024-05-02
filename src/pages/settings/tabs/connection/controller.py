from .view import ConnectionView




class ConnectionController(ConnectionView):
    def __init__(self, master):
        super().__init__(master)
        self.setup_event_handler()


    # init
    def setup_event_handler(self):
        self.show_pass_ck_btn.configure(command=self.on_show_pass_ck_btn_pressed)
    

    # event handler
    def on_show_pass_ck_btn_pressed(self):
        if self.show_pass_v.get():
            self.password_entry.configure(show="")
        else:
            self.password_entry.configure(show="*")
    

    # logic
    def save_data(self, data):
        data["connection"] = {
            "ip" : self.ip_v.get(),
            "user" : self.user_v.get(),
            "password" : self.password_v.get(),
            "keep_conn" : self.keep_conn_v.get()
        }
        

    def load_data(self, data):        
        data = data.get("connection")

        self.ip_v.set(data.get("ip"))
        self.user_v.set(data.get("user"))
        self.password_v.set(data.get("password"))
        self.keep_conn_v.set(data.get("keep_conn"))