import kivy
kivy.require("2.1.0")

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivymd.uix.screen import MDScreen
from kivy.properties import DictProperty
from kivy.core.window import Window
from kivy_garden.mapview import MapView
from kivymd.uix.list import TwoLineIconListItem, IconLeftWidget
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDFlatButton, MDFloatingActionButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.textinput import TextInput
from kivymd.uix.swiper import MDSwiper, MDSwiperItem
from kivymd.uix.label import MDLabel
import os

##Store Location##
class StoreLocationScreen(MDScreen):
    pass

##Mail##
class MailScreen(MDScreen):
    pass

##Phonebook##
class PhonebookScreen(MDScreen):
    
    card = None
    textField_1 = None
    textField_2 = None
        
    def add_card(self):
        
        self.textField_1 = MDTextField(
            hint_text = "Name",
            font_size = 25,
            size_hint_x = .8,
            pos_hint = {'center_x': .5,'center_y': .8},
        )
        
        self.textField_2 = MDTextField(
            hint_text = "Number",
            font_size = 25,
            size_hint_x = .8,
            pos_hint = {'center_x': .5,'center_y': .5},
        )
        
        self.card = MDCard(
            MDFloatLayout(
                self.textField_1,
                self.textField_2,
                MDFlatButton(
                    text = "OK",
                    size_hint = (.2, .2),
                    pos_hint = {'center_x': 0.85,'center_y': 0.15},
                    on_release = self.AddPerson,
                ),
                MDFlatButton(
                    text = "CANCEL",
                    size_hint = (.2, .2),
                    pos_hint = {'center_x': 0.6,'center_y': 0.15},
                    on_release = self.Cancel,
                ),
                size = self.size
            ),
            orientation = 'vertical',
            size_hint = (.7, .2),
            pos_hint = {'center_x': 0.5,'center_y': 0.5},
            elevation = 4,
            radius = [20],
        )
        self.add_widget(self.card)
            
    def AddPerson(self, obj):
        
        name = str(self.textField_1.text)
        number = str(self.textField_2.text)

        with open('phonebook.txt','a') as file:
            file.write(f'{self.textField_1.text} {self.textField_2.text}\n')
        
        self.manager.get_screen('P').ids.PhoneBookNumbers.add_widget(
            TwoLineIconListItem(
                IconLeftWidget(
                    icon="account"
                ),
                text = str(name) + ' ',
                secondary_text = "Number: " + str(number),
                on_release = self.PressedItem,
                bg_color = (1,1,1,1),
                radius = [25]
                )
        )
        
        self.remove_widget(self.card)
    
    def Cancel(self, obj):
        self.remove_widget(self.card)
            
    def PressedItem(self, obj):
        if PerfectStoreApp.delPerson:
            PerfectStoreApp.delPerson.bg_color = (1,1,1,1)
            if PerfectStoreApp.delPerson != obj:
                PerfectStoreApp.delPerson = obj
                PerfectStoreApp.delPerson.bg_color = "#00B4D8"
            else:
                PerfectStoreApp.delPerson = None
        else:
            PerfectStoreApp.delPerson = obj
            PerfectStoreApp.delPerson.bg_color = "#00B4D8"
            
    def deleteItem(self):

        if PerfectStoreApp.delPerson:
            person = str(PerfectStoreApp.delPerson.text) + str(PerfectStoreApp.delPerson.secondary_text.replace('Number: ', ''))
            with open('phonebook.txt', 'r') as file:
                    with open('temp.txt','a+') as temp:
                        for line in file:
                            if not line.strip('\n').startswith(f'{person}'):
                                temp.write(line)
            os.replace('temp.txt', 'phonebook.txt')
            
            self.manager.get_screen('P').ids.PhoneBookNumbers.remove_widget(PerfectStoreApp.delPerson)
            PerfectStoreApp.delPerson = None

##Settings##
class SettingsScreen(MDScreen):
            
    def ChangeText(self, theme):
            if theme == "DARK":
                self.manager.get_screen('S').ids.ThemeLabel.text = '[b][color=FFFFFF]THEME[/color][/b]'
                self.manager.get_screen('main').ids.mainTitle.text = '[b][color=FFFFFF][size=90]P[/size][size=85]erfect[/size][/color][i][color=4073FF][size=90]S[/size]tore[/color][/i][/b]'
                self.manager.get_screen('main').ids.HelloText.text = '[b][color=FFFFFF]Hello\nWe are hoping that you have a great day[/color][/b]'
                self.manager.get_screen('main').ids.tasksLabel.text = '[b][color=FFFFFF]My Tasks:[/color][/b]'
                
            elif theme == "LIGHT":
                self.manager.get_screen('S').ids.ThemeLabel.text = '[b][color=000000]THEME[/color][/b]'
                self.manager.get_screen('main').ids.mainTitle.text = '[b][color=000000][size=90]P[/size][size=85]erfect[/size][/color][i][color=4073FF][size=90]S[/size]tore[/color][/i][/b]'
                self.manager.get_screen('main').ids.HelloText.text = '[b][color=000000]Hello\nWe are hoping that you have a great day[/color][/b]'
                self.manager.get_screen('main').ids.tasksLabel.text = '[b][color=000000]My Tasks:[/color][/b]'

class MainScreen(MDScreen):
    def ChangeScreen(self, ScreenName):
        self.manager.current = ScreenName
                  
class PerfectStoreApp(MDApp):

    #class objects
    obj_p = PhonebookScreen()
    delPerson = None
    
    #Screen properties
    Window.size = (375, 812)
    sm = ScreenManager(transition = SlideTransition())
    
    #SpeedDial data
    data = DictProperty()
    
    #Storing bill data
    string = ""
    Bill = []
    BillPaths = []
    menuForDisplaying = None
    menuForDeleting = None
    
    #Data for creating a bill
    card = None
    textField_1 = None
    textField_2 = None
    textInput_3 = None
    deleteCard = None
    
    #Amount sold screen data
    totalProfit = 0
    ListOfItems = []
    menuForItems = None
    InStorage = 1000
    
    #Tasks Screen
    textField_1_task = None
    textInput_2_task = None
    card_task = None
    TaskItem = None
    listOfTasks = []
    listOfButtons = []
    checkbutton = None
    deleteButton = None
    

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        
        self.data = {
            'Store Location': [
                'map-marker-outline',
                'on_release', lambda x: callback('SL')
            ],
            'Mail':[
                'email-outline',
                'on_release', lambda x: callback('M')
            ],
            'Phonebook':[
                'book-account',
                'on_release', lambda x: callback('P')
            ],
            'Settings':[
                'cog-outline',
                'on_release', lambda x: callback('S')
            ]
        }
        
        self.sm.add_widget(MainScreen(name = 'main'))
        self.sm.add_widget(StoreLocationScreen(name = 'SL'))
        self.sm.add_widget(MailScreen(name = 'M'))
        self.sm.add_widget(PhonebookScreen(name = 'P'))
        self.sm.add_widget(SettingsScreen(name = 'S'))
        
        def callback(instance):
            self.sm.get_screen('main').ids.speedDial.close_stack()
            self.sm.current = instance
            
        return self.sm
    
    def DropDownMenuForDisplaying(self):
        bill_items = [
            {
                "text": str(i['Name']),
                "viewclass": "OneLineListItem",
                "on_release": lambda x=str(i['Name']): self.LoadBills(x),
            }for i in self.Bill
        ]
        
        self.menuForDisplaying = MDDropdownMenu(
            caller = self.sm.get_screen('main').ids.SelectItem,
            items = bill_items,
            width_mult = 2,
            max_height = 300,
        )
        
        self.menuForDisplaying.open()
    
    def DropDownMenuForDeleting(self):
        bill_items = [
            {
                "text": str(i['Name']),
                "viewclass": "OneLineListItem",
                "on_release": lambda x=str(i['Name']): self.DeleteBills(x),
            }for i in self.Bill
        ]
        
        self.menuForDeleting = MDDropdownMenu(
            caller = self.sm.get_screen('main').ids.DeleteItem,
            items = bill_items,
            width_mult = 2,
            max_height = 300,
        )
        
        self.menuForDeleting.open()
    
    def ChangeTheme(self, theme):
            if theme == "DARK":
                self.theme_cls.theme_style = "Dark"
                self.theme_cls.primary_palette = "Blue"

            elif theme == "LIGHT":
                self.theme_cls.theme_style = "Light"
                self.theme_cls.primary_palette = "Blue"
        
    def CreateBillPopUp(self):
        
        self.textField_1 = MDTextField(
            hint_text = "Bill Name:",
            font_size = 25,
            size_hint_x = .8,
            pos_hint = {'center_x': .5,'center_y': .85},
        )
        
        self.textField_2 = MDTextField(
            hint_text = "Date:",
            font_size = 25,
            size_hint_x = .8,
            pos_hint = {'center_x': .5,'center_y': .7},
        )
        
        self.textInput_3 = TextInput(
            hint_text = "Items",
            font_size = 30,
            size_hint = (.8, .5),
            pos_hint = {'center_x': .5,'center_y': .35},
            multiline = True,
            background_color = (0,0,0,0),
        )
        
        self.card = MDCard(
            MDFloatLayout(
                self.textField_1,
                self.textField_2,
                self.textInput_3,
                MDFlatButton(
                    text = "OK",
                    size_hint = (.2, .2),
                    pos_hint = {'center_x': 0.85,'center_y': 0.15},
                    on_release = self.AddBill,
                ),
                MDFlatButton(
                    text = "CANCEL",
                    size_hint = (.2, .2),
                    pos_hint = {'center_x': 0.6,'center_y': 0.15},
                    on_release = self.Cancel,
                )
            ),
            orientation = 'vertical',
            size_hint = (.8, .3),
            pos_hint = {'center_x': 0.5,'center_y': 0.5},
            elevation = 4,
            radius = [20],
        )
        self.sm.get_screen('main').add_widget(self.card)
    
    def AddBill(self, obj):
        items = []
        string_list = []
        string = ""
        dic = {'Name' : "", 'Date' : "", 'Items' : []}
        
        dic['Name'] = str(self.textField_1.text)
        dic['Date'] = str(self.textField_2.text + "\n")
        
        filepath = f"Racuni/{self.textField_1.text}.txt"
        self.BillPaths.append(filepath)
        
        with open(filepath, "a") as BillFile:
            BillFile.write(f"{str(self.textField_2.text)}\n")
            BillFile.write(str(self.textInput_3.text))
        
        with open('racuni.txt', 'r') as file:
            with open('temp.txt', 'w') as copy:
                for line in file:
                    copy.write(line)
                copy.write(filepath + "\n")
        
        os.replace('temp.txt', 'racuni.txt')
        for i in self.textInput_3.text.splitlines():
            items.append(str(i)+"\n")
        
        dic['Items'] = items
        self.Bill.append(dic)
        
        for x in items:
            for y in x:
                if y != ' ' and y != '\n':
                    string += y
                else:
                    string_list.append(string)
                    string = ""

        self.TotalAmount(string_list)
        
        self.totalProfit = round(self.totalProfit,2)
        self.sm.get_screen('main').ids.TotalProfit.text = f"TOTAL PROFIT: {self.totalProfit}$"
        
        self.sm.get_screen('main').remove_widget(self.card)
        
    def LoadBills(self, item):
        if item == "None":
            for i in self.Bill:
                self.string += f"{str(i['Name'])}\n{str(i['Date'])}{' '.join(i['Items'])}\n"
            self.sm.get_screen('main').ids.BillContent.text = f'[b]{self.string}[/b]'
            self.string = ""
        else:
            self.menuForDisplaying.dismiss()
            for i in self.Bill:
                if i['Name'] == item:
                    self.string = f"{str(i['Name'])}\n{str(i['Date'])}{' '.join(i['Items'])}\n"
                    self.sm.get_screen('main').ids.BillContent.text = f'[b]{self.string}[/b]'
            self.string = ""
            
    def DeleteBills(self, item):
        
        a = 0
        minus = 0
        string_list = []
        string = ""
        for i in self.Bill:
            if i['Name'] == item:
                self.Bill.remove(i)
                
                for x in i['Items']:
                    for x in i['Items']:
                        for y in x:
                            if y != ' ' and y != '\n':
                                string += y
                            else:
                                string_list.append(string)
                                string = ""

                minus = int(string_list[1]) * float(string_list[2])
                
                os.remove(str(self.BillPaths[a]))
                with open('/Users/pierstrbad/Desktop/Programi/Python/Kivy/NewApp/racuni.txt', 'r') as file:
                    with open('temp.txt','w') as temp:
                        for line in file:
                            if not line.strip("\n").startswith(str(self.BillPaths[a])):
                                temp.write(line)
                                
                self.BillPaths.remove(self.BillPaths[a])
                break
            a+=1
        os.replace('temp.txt', '/Users/pierstrbad/Desktop/Programi/Python/Kivy/NewApp/racuni.txt')
        self.sm.get_screen('main').ids.TotalProfit.text = f"TOTAL PROFIT: {str(self.totalProfit-round(minus,2))}$"
        self.menuForDeleting.dismiss()
    
    def Cancel(self, obj):
        if self.card:
            self.sm.get_screen('main').remove_widget(self.card)
            self.card = None
        
        if self.card_task:
            self.sm.get_screen('main').remove_widget(self.card_task)
            self.card_task = None
              
    def DisplayItem(self):
        items_ = [
            {
                "text": str(i),
                "viewclass": "OneLineListItem",
                "on_release": lambda x=str(i): self.ShowItem(x),
            }for i in self.ListOfItems
        ]
        self.menuForItems = MDDropdownMenu(
            caller = self.sm.get_screen('main').ids.SelectItem,
            items = items_,
            width_mult = 2,
            border_margin = 24,
            max_height = 350,
            ver_growth = "down",
        )

        self.menuForItems.open()
            
    def ShowItem(self, instance):
        
        total_amount = 0
        string_list = []
        string = ""
        price = ""
        
        for i in self.Bill:
            for x in i['Items']:
                for y in x:
                    if y != ' ' and y != '\n':
                        string += y
                    else:
                        string_list.append(string)
                        string = ""
                        
        for i in range(len(string_list)):
            if string_list[i] == instance:
                total_amount += int(string_list[i+1])
                price = string_list[i+2]
        
        self.sm.get_screen('main').ids.item.text = f"Item: {instance}"
        self.sm.get_screen('main').ids.amount.text = f"Amount Sold: {str(total_amount)}"
        self.sm.get_screen('main').ids.price.text = f"Price: {str(price)}$"
        self.sm.get_screen('main').ids.storage.text = f"In Storage: {str(self.InStorage - total_amount)}"
        self.menuForItems.dismiss()
    
    def AddSwiperItem(self):
        
        self.textField_1_task = MDTextField(
            hint_text = "Task Name",
            font_size = 25,
            size_hint_x = .8,
            pos_hint = {'center_x': .5,'center_y': .85},
        )
        
        self.textInput_2_task = TextInput(
            hint_text = "Description\nMaximum number of characters is 60",
            font_size = 35,
            hint_text_color = (0, 153/250, 1, 135/250),
            size_hint = (.8, .5),
            pos_hint = {'center_x': .5,'center_y': .5},
            multiline = True,
            background_color = (0,0,0,0),
        )
        
        self.card_task = MDCard(
            MDFloatLayout(
                self.textField_1_task,
                self.textInput_2_task,
                MDFlatButton(
                    text = "OK",
                    size_hint = (.2, .2),
                    pos_hint = {'center_x': 0.85,'center_y': 0.15},
                    on_release = self.addTask
                ),
                MDFlatButton(
                    text = "CANCEL",
                    size_hint = (.2, .2),
                    pos_hint = {'center_x': 0.6,'center_y': 0.15},
                    on_release = self.Cancel
                )
            ),
            orientation = 'vertical',
            size_hint = (.8, .4),
            pos_hint = {'center_x': 0.5,'center_y': 0.5},
            elevation = 4,
            radius = [20],
        )
        
        self.sm.get_screen('main').add_widget(self.card_task)
    
    def addTask(self, obj):
        
        if self.card_task:
            if not self.textField_1_task.text and not self.textInput_2_task.text:
                self.textField_1_task.text = "Task: None"
                self.textInput_2_task.text = "Information: None"

            self.creatingASwiperItem(self.textField_1_task.text, self.textInput_2_task.text)
            self.sm.get_screen('main').remove_widget(self.card_task)
            self.card_task = None
            
            with open('tasks.txt', 'a') as taskFile:
                taskFile.write(f"Task Name: {self.textField_1_task.text}\nTask Description: {self.textInput_2_task.text}\n")
        
    def CheckTask(self, instance):
        
        # gray [0.5019607843137255, 0.5019607843137255, 0.5019607843137255, 1.0]
        # green [0.4470588235294118, 0.8, 0.3137254901960784, 1.0]
        
        if instance.md_bg_color == [0.5019607843137255, 0.5019607843137255, 0.5019607843137255, 1.0]:
            instance.md_bg_color = "#72CC50"
        else:
            instance.md_bg_color = "gray"
            
    def removeTask(self, instance):
        
        for i in range(len(self.listOfButtons)):
            if self.listOfButtons[i] == instance:
                self.sm.get_screen('main').ids.TaskSwiper.remove_widget(self.listOfTasks[i])
                self.listOfTasks.remove(self.listOfTasks[i])
                self.listOfButtons.remove(self.listOfButtons[i])
                with open('tasks.txt', 'r') as file:
                    counter = 0
                    with open('temp.txt', 'a') as temp:
                        for line in file:
                            if counter != (i*2) and counter != (i*2+1):
                                temp.write(line)
                            counter += 1
                break
        os.replace('temp.txt', 'tasks.txt')
    
                
    def on_start(self):
        items = []
        string_list = []
        string = ""
        i = 1
        
        with open('/Users/pierstrbad/Desktop/Programi/Python/Kivy/NewApp/racuni.txt', 'r') as file:
            for x in file:
                if x != "\n":
                    bill = open(x.strip(),"r")
                    self.BillPaths.append(x.strip())
                    dict = {'Name': "",'Date': "", 'Items': []}
                    for a in bill:
                        if a[0].isdigit():
                            dict['Date'] = a
                        else:
                            dict['Name'] = f'Racun {i}'
                            items.append(a)
                    dict['Items'] = items
                    self.Bill.append(dict)
                    items = []
                    i += 1
        
        bill.close()
        for i in self.Bill:
            for x in i['Items']:
                for y in x:
                    if y != ' ' and y != '\n':
                        string += y
                    else:
                        string_list.append(string)
                        string = ""

        self.TotalAmount(string_list)
        
        self.totalProfit = round(self.totalProfit,2)
        self.sm.get_screen('main').ids.TotalProfit.text = f"TOTAL PROFIT: {str(self.totalProfit)}$"
        
        temp_name = temp_number = ""
        with open('phonebook.txt', 'r') as file:
            if os.path.getsize('phonebook.txt') != 0:
                for x in file:
                    for i in x:
                        if not i.isdigit():
                            temp_name += i
                        else:
                            temp_number += i

                    self.sm.get_screen('P').ids.PhoneBookNumbers.add_widget(
                        TwoLineIconListItem(
                            IconLeftWidget(
                                icon="account"
                            ),
                            text = str(temp_name).strip('\n'),
                            secondary_text = "Number: " + str(temp_number).strip('\n'),
                            on_release = self.obj_p.PressedItem,
                            bg_color = (1,1,1,1),
                            radius = [25]
                            )
                    )
                    temp_name = temp_number = ""
                
        with open('tasks.txt', 'r') as taskFile:
            taskListFromFile = []
            item = []
            for i in taskFile:
                if i.strip('\n').startswith("Task Name:"):
                    item.append(i.replace('Task Name: ', ''))
                elif i.strip('\n').startswith("Task Description:"):
                    item.append(i.replace('Task Description: ', ''))
                if len(item) == 2:
                    taskListFromFile.append(item)
                    item = []

        for i in taskListFromFile:
            name = i[0].strip()
            description = i[1].strip()
            self.creatingASwiperItem(name, description)
                
    def on_stop(self):

        #self.menuForDisplaying = None
        #self.menuForDeleting = None
        #self.card = None
        #self.textField_1 = None
        #self.textField_2 = None
        #self.textInput_3 = None
        #self.deleteCard = None
        #self.menuForItems = None
        #self.textField_1_task = None
        #self.textInput_2_task = None
        #self.card_task = None
        #self.TaskItem = None
        #self.checkbutton = None
        #self.deleteButton = None
        
        self.Bill.clear()
        self.BillPaths.clear()
        self.ListOfItems.clear()
        self.listOfTasks.clear()
        self.listOfButtons.clear()

    def TotalAmount(self, string_list):
        
        temp_list = []
        
        for i in string_list:
           test = str(i)
           res = test.replace('.','',1).isdigit()
           if res:
               if test.isdigit():
                   amount = int(test)
               if not test.isdigit():
                   self.totalProfit += float(test) * amount
           elif not res:
               temp_list.append(test)
            
        if self.ListOfItems == []:
            self.ListOfItems = list(set(temp_list))
            self.ListOfItems.sort()
        else:
            temp_list += self.ListOfItems
            self.ListOfItems = list(set(temp_list))
            self.ListOfItems.sort()
            
    def creatingASwiperItem(self, task, description):
        self.checkbutton = MDFloatingActionButton(
                           icon = 'check-bold',
                           pos_hint = {'center_x': 0.55,'center_y': 0.2},
                           md_bg_color = "gray",
                           elevation = None,
                           on_release = self.CheckTask
                        )
        self.deleteButton = MDFloatingActionButton(
                       icon = 'delete',
                       pos_hint = {'center_x': 0.82,'center_y': 0.2},
                       md_bg_color = "red",
                       elevation = None,
                       on_release = self.removeTask
                    )
        self.TaskItem = MDSwiperItem(
               MDFloatLayout(
                   self.checkbutton,
                   self.deleteButton,
                   MDCard(
                       MDLabel(
                           markup = True,
                           text = f'[b]{task}[/b]',
                           font_size = 55,
                           halign = 'center'
                       ),
                       orientation = 'vertical',
                       elevation = 1,
                       md_bg_color = (1,1,1,1),
                       size_hint = (0.9, 0.1),
                       pos_hint = {'center_x': 0.5,'center_y': 0.9}
                   ),
                   MDCard(
                       MDFloatLayout(
                           MDLabel(
                               markup = True,
                               text = f'[b]{description}[/b]',
                               pos_hint = {'center_x': 0.5,'center_y': 0.9},
                               font_size = 45
                           )
                       ),
                       orientation = 'vertical',
                       elevation = 1,
                       md_bg_color = (1,1,1,1),
                       size_hint = (.9, .4),
                       pos_hint = {'center_x': 0.5,'center_y': 0.6},
                       padding = 20,
                       spacing = 10
                   )
               ),
               radius = [25,],
               md_bg_color = (0, 153/250, 1, 255/250)
            )
        self.listOfTasks.append(self.TaskItem)
        self.listOfButtons.append(self.deleteButton)
        self.sm.get_screen('main').ids.TaskSwiper.add_widget(self.TaskItem)
        
if __name__ == '__main__':
    PerfectStoreApp().run()