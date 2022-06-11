from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen


class SwitchableScreen(Screen):
    def __init__(self, name: str, **kwargs):
        super().__init__(name=name, **kwargs)
        self.add_widget(Builder.load_file(f'view/{name}.kv'))
    
    def switch_screen(self, name: str, to_left = True):
        self.manager.transition.direction = 'right' if to_left else 'left'
        self.manager.transition.duration = 1
        self.manager.current = name
