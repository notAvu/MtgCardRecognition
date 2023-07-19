from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
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
        cardReader.read_card("{}.png".format(imageName))
        print("Captured")

class TestCamera(App):

    def build(self):
        return CameraClick()

TestCamera().run()