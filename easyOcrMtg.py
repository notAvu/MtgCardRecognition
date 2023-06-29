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
if sf.card_by_name(cardName) == None:
    cardName = rDf[1][1]
print(f"{sf.version_prices(cardName)}")

# card = Card.where(name = cardName).all()
# for c in card:
#     print(f"Card: {c.name} ({c.set}) \n Cost: {c.mana_cost} \n Cardmarket: {3}€")