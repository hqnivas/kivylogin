from kivymd.app import MDApp

class LoginApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Indigo"
        return

LoginApp().run()

