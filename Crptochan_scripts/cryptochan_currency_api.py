from Crptochan_scripts.cryptochan_curreny_literals import FiatCode
from pycoingecko import CoinGeckoAPI
import pandas as pd

cg = CoinGeckoAPI()


def GET_CURRENCIES():
    currency = cg.get_supported_vs_currencies()
    df = pd.DataFrame(currency)
    df.rename(columns={0: 'Currency'}, inplace=True)
    value = df['Currency'].to_list()
    key = df['Currency'].str.upper().to_list()
    currency_dict = dict(zip(key, value))
    print(currency_dict)
    # print(DF['Currency'])
    return currency_dict


if __name__ == '__main__':
    GET_CURRENCIES()
