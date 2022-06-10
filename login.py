from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = GridLayout()
        self.layout.cols = 1
        self.username = TextInput(multiline=False)
        self.password = TextInput(password=True, multiline=False)
        self.layout.add_widget(Label(text='Username'))
        self.layout.add_widget(self.username)
        self.layout.add_widget(Label(text='Password'))
        self.layout.add_widget(self.password)
        self.add_widget(self.layout)
