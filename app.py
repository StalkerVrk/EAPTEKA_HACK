from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton #Прямоугольная Плоская кнопка MD
from kivy.lang import Builder #Конструктор типа Lang 
from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout

from kivy.core.window import Window #Для размера окна

Window.size = (480, 853)


KV = '''
MDScreen:

    FitImage:
        source:'fS6tmUgBPmw.jpg'
    
    

    MDRaisedButton:
        text: "Кнопка Светлее"
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
        md_bg_color: app.theme_cls.primary_light

    MDRaisedButton:
        text: "Обычный цвет"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}

    MDRaisedButton:
        text: "Тёмный цвет"
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        md_bg_color: app.theme_cls.primary_dark

    MDRectangleFlatButton:
        text: "Прозрачная кнопка"
        pos_hint: {"center_x": .2, "center_y": .6} 
        md_bg_color: app.theme_cls.primary_light   
'''

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray" #Основная палтра
        self.theme_cls.theme_style = "Light"           #Общий фон
        
        self.root = Builder.load_string(KV)           # Исполняет код в KV
        return Builder.load_string(KV)
    
    def on_start(self):
        self.fps_monitor_start()

        
        
MainApp().run()