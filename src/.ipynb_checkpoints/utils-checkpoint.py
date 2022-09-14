import requests

import pandas as pd

ETH_URL = 'https://api.ethplorer.io/getAddressInfo/{}?apiKey=freekey'


def get_eth_json_obj(wallet_id):
    try:
        json_obj = requests.get(ETH_URL.format(wallet_id)).json()
    except Exception as e:
        json_obj = {}
        print(e)
    return json_obj       

def json_to_df(json_obj):
    temp_token = json_obj['tokens']
    temp_token = pd.json_normalize(temp_token)
    temp_df = pd.json_normalize(json_obj)
    temp_df = pd.concat([temp_df] * temp_token.shape[0]).reset_index(drop=True).drop(columns=['tokens'])
    temp_df.loc[temp_token.index, temp_token.columns] = temp_token
    return temp_df
