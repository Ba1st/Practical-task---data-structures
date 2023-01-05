import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition

class ScreenManagment(ScreenManager):
    
    def __init__(self, **kwargs):
        super(ScreenManagment, self).__init__(**kwargs)

class SecondScreen(Screen):
    
    def __init__(self, **kwargs):
        super(SecondScreen, self).__init__(**kwargs)
    
    def main_screen(self):
        self.manager.current = 'main'

class MainScreen(Screen):
    
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
                    
    def changeScreen(self, string):
        self.manager.get_screen('second').ids.lb1.text = string
        self.manager.current = 'second'
        

class mainApp(App):
    def build(self):
        sm = ScreenManagment(transition = SlideTransition())
        sm.add_widget(MainScreen(name = 'main'))
        sm.add_widget(SecondScreen(name = 'second'))
        
        return sm

if __name__ == '__main__':
    mainApp().run()
