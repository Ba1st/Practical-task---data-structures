import kivy
kivy.require("2.1.0")

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.pickers import MDDatePicker
from kivy.properties import DictProperty
from kivy.core.window import Window
from kivy_garden.mapview import MapView

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
        self.dateD = MDDatePicker(title_input = "INPUT DATE" ,mode = "range")
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
        
    def ChangeLanguage(self, lang):
        
        cro = ["Nazad", "Otvori Kalendar", "JEZIK", "Isprintaj Racune", "Prodano", "Kalendar", "TEME", "MRAČNO", "SVJETLO", 
                "Bok", "Nadamo se da ste imali dobar dan", "Novosti"]    
        eng = ["Back", "Open Calendar", "LANGUAGE", "Print Bills", "Amount Sold", "Calendar", "THEME", "DARK", "LIGHT", 
                "Hello", "We are hoping that you have a great day", "News"]
        screens = ['bill', 'amount', 'calendar', 'SL', 'M', 'P', 'N', 'S']
    
        if lang == "CRO":
            for a in screens:
                self.manager.get_screen(str(a)).ids.BackButton.text = '[b]' + cro[0] + '[/b]'
            
            self.manager.get_screen(str(screens[7])).ids.ThemeLabel.text = cro[6]
            self.manager.get_screen(str(screens[7])).ids.DarkButton.text = '[b]' + cro[7] + '[/b]'
            self.manager.get_screen(str(screens[7])).ids.LightButton.text = '[b]' + cro[8] + '[/b]'
            self.manager.get_screen(str(screens[7])).ids.LanguageLabel.text = cro[2]
            self.manager.get_screen(str(screens[2])).ids.OpenCalendar.text = '[b]' + cro[1] + '[/b]'
            self.manager.get_screen('main').ids.PrintBills.text = '[b]' + cro[3] + '[/b]'
            self.manager.get_screen('main').ids.AmountSold.text = '[b]' + cro[4] + '[/b]'
            self.manager.get_screen('main').ids.Calendar.text = '[b]' + cro[5] + '[/b]'
            
        elif lang == "ENG":
            for a in screens:
                self.manager.get_screen(str(a)).ids.BackButton.text = '[b]' + eng[0] + '[/b]'
                
            self.manager.get_screen(str(screens[7])).ids.ThemeLabel.text = eng[6]
            self.manager.get_screen(str(screens[7])).ids.DarkButton.text = '[b]' + eng[7] + '[/b]'
            self.manager.get_screen(str(screens[7])).ids.LightButton.text = '[b]' + eng[8] + '[/b]'
            self.manager.get_screen(str(screens[7])).ids.LanguageLabel.text = eng[2]
            self.manager.get_screen(str(screens[2])).ids.OpenCalendar.text = '[b]' + eng[1] + '[/b]'
            self.manager.get_screen('main').ids.PrintBills.text = '[b]' + eng[3] + '[/b]'
            self.manager.get_screen('main').ids.AmountSold.text = '[b]' + eng[4] + '[/b]'
            self.manager.get_screen('main').ids.Calendar.text = '[b]' + eng[5] + '[/b]'
            
    def ChangeText(self, theme):
            if theme == "DARK":
                self.manager.get_screen('S').ids.LanguageLabel.text_color = 'white'
                self.manager.get_screen('S').ids.ThemeLabel.text_color = 'white'
                self.manager.get_screen('main').ids.mainTitle.text = '[b][color=FFFFFF][size=90]P[/size][size=85]erfect[/size][/color][i][color=4073FF][size=90]S[/size]tore[/color][/i][/b]'
                self.manager.get_screen('main').ids.speedDial.label_text_color = 'white'

            elif theme == "LIGHT":
                self.manager.get_screen('S').ids.LanguageLabel.text_color = 'black'
                self.manager.get_screen('S').ids.ThemeLabel.text_color = 'black'
                self.manager.get_screen('main').ids.mainTitle.text = '[b][color=000000][size=90]P[/size][size=85]erfect[/size][/color][i][color=4073FF][size=90]S[/size]tore[/color][/i][/b]'
                self.manager.get_screen('main').ids.speedDial.label_text_color = 'black'

class MainScreen(MDScreen):
    
    def ChangeScreen(self, ScreenName):
        self.manager.current = ScreenName
                  
class PerfectStoreApp(MDApp):

    data = DictProperty()

    def build(self):
        sm = ScreenManager()
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        
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
    
    def ChangeTheme(self, theme):
            if theme == "DARK":
                self.theme_cls.theme_style = "Dark"
                self.theme_cls.primary_palette = "Blue"

            elif theme == "LIGHT":
                self.theme_cls.theme_style = "Light"
                self.theme_cls.primary_palette = "Blue"
    
if __name__ == '__main__':
    PerfectStoreApp().run()