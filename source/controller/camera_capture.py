import cv2
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
import logging


class CameraCapture(Screen):
    def __init__(self, fps: int, **kwargs):
        super().__init__(**kwargs)
        self.layout = Image()
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.update, 1.0 / fps)
        self.add_widget(self.layout)

    def update(self, refresh_frequency: float):
        is_frame_grabbed, frame = self.capture.read()
        if is_frame_grabbed:
            buffer = cv2.flip(frame, 0).tobytes()
            # using the 'bgr' colour format since it's the default one in OpenCV
            image_texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            image_texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
            self.layout.texture = image_texture
        else:
            logging.warning("The frame of the camera could not be captured!")
    
    def on_stop(self):
        self.capture.release()
    
    def __del__(self):
        self.on_stop()
