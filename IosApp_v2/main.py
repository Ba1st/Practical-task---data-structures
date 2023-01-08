import kivy
kivy.require("2.1.0")

from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.pickers import MDDatePicker
from kivy.properties import DictProperty
from kivy.core.window import Window

##Print Bills##
class PrintBillsScreen(MDScreen):
    def ChangeScreen(self, ScreenName):
        self.manager.current = ScreenName

##Amount Sold##
class AmountSoldScreen(MDScreen):
    def ChangeScreen(self, ScreenName):
        self.manager.current = ScreenName

##Calendar##
class CalendarScreen(MDScreen):
    
    def DatePicker(self):
        self.dateD = MDDatePicker()
        self.dateD.open()
        
    def ChangeScreen(self, ScreenName):
        self.manager.current = ScreenName

##Store Location##
class StoreLocationScreen(MDScreen):
    def ChangeScreen(self, ScreenName):
        self.manager.current = ScreenName

##Mail##
class MailScreen(MDScreen):
    def ChangeScreen(self, ScreenName):
        self.manager.current = ScreenName

##Phonebook##
class PhonebookScreen(MDScreen):
    def ChangeScreen(self, ScreenName):
        self.manager.current = ScreenName

##News##
class NewsScreen(MDScreen):
    def ChangeScreen(self, ScreenName):
        self.manager.current = ScreenName

##Settings##
class SettingsScreen(MDScreen):
    def ChangeScreen(self, ScreenName):
        self.manager.current = ScreenName

class MainScreen(MDScreen):
    
    def ChangeScreen(self, ScreenName):
        self.manager.current = ScreenName
                  
class PerfectStoreApp(MDApp):

    data = DictProperty()
    Window.size = (375, 812)

    def build(self):
        sm = MDScreenManager()
        
        self.data = {
            'Store Location': [
                'map-marker-outline',
                'on_press', lambda x: callback('SL')
            ],
            'Mail':[
                'email-outline',
                'on_press', lambda x: callback('M')
            ],
            'Phonebook':[
                'book-account',
                'on_press', lambda x: callback('P')
            ],
            'News':[
                'newspaper',
                'on_press', lambda x: callback('N')
            ],
            'Settings':[
                'cog-outline',
                'on_press', lambda x: callback('S')
            ]
        }
        
        sm.add_widget(MainScreen(name = 'main'))
        sm.add_widget(PrintBillsScreen(name = 'bill'))
        sm.add_widget(AmountSoldScreen(name = 'amount'))
        sm.add_widget(CalendarScreen(name = 'calendar'))
        sm.add_widget(StoreLocationScreen(name = 'SL'))
        sm.add_widget(MailScreen(name = 'M'))
        sm.add_widget(PhonebookScreen(name = 'P'))
        sm.add_widget(NewsScreen(name = 'N'))
        sm.add_widget(SettingsScreen(name = 'S'))
        
        def callback(instance):
            sm.get_screen('main').ids.speedDial.close_stack()
            sm.current = instance
        
        return sm
    
    def on_start(self):
        self.fps_monitor_start()
    
if __name__ == '__main__':
    PerfectStoreApp().run()
        