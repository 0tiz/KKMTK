import kivy
from kivy.app import App
from kivy.uix.widget import Widget


class Login(Widget):
    pass

class StartApp(App):
        def build(self):
                return Login()

if __name__ == "__main__":
    StartApp().run()