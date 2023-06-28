from mtgsdk import Card, Set
import easyocr
import pandas as pd
import matplotlib.pyplot as plt

img= plt.imshow(plt.imread("./Gobrecruiter.jpg"))
reader = easyocr.Reader(['en', 'es'], gpu= False)
results = reader.readtext("./Gobrecruiter.jpg")
rDf=pd.DataFrame(results)
# plt.show()
print(rDf[1][0])
cardName = rDf[1][0]
card = Card.where(name = cardName).all()
for c in card:
    print(f"Card: {c.name} ({c.set}) \n Cost: {c.mana_cost} \n Cardmarket: {3}€")