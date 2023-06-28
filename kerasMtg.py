# from mtgsdk import Card, Set
# cardName = input("Name of the card: ")
# card = Card.where(name = cardName).all()
# for c in card:
#     print(f"Card name: {c.name} \n Cost {c.mana_cost}")

from PIL import Image
import matplotlib.pyplot as plt
import keras_ocr
import numpy as np
import pandas as pd
# class mtgHelper:
#     card
class MtgImageRecognition:
    def __init__(self, images):
        self.imgs = images
        self.pipeline = keras_ocr.pipeline.Pipeline()
    def load_card(self):
        self.pred = self.pipeline.recognize(self.imgs)
        self.textDf = pd.DataFrame(self.pred[0], columns=['text', 'box'])
    def show_card(self, index):
        fig, ax = plt.subplots(figsize=(10, 10))
        keras_ocr.tools.drawAnnotations(self.imgs[index], self.pred[index], ax=ax)
        plt.show()
        # fig, axs = plt.subplots(nrows=len(self.imgs), figsize=(20,20))
        # for ax, image, predictions in zip(axs, self.imgs, self.pred):
        #     keras_ocr.tools.drawAnnotations(image=image, predictions=predictions, ax = ax)
    def get_card_name(self):
        # self.pipeline.recognize(self.imgs)
        return 2

img = keras_ocr.tools.read("https://i.ebayimg.com/images/g/ecUAAOSw07diceIX/s-l1600.jpg")
yuriko = keras_ocr.tools.read("https://i.ebayimg.com/images/g/s~UAAOSws2dixw0m/s-l1200.webp")
ir = MtgImageRecognition([img,yuriko])
ir.load_card()
ir.show_card(1)
