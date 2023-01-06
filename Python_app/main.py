from kivy.app import App
from kivy.uix.widget import Widget


class MyLayout(Widget):
    pass


class TheMobApp(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    TheMobApp().run()
