import requests
import json
import pandas as pd
from types import SimpleNamespace

class scryfall_api:

    # def card_by_mkm_id(id):
    #     """returns """
    #     req = requests.get(f"https://api.scryfall.com/cards/cardmarket/{id}")
    #     jason = json.loads(req.content, object_hook=lambda d: SimpleNamespace(**d))
    #     return jason

    def parse_name(cardName) ->str:
        """
        This method replaces whitespaces and any characters to allow for correct queries.
        TODO: test with different languages and cards to check and fix possible inconsistencies
        """
        return cardName.replace(" ","+")

    def card_by_name(name):
        """
        A method that fetches and retrieves data from a card given its name
        """
        formated_name = scryfall_api.parse_name(name)
        req = requests.get(f"https://api.scryfall.com/cards/named?fuzzy={formated_name}")
        if req.status_code == 200:
            jason = json.loads(req.content, object_hook=lambda d: SimpleNamespace(**d))
        else:
            #TODO: Control request/response errors
            jason = None
        return jason
    
    def price_by_name(name):
        """
        Returns the price of a card in euros
        """
        formated_name = scryfall_api.parse_name(name)
        return scryfall_api.card_by_name(formated_name).prices.eur

    def search_by_name(name):
        """
        Search for a card by its name 
        TODO: This method should allow parameters such as mana cost, text in card, etc. 
        """
        formated_name = scryfall_api.parse_name(name)
        req = requests.get(f"https://api.scryfall.com/cards/search?order=released&include_multilingual=true&unique=prints&q=!{formated_name}")
        if req.status_code == 404:
            req = requests.get(f"https://api.scryfall.com/cards/search?order=released&include_multilingual=true&unique=prints&q={formated_name}")
        jason = json.loads(req.content, object_hook=lambda d: SimpleNamespace(**d))
        return jason
        
    def version_prices(name):
        """
        Returns a dataframe with the name and price of each printing of the requested card for both foil and non-foil versions
        TODO: Try to implement cardmarket's API or somehow extract real time prices from cardmarket 
        """
        versions = scryfall_api.search_by_name(name)
        dataframe = pd.DataFrame(columns=['Card Name', 'version', 'price', 'price foil'])
        for v in versions.data:
            dataframe.loc[v.collector_number] = [v.name, v.set, v.prices.eur, v.prices.eur_foil]
            dataframe.reset_index()
        return dataframe