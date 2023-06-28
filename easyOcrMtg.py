from mtgsdk import Card, Set
# cardName = input("Name of the card: ")
# card = Card.where(name = cardName).all()
# for c in card:
#     print(f"Card name: {c.name} \n Cost {c.mana_cost}")
import easyocr
import pandas as pd
import matplotlib.pyplot as plt

img= plt.imshow(plt.imread("./Gobrecruiter.jpg"))
reader = easyocr.Reader(['en', 'es'], gpu= False)
results = reader.readtext("./Gobrecruiter.jpg")
rDf=pd.DataFrame(results)
plt.show()
print(rDf[1][0])