from hashlib import new
import json 

f = open("coingecko.json")
data = json.load(f)
#need:
# "symbol": "btc",
# "name": "Bitcoin",
# "image": "https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1547033579",
# "current_price": 47012,
# "market_cap": 893095842948,
# "total_supply": 21000000.0,
# "max_supply": 21000000.0,


new_tokens = []
for token in data:
    new_tokens.append({
        "TokenName": token['name'],
        "TokenSymbol": token['symbol'],
        "TokenImage": token['image'],
        "MarketCap": token['market_cap'],
        "TotalSupply": token['total_supply'],
        "MaxSupply": token['max_supply'],
        "CoingeckoPrice": token['current_price']
    })

h = open('coingecko_final.json', 'w')

json.dump(new_tokens, h, indent=4)
h.close()
