import easyocr
import pandas as pd
import matplotlib.pyplot as plt
from scryfall import scryfall_api as sf

img= plt.imshow(plt.imread("./opt.jpg"))
reader = easyocr.Reader(lang_list=['es','en'], gpu= False)
results = reader.readtext("./opt.jpg")
rDf=pd.DataFrame(results)

print(rDf)
cardName = rDf[1][0]
for row in rDf.itertuples():
    val = sf.card_by_name(cardName)
    if val is not None:
        break
    cardName = row[2]

print(f"{sf.version_prices(cardName)}")