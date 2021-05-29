
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatIconButton
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivymd.uix.button import MDRaisedButton #Прямоугольная Плоская кнопка MD

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window #Для размера окна
from kivy.uix.popup import Popup
Window.size = (480, 600)

KV="""
СС:
    send_fone: fone
    ch: but
    MDScreen:
        FitImage:
            source: 'fS6tmUgBPmw.jpg'

        GridLayout:
            rows: 10

            BoxLayout:
                orientation: 'vertical'
            BoxLayout:
                orientation: 'vertical'
            BoxLayout:
                orientation: 'vertical'

            
                
                
                MDTextField:
                    id: fone
                    hint_text: "Введите номер телефона"
                    line_color_focus: 1, 0, 1, 1
                    multiline: False
                    size_hint: .8 , .1
                    pos_hint: {'center_x':0.5,'center_y':0.7}
            BoxLayout:
                orientation: 'vertical'    
                MDTextButton:
                    id: but
                    pos_hint: {'center_x':0.5,'center_y':0.5}
                    size_hint: 0.5,0.1
                    text: "Войти"
                    font_size:  '25sp'
                    icon: "android"
                    theme_text_color: "Custom"
                    on_release:
                        root.send()  

            BoxLayout:
                orientation: 'vertical'
            BoxLayout:
                orientation: 'vertical'
            BoxLayout:
                orientation: 'vertical'
            BoxLayout:
                orientation: 'vertical'
            BoxLayout:
                orientation: 'vertical'        
            BoxLayout:
                orientation: 'vertical'
"""
KV2 = '''
Code:
    MDScreen:
        FitImage:
            source: 'fS6tmUgBPmw.jpg'
'''
class Code(BoxLayout):
    pass

class СС(MDApp,BoxLayout):
    fl = 0
    def send(self):
        fone = self.send_fone.text
        self.ch.text="Подтвердить"
        self.send_fone.hint_text="Введите код"
        self.send_fone.text=""
        self.theme_cls.primary_palette = "BlueGray" #Основная палтра
        self.theme_cls.theme_style = "Light"           #Общий фон
        
        self.root = Builder.load_string(KV2)           # Исполняет код в KV
        return Builder.load_string(KV2)  


#class MainApp(MDApp):
#    def build(self):
#        return СС()
#class MainApp(MDApp):
#    def build(self):
#        self.root = Builder.load_string(KV)
    
#MainApp().run()
class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray" #Основная палтра
        self.theme_cls.theme_style = "Light"           #Общий фон
        
        self.root = Builder.load_string(KV)           # Исполняет код в KV
        return Builder.load_string(KV)


        
        
MainApp().run()