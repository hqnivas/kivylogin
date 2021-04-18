from kivymd.app import MDApp
from kivy.core.window import Window

class LoginApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Indigo"
        return

Window.fullscreen = True
LoginApp().run()

