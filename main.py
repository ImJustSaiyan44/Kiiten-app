from kivy.app import App
from kivy.metrics import dp
from kivy.lang.builder import Builder
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.datatables import MDDataTable
from kivymd.app import MDApp
import os
import gspread

path = 'D:\Programming\KittenApp'
file_name = 'Cred.json'
os.path.join(path, file_name)
gc = gspread.service_account(filename= 'Cred.json')
sh = gc.open('Kitten Weights')
kE1 = sh.worksheet('Kitten1')
kE2 = sh.worksheet('Kitten2')
kE3 = sh.worksheet('Kitten3')
kE4 = sh.worksheet('Kitten4')
whichCat = 0
addi = False
fixi = False

  
screen_helper = """

ScreenManager:
    id: sm
    MenuScreen:
    oneKitten:
    twoKitten:
    threeKitten:
    fourKitten:
    addScreen:
    fixScreen:
<MenuScreen>:
    name: 'menu'
    MDToolbar:
        id: toolbar
        title: "Kittens"
        anchor_title: "center"
        elevation: 10
        pos_hint: {"top": 1}
    Image:
        id: k1pic
        source: 'Pictures\Kitten_1.jpg'
        size_hint_x: 0.2
        size_hint_y: 0.2
        pos_hint: {'center_x':0.75,'center_y':0.75}
    MDFillRoundFlatButton:
        id: k1
        text: 'Kitten 1'
        pos_hint: {'center_x':0.35,'center_y':0.75}
        on_press: root.manager.current = 'oneKitten'
    Image:
        id: k2pic
        source: 'Pictures\Kitten_2.jpg'
        size_hint_x: 0.2
        size_hint_y: 0.2
        pos_hint: {'center_x':0.75,'center_y':0.55}
    MDFillRoundFlatButton:
        id: k2
        text: 'Kitten 2'
        pos_hint: {'center_x':0.35,'center_y':0.55}
        on_press: root.manager.current = 'twoKitten'
    Image:
        id: k3pic
        source: 'Pictures\Kitten_3.jpg'
        size_hint_x: 0.2
        size_hint_y: 0.2
        pos_hint: {'center_x':0.75,'center_y':0.35}
    MDFillRoundFlatButton:
        id: k3
        text: 'Kitten 3'
        pos_hint: {'center_x':0.35,'center_y':0.35}
        on_press: root.manager.current = 'threeKitten'
    Image:
        id: k4pic
        source: 'Pictures\Kitten_4.jpg'
        size_hint_x: 0.2
        size_hint_y: 0.2
        pos_hint: {'center_x':0.75,'center_y':0.15}
    MDFillRoundFlatButton:
        id: k4
        text: 'Kitten 4'
        pos_hint: {'center_x':0.35,'center_y':0.15}
        on_press: root.manager.current = 'fourKitten'

<oneKitten>:
    name: 'oneKitten' 
    MDLabel:
        text: 'Kitten 1'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.3}
    MDFillRoundFlatButton:
        text: 'Go Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'
    MDFillRoundFlatButton:
        text: 'Add Input'
        pos_hint: {'center_x':0.4,'center_y':0.3}
        on_press: root.manager.current = 'add'
        on_press: root.whatCat()
        on_press: root.add()
    MDFillRoundFlatButton:
        text: 'Fix Input'
        pos_hint: {'center_x':0.6,'center_y':0.3}
        on_press: root.manager.current = 'fix'
        on_press: root.whatCat()
        on_press: root.fix()
        
<twoKitten>:
    name: 'twoKitten'
    MDLabel:
        text: 'Kitten 2'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.3}
    MDFillRoundFlatButton:
        text: 'Go Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'
    MDFillRoundFlatButton:
        text: 'Add Input'
        pos_hint: {'center_x':0.4,'center_y':0.3}
        on_press: root.manager.current = 'add'
        on_press: root.whatCat()
        on_press: root.add()
    MDFillRoundFlatButton:
        text: 'Fix Input'
        pos_hint: {'center_x':0.6,'center_y':0.3}
        on_press: root.manager.current = 'fix'
        on_press: root.whatCat()
        on_press: root.fix()
<threeKitten>:
    name: 'threeKitten'
    MDLabel:
        text: 'Kitten 3'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.3}
    MDFillRoundFlatButton:
        text: 'Go Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'
    MDFillRoundFlatButton:
        text: 'Add Input'
        pos_hint: {'center_x':0.4,'center_y':0.3}
        on_press: root.manager.current = 'add'
        on_press: root.whatCat()
        on_press: root.add()
    MDFillRoundFlatButton:
        text: 'Fix Input'
        pos_hint: {'center_x':0.6,'center_y':0.3}
        on_press: root.manager.current = 'fix'
        on_press: root.whatCat()
        on_press: root.fix()
        
<fourKitten>:
    name: 'fourKitten'
    MDLabel:
        text: 'Kitten 4'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.3}
    MDFillRoundFlatButton:
        text: 'Go Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'
    MDFillRoundFlatButton:
        text: 'Add Input'
        pos_hint: {'center_x':0.4,'center_y':0.3}
        on_press: root.manager.current = 'add'
        on_press: root.whatCat()
        on_press: root.add()
    MDFillRoundFlatButton:
        text: 'Fix Input'
        pos_hint: {'center_x':0.6,'center_y':0.3}
        on_press: root.manager.current = 'fix'
        on_press: root.whatCat()
        on_press: root.fix()
<addScreen>:
    date: Date
    weight: Weight
    notes: Notes
    name: 'add'
    MDFillRoundFlatButton:
        text: 'Go Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'
    MDFillRoundFlatButton:
        text: 'Submit'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: root.manager.current = 'menu'
        on_press: root.btn()
    MDLabel:
        text: 'Date'
        font_size: 20
        halign: 'center'
        pos_hint: {'center_x':0.15,'center_y':0.7}
    MDLabel:
        text: 'Weight'
        font_size: 20
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.7}
    MDLabel:
        text: 'Notes'
        font_size: 20
        halign: 'center'
        pos_hint: {'center_x':0.85,'center_y':0.7}
    TextInput:
        id: Date
        size_hint: (0.2, 0.3)
        pos_hint: {'center_x':0.15,'center_y':0.5}
        on_text: self.foreground_color = (1,1,1,1)
        foreground_color: (0,0,0,1)
        background_color: 0.129, 0.58, 0.95, 1
    TextInput:
        id: Weight
        size_hint: (0.2, 0.3)
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_text: self.foreground_color = (1,1,1,1)
        foreground_color: (0,0,0,1)
        background_color: 0.129, 0.58, 0.95, 1
    TextInput:
        id: Notes
        size_hint: (0.2, 0.3)
        pos_hint: {'center_x':0.85,'center_y':0.5}
        on_text: self.foreground_color = (1,1,1,1)
        foreground_color: (0,0,0,1)
        background_color: 0.129, 0.58, 0.95, 1
<fixScreen>:
    name: 'fix'
    MDFillRoundFlatButton:
        text: 'Go Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'

        
"""


class MenuScreen(Screen):
   pass
class oneKitten(Screen):
    def whatCat(self):
        global whichCat
        whichCat = 1
    def add(self):
        global addi
        addi = True
    def fix(self):
        global fixi
        fixi = True      
class twoKitten(Screen):
    def whatCat(self):
        global whichCat
        whichCat = 2
    def add(self):
        global addi
        addi = True
    def fix(self):
        global fixi
        fixi = True   
class threeKitten(Screen):
    def whatCat(self):
        global whichCat
        whichCat = 3
    def add(self):
        global addi
        addi = True
    def fix(self):
        global fixi
        fixi = True   
class fourKitten(Screen):
    def whatCat(self):
        global whichCat
        whichCat = 4
    def add(self):
        global addi
        addi = True
    def fix(self):
        global fixi
        fixi = True   
class addScreen(Screen):
    date = ObjectProperty(None)
    weight = ObjectProperty(None)
    notes = ObjectProperty(None)
    def btn(self):
        if whichCat == 1:
            valList1 = []
            valList1 = kE1.col_values(1)
            cellNum = len(valList1) + 1 
            A = 'A' + str(cellNum)
            B = 'B' + str(cellNum)
            C = 'C' + str(cellNum)
            kE1.update(A, self.date.text)
            kE1.update(B, self.weight.text)
            kE1.update(C, self.notes.text)
            self.date.text = ""
            self.weight.text = ""
            self.notes.text = ""
            valList1 = []
            infoList = []
        elif whichCat == 2:
            valList1 = []
            valList1 = kE2.col_values(1)
            cellNum = len(valList1) + 1 
            A = 'A' + str(cellNum)
            B = 'B' + str(cellNum)
            C = 'C' + str(cellNum)
            kE1.update(A, self.date.text)
            kE1.update(B, self.weight.text)
            kE1.update(C, self.notes.text)
            self.date.text = ""
            self.weight.text = ""
            self.notes.text = ""
            valList1 = []
            infoList = []
        elif whichCat == 3:
            valList1 = []
            valList1 = kE3.col_values(1)
            cellNum = len(valList1) + 1 
            A = 'A' + str(cellNum)
            B = 'B' + str(cellNum)
            C = 'C' + str(cellNum)
            kE1.update(A, self.date.text)
            kE1.update(B, self.weight.text)
            kE1.update(C, self.notes.text)
            self.date.text = ""
            self.weight.text = ""
            self.notes.text = ""
            valList1 = []
            infoList = []
        else:
            valList1 = []
            valList1 = kE4.col_values(1)
            cellNum = len(valList1) + 1 
            A = 'A' + str(cellNum)
            B = 'B' + str(cellNum)
            C = 'C' + str(cellNum)
            kE1.update(A, self.date.text)
            kE1.update(B, self.weight.text)
            kE1.update(C, self.notes.text)
            self.date.text = ""
            self.weight.text = ""
            self.notes.text = ""
            valList1 = []
            infoList = []
class fixScreen(Screen):
    pass

# Create the screen manager
screenManager = ScreenManager()
screenManager.add_widget(MenuScreen(name='menu'))
screenManager.add_widget(oneKitten(name='oneKitten'))
screenManager.add_widget(twoKitten(name='twoKitten'))
screenManager.add_widget(threeKitten(name='threeKitten'))
screenManager.add_widget(fourKitten(name='fourKitten'))
screenManager.add_widget(addScreen(name='add'))
screenManager.add_widget(fixScreen(name='fix'))

class KittenApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        screen = Screen()
        builder = Builder.load_string(screen_helper)
        return builder
    def initilize_global_vars(self):
        root_folder = self.user_data_dir
        cache_folder = os.path.join(root_folder, 'D:\Programming\KittenApp')

        if not os.path.exists(cache_folder):
            os.makedirs(cache_folder)

# if __name__ == '__main__':
KittenApp().run()