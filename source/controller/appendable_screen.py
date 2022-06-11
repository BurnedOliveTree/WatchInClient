from kivy.uix.label import Label
from controller.switchable_screen import SwitchableScreen


class AppendableScreen(SwitchableScreen):
    def __init__(self, name: str, **kwargs):
        super().__init__(name=name, **kwargs)
    
    def append(self, child):
        self.children[0].add_widget(child)
    
    def clear(self, childType):
        for child in reversed(self.children[0].children):
            if isinstance(child, childType):
                self.children[0].remove_widget(child)
