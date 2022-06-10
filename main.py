import cv2
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
import logging

from camera_capture import CameraCapture
from login import LoginScreen
from menu import MenuScreen


class WatchInClient(App):
    def build(self):
        self.menu = MenuScreen()
        self.login = LoginScreen(name='login')
        self.capture = cv2.VideoCapture(0)
        self.camera = CameraCapture(capture=self.capture, fps=30, name='camera')

        self.manager = ScreenManager()
        self.manager.add_widget(self.menu)
        self.manager.add_widget(self.login)
        self.manager.add_widget(self.camera)
        return self.manager

    def on_stop(self):
        self.capture.release()


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.DEBUG
    )
    WatchInClient().run()
