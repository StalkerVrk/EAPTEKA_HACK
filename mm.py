from typing import KeysView
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatIconButton
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivymd.uix.button import MDRaisedButton #Прямоугольная Плоская кнопка MD

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.app import App
from kivy.lang import Builder

KV = '''
Code:
    MDScreen:
        FitImage:
            source: 'fS6tmUgBPmw.jpg'
'''
class SettingScreen(App):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray" #Основная палтра
        self.theme_cls.theme_style = "Light"           #Общий фон
        
        self.root = Builder.load_string(KV)           # Исполняет код в KV
        return Builder.load_string(KV)


if __name__ == "__main__":
    SettingScreen().run()


