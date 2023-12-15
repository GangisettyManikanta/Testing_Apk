from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen

kv="""
BoxLayout:
    orientation: 'vertical'

    ScreenManager:
        id: screen_manager

        Screen:
            name: 'borrower_reg_form1'

            Image:
                source: 'C:\\kivymd\\images\\kotak.png'
                size_hint: None, None  # This line ensures that size is not hinted
                size: 200, 80  # Adjust the size as per your requirement
                pos_hint: {'x': 0, 'top': 1}

            MDRectangleFlatButton:
                text: 'HOME'
                text_color: 0, 0, 0, 1  # Black text color
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'top': 1}
                on_release: app.go_home()
                size_hint: (0.1, 0.03)
                font_size: "13sp"

            MDBoxLayout:
                orientation: 'vertical'
                spacing: dp(10)
                padding: dp(10)
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300
                MDCard:
                    orientation: "vertical"
                    size_hint: None, None
                    size: "280dp", "480dp"
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}

                    MDLabel:
                        text: 'Borrower Registration Form1'
                        font_size: 25
                        halign: 'center'
                        bold: True

                    MDTextField:
                        id: username
                        hint_text: 'Enter full name'
                        multiline: False
                        helper_text: 'Enter valid name'
                        helper_text_mode: 'on_focus'
                        size_hint_y: None
                        height: self.minimum_height
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: None
                        width: 300
                        font_name: "Roboto-Bold"

                    MDTextField:
                        id: email
                        hint_text: 'Enter email'
                        multiline: False
                        helper_text: 'Enter valid email'
                        helper_text_mode: 'on_focus'
                        size_hint_y: None
                        height: self.minimum_height
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: None
                        width: 300
                        font_name: "Roboto-Bold"
                    MDTextField:
                        id: phno
                        hint_text: 'Enter phno'
                        multiline: False
                        helper_text: 'Enter valid phno'
                        helper_text_mode: 'on_focus'
                        size_hint_y: None
                        height: self.minimum_height
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: None
                        width: 300
                        font_name: "Roboto-Bold"
                    MDTextField:
                        id: alternate_email
                        hint_text: 'Enter alternate email'
                        multiline: False
                        helper_text: 'Enter valid email'
                        helper_text_mode: 'on_focus'
                        size_hint_y: None
                        height: self.minimum_height
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: None
                        width: 300
                        font_name: "Roboto-Bold"
                    MDTextField:
                        id: alternate_ph_no
                        hint_text: 'Enter alternate ph no'
                        multiline: False
                        helper_text: 'Enter valid no'
                        helper_text_mode: 'on_focus'
                        size_hint_y: None
                        height: self.minimum_height
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: None
                        width: 300
                        font_name: "Roboto-Bold"
                    BoxLayout:
                        spacing: dp(10)
                        size_hint_x: None
                        height: "60dp"
                        width: "60dp"
                        pos_hint: {'center_x': 0.4, 'center_y': 0.6}
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1
                        md_bg_color: 0, 0, 0, 1
                        MDRectangleFlatButton:
                            text: 'Back'
                            text_color: 0, 0, 0, 1  # Black text color
                            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                            md_bg_color: 0.031, 0.463, 0.91, 1
                            on_release: app.root.ids.screen_manager.current = 'borrower_reg_form1'

                        MDRectangleFlatButton:
                            text: 'Next'
                            text_color: 0, 0, 0, 1  # Black text color
                            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                            md_bg_color: 0.031, 0.463, 0.91, 1
                            on_release: app.root.ids.screen_manager.current = 'borrower_reg_form3'

            
"""

class DemoApp(MDApp):
    def build(self):
        return Builder.load_string(kv)
DemoApp().run()