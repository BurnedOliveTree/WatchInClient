from typing import Any, List
from kivy.uix.label import Label

from controller.switchable_screen import SwitchableScreen


class AppendableScreen(SwitchableScreen):
    def __init__(self, name: str, content: List[str] = [], **kwargs):
        super().__init__(name=name, **kwargs)
        self.append([Label(text=child) for child in content])
    
    def append(self, children: List[Any]):
        for child in children:
            self.children[0].add_widget(child)
    
    def clear(self, childType):
        for child in reversed(self.children[0].children):
            if isinstance(child, childType):
                self.children[0].remove_widget(child)
