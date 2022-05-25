import cv2
from kivy.app import App
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.image import Image
import logging


class CameraCapture(Image):
    def __init__(self, capture: cv2.VideoCapture, fps: int):
        super().__init__()
        self.capture = capture
        Clock.schedule_interval(self.update, 1.0 / fps)

    def update(self, refresh_frequency: float):
        is_frame_grabbed, frame = self.capture.read()
        if is_frame_grabbed:
            buffer = cv2.flip(frame, 0).tobytes()
            # using the 'bgr' colour format since it's the default one in OpenCV
            image_texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            image_texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
            self.texture = image_texture
        else:
            logging.warning("The frame of the camera could not be captured!")


class WatchInClient(App):
    def build(self):
        self.capture = cv2.VideoCapture(0)
        self.camera = CameraCapture(capture=self.capture, fps=30)
        return self.camera

    def on_stop(self):
        self.capture.release()


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.DEBUG
    )
    WatchInClient().run()
