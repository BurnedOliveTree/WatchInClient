from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
import logging

from controller import CameraCapture, SwitchableScreen


class WatchInClient(App):
    def build(self):
        self.menu = SwitchableScreen(name='menu')
        self.login = SwitchableScreen(name='login')
        self.camera = CameraCapture(fps=30, name='camera')

        self.manager = ScreenManager()
        self.manager.add_widget(self.menu)
        self.manager.add_widget(self.login)
        self.manager.add_widget(self.camera)
        return self.manager

    def on_stop(self):
        self.camera.on_stop()


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.DEBUG
    )
    WatchInClient().run()
