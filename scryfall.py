import requests
import json
import pandas as pd
import numpy as np

from types import SimpleNamespace


class scryfall_api:
    def card_by_mkm_id(id):
        req = requests.get(f"https://api.scryfall.com/cards/cardmarket/{id}")
        jason = json.loads(req.content, object_hook=lambda d: SimpleNamespace(**d))
        return jason
    def parse_name(name) ->str:
        return name.replace(" ","+")
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
        req = requests.get(f"https://api.scryfall.com/cards/search?order=released&q={formated_name}")
        jason = json.loads(req.content, object_hook=lambda d: SimpleNamespace(**d))
        return jason
    def version_prices(name):
        versions = scryfall_api.search_by_name(name)
        dataframe = pd.DataFrame(columns=['Card Name', 'version', 'price', 'price foil'])
        for v in versions.data:
            # dict = {'Card Name': [v.name], 'version': [v.set], 'price': [v.prices.eur], 'price foil': [v.prices.eur_foil]}
            # aux_df = pd.DataFrame(dict)
            # aux_df = pd.DataFrame([v.name, v.set, v.prices.eur, v.prices.eur_foil],columns=['Card Name', 'version', 'price', 'price foil'])
            # pd.DataFrame.merge(dataframe,aux_df)
            dataframe.loc[v.collector_number] = [v.name, v.set, v.prices.eur, v.prices.eur_foil]
            dataframe.reset_index()
        return dataframe
