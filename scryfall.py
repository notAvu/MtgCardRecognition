import requests
import json
import pandas as pd
import numpy as np
from mtgsdk import Card
from types import SimpleNamespace


class scryfall_api:
    def card_by_mkm_id(id):
        req = requests.get(f"https://api.scryfall.com/cards/cardmarket/{id}")
        jason = json.loads(req.content, object_hook=lambda d: SimpleNamespace(**d))
        return jason
    def parse_name(cardName) ->str:
        # cardName = Card.where(name = cardName).where(language= '').all()
        return cardName.replace(" ","+")
    def card_by_name(name):
        formated_name = scryfall_api.parse_name(name)
        req = requests.get(f"https://api.scryfall.com/cards/named?fuzzy={formated_name}")
        if req.status_code == 200:
            jason = json.loads(req.content, object_hook=lambda d: SimpleNamespace(**d))
        else:
            jason = None
        return jason
    def price_by_name(name):
        formated_name = scryfall_api.parse_name(name)
        return scryfall_api.card_by_name(formated_name).prices.eur
    def search_by_name(name):
        #TODO: allow search parameters 
        formated_name = scryfall_api.parse_name(name)
        req = requests.get(f"https://api.scryfall.com/cards/search?order=released&include_multilingual=true&unique=prints&q=!{formated_name}")
        jason = json.loads(req.content, object_hook=lambda d: SimpleNamespace(**d))
        return jason
    def version_prices(name):
        versions = scryfall_api.search_by_name(name)
        dataframe = pd.DataFrame(columns=['Card Name', 'version', 'price', 'price foil'])
        for v in versions.data:
            dataframe.loc[v.collector_number] = [v.name, v.set, v.prices.eur, v.prices.eur_foil]
            dataframe.reset_index()
        return dataframe
