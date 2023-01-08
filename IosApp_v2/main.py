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
        
        artikli = ["Artikl: Kruh \nCijena: 8.00 kn \nKolicina: 20",
                   "Artikl: Sladoled \nCijena: 20.00 kn \nKolicina: 30",
                   "Artikl: Jaja \nCijena: 13.00 kn \nKolicina: 21",
                   "Artikl: Majoneza \nCijena: 16.00 kn \nKolicina: 32",
                   "Artikl: Jabuke \nCijena: 6.00 kn \nKolicina: 60",
                   "Artikl: Nutella \nCijena: 22.00 kn \nKolicina: 30",
                   "Artikl: Meso \nCijena: 40.00 kn \nKolicina: 18",
                   "Artikl: Jogurt \nCijena: 20.00 kn \nKolicina: 15"]
        
        if string == "Kruh":
            self.manager.get_screen('second').ids.lb1.text = artikli[0]
            
        elif string == "Sladoled":
            self.manager.get_screen('second').ids.lb1.text = artikli[1]
            
        elif string == "Jaja":
            self.manager.get_screen('second').ids.lb1.text = artikli[2]
            
        elif string == "Majoneza":
            self.manager.get_screen('second').ids.lb1.text = artikli[3]
            
        elif string == "Jabuke":
            self.manager.get_screen('second').ids.lb1.text = artikli[4]
            
        elif string == "Nutella":
            self.manager.get_screen('second').ids.lb1.text = artikli[5]
            
        elif string == "Meso":
            self.manager.get_screen('second').ids.lb1.text = artikli[6]
            
        elif string == "Jogurt":
            self.manager.get_screen('second').ids.lb1.text = artikli[7]
            
        self.manager.current = 'second'

class mainApp(App):
    def build(self):
        sm = ScreenManagment(transition = SlideTransition())
        sm.add_widget(MainScreen(name = 'main'))
        sm.add_widget(SecondScreen(name = 'second'))
        return sm

if __name__ == '__main__':
    mainApp().run()
