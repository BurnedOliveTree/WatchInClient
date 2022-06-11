from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(padding=64, spacing=64, orientation='vertical')
        self.layout.cols = 1
        self.username = TextInput(multiline=False)
        self.password = TextInput(password=True, multiline=False)
        submit_button = Button(text='Submit')
        back_button = Button(text='Back')
        # TODO submit_button.bind
        back_button.bind(on_press=lambda instance: self.switch_screen('menu', False))
        self.layout.add_widget(Label(text='Username'))
        self.layout.add_widget(self.username)
        self.layout.add_widget(Label(text='Password'))
        self.layout.add_widget(self.password)
        inner_layout = BoxLayout(spacing=64, orientation='horizontal')
        inner_layout.add_widget(submit_button)
        inner_layout.add_widget(back_button)
        self.layout.add_widget(inner_layout)
        self.add_widget(self.layout)
    
    def switch_screen(self, name: str, to_left = True):
        self.manager.transition.direction = 'right' if to_left else 'left'
        self.manager.transition.duration = 1
        self.manager.current = name
