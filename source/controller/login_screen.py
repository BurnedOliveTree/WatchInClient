from typing import Any, List
from kivy.uix.label import Label

from controller.switchable_screen import SwitchableScreen
from model import login


class LoginScreen(SwitchableScreen):
    def __init__(self, name: str, **kwargs):
        super().__init__(name=name, **kwargs)
    
    def login(self):
        login(self.children[0].ids.username.text, self.children[0].ids.password.text, False)
