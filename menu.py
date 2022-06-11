from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen


class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(padding=64, spacing=64)
        login_button = Button(text='Login')
        camera_button = Button(text='Camera')
        login_button.bind(on_press=lambda instance: self.switch_screen('login', True))
        camera_button.bind(on_press=lambda instance: self.switch_screen('camera', False))
        self.layout.add_widget(login_button)
        self.layout.add_widget(camera_button)
        self.add_widget(self.layout)
    
    def switch_screen(self, name: str, to_left = True):
        self.manager.transition.direction = 'right' if to_left else 'left'
        self.manager.transition.duration = 1
        self.manager.current = name
