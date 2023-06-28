from PIL import Image
import matplotlib.pyplot as plt
import keras_ocr
import numpy as np
import pandas as pd


class MtgImageRecognition:
    def __init__(self, images):
        self.imgs = images
        self.pipeline = keras_ocr.pipeline.Pipeline()
    def load_card(self):
        self.pred = self.pipeline.recognize(self.imgs)
        self.textDf_list = []
        for p in self.pred: 
            self.textDf_list.append(pd.DataFrame(p, columns=['text', 'box']))
    def show_card(self, index):
        fig, ax = plt.subplots(figsize=(10, 10))
        keras_ocr.tools.drawAnnotations(self.imgs[index], self.pred[index], ax=ax)
        plt.show()
    def get_card_name(self, index): return self.pred[index]

img = keras_ocr.tools.read("https://i.ebayimg.com/images/g/ecUAAOSw07diceIX/s-l1600.jpg")
yuriko = keras_ocr.tools.read("https://i.ebayimg.com/images/g/s~UAAOSws2dixw0m/s-l1200.webp")
ir = MtgImageRecognition([img,yuriko])
ir.load_card()
ir.show_card(1)
