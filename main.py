if __name__ == "__main__":
    import builtins
    from src.main.controller import MainController

    builtins._ = lambda text: text
    app = MainController()
    app.mainloop()