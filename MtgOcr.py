import easyocr
import pandas as pd
import matplotlib.pyplot as plt
from scryfall import scryfall_api as sf

class MtgOcr:
    def __init__(self):
        self.reader = easyocr.Reader(lang_list=['es','en'], gpu= False)

    def read_card(self, img_path : str):
        res = self.reader.readtext(img_path)
        rDf=pd.DataFrame(res)
        cardName = rDf[1][0]
        for row in rDf.itertuples():
            val = sf.card_by_name(cardName)
            if val is not None:
                break
            cardName = row[2]
        return sf.version_prices(cardName)