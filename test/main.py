from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

Window.size = (380, 500)

Builder.load_string( """
<Enter>:
    MDFloatLayout:
        MDScreen:
            FitImage:
                source: 'Dawn.jpg'
        MDLabel:
            text: "Login"
            pos_hint: {"center_y": .85}
            font_style: "H4"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 0,0,0,1
        MDLabel:
            text: "Welcome To EAPTEKA"
            pos_hint: {"center_y": .75}
            font_style: "H5"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 0,0,0,1
        MDTextField:
            hint_text: "Enter Your Number"
            pos_hint: {"center_x": .5, "center_y": .6}
            current_hint_text_color: 0,0,0,1
            size_hint_x: .8
        
        MDRaisedButton:
            text: "Input"
            pos_hint: {"center_x": .5, "center_y": .3}
            size_hint_x: .5
""")
class Enter(Screen):
    pass


SM = ScreenManager() #для создания окон

class Tutorial(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        
        SM.add_widget(Enter(name='enter'))
        return SM

if __name__ == "__main__":
    Tutorial().run()