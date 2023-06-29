from mtgsdk import Card, Set
import easyocr
import pandas as pd
import matplotlib.pyplot as plt
from scryfall import scryfall_api as sf

img= plt.imshow(plt.imread("./opt.jpg"))
reader = easyocr.Reader(['en', 'es'], gpu= False)
results = reader.readtext("./opt.jpg")
rDf=pd.DataFrame(results)
# plt.show()
print(rDf)
cardName = rDf[1][0]
for index, row in rDf.iterrows():
    val = sf.card_by_name(cardName)
    if val != None:
        break
    cardName = row[1]
# while i < rDf.si:
#     cardName = rDf[1][i]
#     sf.card_by_name(cardName) == None


print(f"{sf.version_prices(cardName)}")