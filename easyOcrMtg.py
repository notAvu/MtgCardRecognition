from mtgsdk import Card, Set
cardName = input("Name of the card: ")
card = Card.where(name = cardName).all()
for c in card:
    print(f"Card name: {c.name} \n Cost {c.mana_cost}")