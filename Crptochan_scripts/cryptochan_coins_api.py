from pycoingecko import CoinGeckoAPI
import pandas as pd
from Crptochan_scripts.cryptochan_coin_literals import CoinCode
from Crptochan_scripts.cryptochan_curreny_literals import FiatCode
from Crptochan_scripts.cryptochan_currency_api import GET_CURRENCIES

cg = CoinGeckoAPI()


def GET_COINS():
    coins = cg.get_coins_list()
    df = pd.DataFrame(coins)
    df.set_index('id', inplace=True)
    print(df)
    return coins


class Coins:
    def __init__(self):
        self.BTC = CoinCode.BTC
        self.Currency = GET_CURRENCIES()
        self.USD = self.Currency['USD']
        self.INR = self.Currency['INR']
        return

    def GET_BTC(self):
        btc = cg.get_price(ids=self.BTC, vs_currencies=self.INR)
        print(btc)
        return btc


if __name__ == '__main__':
    GET_COINS()
