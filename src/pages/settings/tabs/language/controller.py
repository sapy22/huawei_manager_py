from .view import LanguageView




class LanguageController(LanguageView):
    def __init__(self, master):
        super().__init__(master)
        self.setup_event_handler()


    # init
    def setup_event_handler(self):
        self.en_rd_btn.configure(command=self.on_lang_rd_btn_pressed)
        self.ar_rd_btn.configure(command=self.on_lang_rd_btn_pressed)


    # event handler
    def on_lang_rd_btn_pressed(self):
        if self.lang_v.get() == "en":
            self.dir_v.set("ltr")
        else:
            self.dir_v.set("rtl")


    # logic
    def save_data(self, data):
        data["language"] = {
            "language" : self.lang_v.get(),
            "direction" : self.dir_v.get()
        }
        

    def load_data(self, data):
        data = data.get("language")

        self.lang_v.set(data.get("language"))
        self.dir_v.set(data.get("direction"))