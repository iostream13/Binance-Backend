import mysql.connector
import json 

mydb = mysql.connector.connect(
    host = "localhost",
    port=3306,
    user="root",
    password="hien1308",
    database="Binance"
)

f = open("../crawl and import data/coingecko_final.json")
data = json.load(f)

mycursor = mydb.cursor()

sql = "INSERT INTO Market (Token1, Token2) VALUES (%s, %s)"

x = len(data)

for id1 in range(0, 5):
    token = data[id1]['TokenName']
    for id2 in range(id1 + 1, x):
        token1 = token
        token2 = data[id2]['TokenName']
        if token1.lower() > token2.lower():
            tmp = token1
            token1 = token2
            token2 = tmp
        val = (token1, token2)
        mycursor.execute(sql, val)

mydb.commit()