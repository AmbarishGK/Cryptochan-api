from flask import Flask, jsonify
from Crptochan_scripts.cryptochan_coins_api import Coins, GET_COINS

app = Flask(__name__)


@app.route('/')
def crypto_world():
    return 'Welcome to Crypto World! I am your CryptoChan, here to help you with your crypto power'


@app.route('/coinlist', methods=['GET'])
def Coin_list():
    coins = GET_COINS()
    return jsonify(coins)


@app.route('/BTC', methods=['GET'])
def Bitcoin():
    btc = Coins().GET_BTC()
    return btc


if __name__ == '__main__':
    app.run()
