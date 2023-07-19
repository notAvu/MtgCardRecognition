from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from glob import glob
from random import randint
from os.path import join, dirname
from kivy.logger import Logger
from kivy.properties import StringProperty
import time
from MtgOcr import MtgOcr as ocr
Builder.load_string('''
<CameraClick>:
    orientation: 'vertical'
    Camera:
        id: camera
        play: False
    ToggleButton:
        text: 'Play'
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: '48dp'
    Button:
        text: 'Scan'
        size_hint_y: None
        height: '48dp'
        on_press: root.capture()
''')

class CameraClick(BoxLayout):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        imageName = "IMG_{}.png".format(timestr)
        camera.export_to_png(imageName)
        cardReader = ocr()
        cardReader.read_card("{}/IMG_{}.png".format(self.curdir,imageName))
        print("Captured")

class TestCamera(App):

    def build(self):
        root = self.root
        self.curdir = dirname(__file__)
        return CameraClick()

if __name__ == "__main__":
    TestCamera().run()