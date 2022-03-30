import mysql.connector
import json 

mydb = mysql.connector.connect(
    host = "localhost",
    port=3306,
    user="root",
    password="hien1308",
    database="Binance"
)

f = open("coingecko_final.json")
data = json.load(f)

mycursor = mydb.cursor()

sql = "INSERT INTO Token (TokenName, TokenSymbol, TokenImage, MarketCap, TotalSupply, MaxSupply, CoingeckoPrice) VALUES (%s, %s, %s, %s, %s, %s, %s)"

for token in data:
    t_supply = token['TotalSupply']
    m_supply = token['MaxSupply']
    if t_supply is None and m_supply is None:
        t_supply = token['MarketCap'] / token['CoingeckoPrice']
        m_supply = t_supply
    if m_supply is None:
        m_supply = t_supply
    if t_supply is None:
        t_supply = m_supply
    val = (token['TokenName'], 
           token['TokenSymbol'], 
           token['TokenImage'], 
           token['MarketCap'], 
           t_supply, 
           m_supply, 
           token['CoingeckoPrice'])
    mycursor.execute(sql, val)
    
mydb.commit()