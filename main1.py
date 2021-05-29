
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatIconButton
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivymd.uix.button import MDRaisedButton #Прямоугольная Плоская кнопка MD
import requests
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window #Для размера окна
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
Window.size = (480, 600)
# Create the manager

Builder.load_string("""
<Autorith>:
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
                        root.manager.current = 'code'    

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
<Code>:
    send_cod: cod
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
                    id: cod
                    hint_text: "Введите код из сообщения"
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
                    text: "Подтвердить"
                    font_size:  '25sp'
                    icon: "android"
                    theme_text_color: "Custom"
                    on_release:
                        root.sendcode()

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
<Menu>:
    send_cod: cod
    ch: but
    MDScreen:
        FitImage:
            source: 'fS6tmUgBPmw.jpg'
""")

class Menu(Screen):
    pass

class Code(Screen):
    def sendcode(self):
        hash1=""
        hash2=""
        #requests.get('htt://45.128.207.185:8000',params={'phone':fone})
        #self.send_fone.hint_text="Введите код"
        #self.send_fone.text=""
        #hash2=""
        sm.switch_to(Menu(name='menu'))

class Autorith(Screen):
    def send(self):
        hash1=""
        hash2=""
        fone = self.send_fone.text
        self.ch.text="Подтвердить"
        #requests.get('htt://45.128.207.185:8000',params={'phone':fone})
        self.send_fone.hint_text="Введите код"
        self.send_fone.text=""
        hash2=""
        sm.switch_to(Code(name='code'))
        
sm = ScreenManager()    
class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray" #Основная палтра
        self.theme_cls.theme_style = "Light"           #Общий фон
        
        sm.add_widget(Autorith(name='autorith'))
        #sm.add_widget(Code(name='code'))
        sm.current = 'autorith'
        return sm

    


        
if __name__ == '__main__':     
    MainApp().run()