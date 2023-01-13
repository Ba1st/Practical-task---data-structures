import kivy
kivy.require("2.1.0")

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from kivymd.uix.screen import MDScreen
from kivymd.uix.pickers import MDDatePicker
from kivy.properties import DictProperty
from kivy.core.window import Window
from kivy_garden.mapview import MapView
from kivymd.uix.list import TwoLineIconListItem, IconLeftWidget
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.floatlayout import MDFloatLayout

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
    
    card = None
    texField_1 = None
    textField_2 = None
    deleteCard = None
    
    def ChangeScreen(self, ScreenName):
        self.manager.current = ScreenName    
        
    def add_card(self):
        
        self.texField_1 = MDTextField(
            hint_text = "Name",
            font_size = 25,
            size_hint_x = .8,
            pos_hint = {'center_x': .5,'center_y': .8}
        )
        
        self.textField_2 = MDTextField(
            hint_text = "Number",
            font_size = 25,
            size_hint_x = .8,
            pos_hint = {'center_x': .5,'center_y': .4}
        )
        
        self.card = MDCard(
            MDFloatLayout(
                self.texField_1,
                self.textField_2,
                MDFlatButton(
                    text = "OK",
                    size_hint = (.2, .2),
                    pos_hint = {'center_x': 0.85,'center_y': 0.15},
                    on_release = self.AddPerson
                ),
                MDFlatButton(
                    text = "CANCEL",
                    size_hint = (.2, .2),
                    pos_hint = {'center_x': 0.6,'center_y': 0.15},
                    on_release = self.Cancel
                ),
                size = self.size
            ),
            orientation = 'vertical',
            line_color = (0.2,0.2,0.2,0.8),
            size_hint = (.7, .2),
            pos_hint = {'center_x': 0.5,'center_y': 0.5},
            elevation = 4,
            radius = [20]
        )
        self.add_widget(self.card)
            
    def AddPerson(self, obj):
        
        name = []
        number = []
        
        name.append(self.texField_1.text)
        number.append(self.textField_2.text)
        
        self.manager.get_screen('P').ids.PhoneBookNumbers.add_widget(
            TwoLineIconListItem(
                IconLeftWidget(
                    icon="account"
                ),
                text = str(*name),
                secondary_text = "Number: " + str(*number),
                on_release = self.PressedItem
                )
        )
        
        self.remove_widget(self.card)
    
    def Cancel(self, obj):
        self.remove_widget(self.card)
        
    def PressedItem(self, obj):
        self.deleteCard = obj
        
    def deleteItem(self):
        if self.deleteCard:
            self.manager.get_screen('P').ids.PhoneBookNumbers.remove_widget(self.deleteCard)
            self.deleteCard = None
             
##News##
class NewsScreen(MDScreen):
    def ChangeScreen(self, ScreenName):
        self.manager.current = ScreenName

##Settings##
class SettingsScreen(MDScreen):
    def ChangeScreen(self, ScreenName):
        self.manager.current = ScreenName
            
    def ChangeText(self, theme):
            if theme == "DARK":
                self.manager.get_screen('S').ids.ThemeLabel.text = '[b][color=FFFFFF]THEME[/color][/b]'
                self.manager.get_screen('main').ids.mainTitle.text = '[b][color=FFFFFF][size=90]P[/size][size=85]erfect[/size][/color][i][color=4073FF][size=90]S[/size]tore[/color][/i][/b]'
                self.manager.get_screen('main').ids.HelloText.text = '[b][color=FFFFFF]Hello\nWe are hoping that you have a great day[/color][/b]'
                
            elif theme == "LIGHT":
                self.manager.get_screen('S').ids.ThemeLabel.text = '[b][color=000000]THEME[/color][/b]'
                self.manager.get_screen('main').ids.mainTitle.text = '[b][color=000000][size=90]P[/size][size=85]erfect[/size][/color][i][color=4073FF][size=90]S[/size]tore[/color][/i][/b]'
                self.manager.get_screen('main').ids.HelloText.text = '[b][color=000000]Hello\nWe are hoping that you have a great day[/color][/b]'

class MainScreen(MDScreen):
    
    def ChangeScreen(self, ScreenName):
        self.manager.current = ScreenName
                  
class PerfectStoreApp(MDApp):

    data = DictProperty()
    card = None
    Window.size = (375, 812)

    def build(self):
        sm = ScreenManager(transition = FadeTransition())
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
            'Settings':[
                'cog-outline',
                'on_press', lambda x: callback('S')
            ]
        }
        
        sm.add_widget(MainScreen(name = 'main'))
        sm.add_widget(StoreLocationScreen(name = 'SL'))
        sm.add_widget(MailScreen(name = 'M'))
        sm.add_widget(PhonebookScreen(name = 'P'))
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
                
    def DatePicker(self):
        self.dateD = MDDatePicker(title_input = "INPUT DATE" ,mode = "range")
        self.dateD.open()
    
if __name__ == '__main__':
    PerfectStoreApp().run()