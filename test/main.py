from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (450, 500)

LoginPage = """
MDFloatLayout:
    MDLabel:
        text: "Login"
        pos_hint: {"center_y": .85}
        font_style: "H4"
        halign: "center"
        theme_text_color: "Custom"
        text_color: 0,0,0,1
   
    MDLabel:
        text: "Welcome T"
        pos_hint: {"center_y": .85}
        font_style: "H4"
        halign: "center"
        theme_text_color: "Custom"
        text_color: 0,0,0,1
"""
class Tutorial(MDApp):
    def build(self):
        login_page = Builder.load_string(LoginPage)
        return login_page

if __name__ == "__main__":
    Tutorial().run()