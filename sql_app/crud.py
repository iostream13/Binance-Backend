import imp
from lib2to3.pgen2.token import OP
from statistics import mode
from time import time
from sqlalchemy import Interval, and_, asc, false, or_, not_, desc, asc, func, true
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from pathlib import Path
import sys
import math
import json
import random


from . import models, schemas
from .models import Action, UserBalance


def get_user_by_name(db: Session, user_name: str):
    return db.query(models.User).filter(models.User.username == user_name).first()


def get_user_balance_by_name(db: Session, user_name: str):
    return db.query(models.User.balanceuser).filter(models.User.username == user_name).first()


def get_user_balance_by_name_and_token(db: Session, user_name: str):
    # data = db.query(models.Token).offset(0).limit(100).all()
    # res = []
    # for token in data:
    #     token_name = token.tokenname
    #     t = []
    #     t.append(token_name)
    #     t.append(db.query(models.UserBalance).filter(models.UserBalance.username == user_name and models.UserBalance.token == token_name).first())
    #     res.append(t)
    return db.query(models.UserBalance).filter(models.UserBalance.username == user_name).all()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_tokens(db: Session):
    return db.query(models.Token).all()


def get_order_buy(db: Session, market: models.Market):
    return db.query(models.MarketOrder).filter(and_(models.MarketOrder.marketid == market.marketid, models.MarketOrder.orderaction == Action.BUY)).all()


def get_order_sell(db: Session, market: models.Market):
    return db.query(models.MarketOrder).filter(and_(models.MarketOrder.marketid == market.marketid, models.MarketOrder.orderaction == Action.SELL)).all()


def get_markets(db: Session):
    return db.query(models.Market).all()


def create_balance(db: Session, username: str, tokenname: str, amount: float):
    db_balance = db.query(models.UserBalance).filter(and_(
        models.UserBalance.username == username, models.UserBalance.tokenname == tokenname)).first()
    if db_balance is None:
        db_userbalance = models.UserBalance(
            username=username, tokenname=tokenname, amount=amount)
        db.add(db_userbalance)
        db.commit()
        db.refresh(db_userbalance)
        return db_userbalance
    return db_balance


def create_user(db: Session, user: schemas.UserCreate):
    bio = ""
    if user.userbio is not None:
        bio = user.userbio
    db_user = models.User(username=user.username,
                          password=user.password, userbio=bio)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    create_balance(db, user.username, tokenname="Bitcoin", amount=500)
    return db_user


def find_token(db: Session, token: str):
    data_token = db.query(models.Token).filter(
        models.Token.tokenname == token).first()
    return data_token


def sort_tokens(token1: str, token2: str):
    if token1 > token2:
        token1, token2 = token2, token1
    return token1, token2


def get_order(db: Session, orderid: int):
    return db.query(models.MarketOrder).filter(models.MarketOrder.marketorderid == orderid).first()
    # return db_order


tokens = ["bitcoin", "ethereum", "tether", "bnb", "usd coin"]


def check_market(db: Session, token1: str, token2: str):
    if token1 not in tokens and token2 not in tokens:
        return "NO"
    return "ok"


def find_market(db: Session, token1: str, token2: str):
    token1, token2 = sort_tokens(token1, token2)
    db_market = db.query(models.Market).filter(
        and_(models.Market.token1 == token1, models.Market.token2 == token2)).first()
    return db_market


def check_balance(db: Session, username: str, token: str, amount: float):
    user: models.UserBalance = db.query(models.UserBalance).filter(and_(
        models.UserBalance.username == username, models.UserBalance.tokenname == token)).first()
    if user is None or user.amount < amount:
        return "NO"
    return "OK"


def order(db: Session, market_order: schemas.MarketOrder):
    market: models.Market = db.query(models.Market).filter(
        models.Market.marketid == market_order.marketid).first()
    token1 = market.token1
    token2 = market.token2
    ok = "YES"
    if market_order.orderaction == Action.BUY:
        ok = check_balance(db, market_order.username,
                           token2, market_order.remainamount)
    else:
        ok = check_balance(db, market_order.username,
                           token1, market_order.remainamount)
    if ok == "NO":
        return None
    db_order = models.MarketOrder(username=market_order.username, marketid=market_order.marketid,
                                  orderaction=market_order.orderaction.value, totalamount=market_order.totalamount, remainamount=market_order.remainamount, price=market_order.price)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def increase_user_token_balance(db: Session, username: str, token: str, delta: float):
    balance: models.UserBalance = db.query(models.UserBalance).filter(and_(
        models.UserBalance.username == username, models.UserBalance.tokenname == token)).first()
    if balance is None:
        if delta < 0:
            return "NO"
        balance = create_balance(db, username, token, delta)
    else:
        if balance.amount + delta < 0:
            return "NO"
        db.query(models.UserBalance).filter(and_(
            models.UserBalance.username == username, models.UserBalance.tokenname == token)).update({"amount": balance.amount + delta})
        db.commit()
    return "OK"


def create_order_history(db: Session, marketid: int, marketorderid: int, amount: float):
    now = datetime.utcnow()
    db_order = models.OrderHistory(marketorderid=marketorderid, marketid=marketid,
                                   amount=amount, orderedat=now)
    db.add(db_order)
    db.commit()
    return "OK"


def deal(db: Session, order_buy: models.MarketOrder, order_sell: models.MarketOrder):
    assert order_buy.marketid == order_sell.marketid
    assert order_buy.price >= order_sell.price
    market: models.Market = db.query(models.Market).filter(
        models.Market.marketid == order_buy.marketid).first()
    token1 = market.token1
    token2 = market.token2
    amount_deal = min(order_buy.remainamount, order_sell.remainamount)
    check1 = check_balance(db, order_buy.username, token2, amount_deal)
    check2 = check_balance(db, order_sell.username, token1, amount_deal)
    if check1 == "NO" or check2 == "NO":
        return "NO"

    increase_user_token_balance(
        db, order_buy.username, token2, -amount_deal * order_buy.price)
    increase_user_token_balance(
        db, order_sell.username, token1, -amount_deal)
    increase_user_token_balance(
        db, order_buy.username, token1, amount_deal)
    increase_user_token_balance(
        db, order_sell.username, token2, amount_deal * order_sell.price)

    create_order_history(db, market.marketid,
                         order_buy.marketorderid, amount_deal)
    create_order_history(db, market.marketid,
                         order_sell.marketorderid, amount_deal)

    db.query(models.MarketOrder).filter(models.MarketOrder.marketorderid ==
                                        order_buy.marketorderid).update({"remainamount": order_buy.remainamount - amount_deal})
    db.commit()
    db.query(models.MarketOrder).filter(models.MarketOrder.marketorderid ==
                                        order_sell.marketorderid).update({"remainamount": order_sell.remainamount - amount_deal})
    db.commit()


def relax_market(db: Session, token1: str, token2: str):
    market: models.Market = find_market(db, token1, token2)
    while 1 > 0:
        sell: models.MarketOrder = db.query(models.MarketOrder).filter(and_(
            models.MarketOrder.marketid == market.marketid, models.MarketOrder.orderaction == Action.SELL, models.MarketOrder.remainamount > 0)).order_by(asc(models.MarketOrder.price)).first()
        if sell is None:
            break
        buy: models.MarketOrder = db.query(models.MarketOrder).filter(and_(
            models.MarketOrder.marketid == market.marketid, models.MarketOrder.orderaction == Action.BUY, models.MarketOrder.remainamount > 0, models.MarketOrder.username != sell.username)).order_by(desc(models.MarketOrder.price)).first()
        if buy is None or sell.price > buy.price or sell.marketorderid == buy.marketorderid:
            break
        if sell.username == buy.username:
            continue
        deal(db, buy, sell)


def get_order_buy(db: Session, market: models.Market):
    return db.query(models.MarketOrder).filter(and_(models.MarketOrder.marketid == market.marketid, models.MarketOrder.orderaction == Action.BUY, models.MarketOrder.remainamount > 0)).all()


def get_order_sell(db: Session, market: models.Market):
    return db.query(models.MarketOrder).filter(and_(models.MarketOrder.marketid == market.marketid, models.MarketOrder.orderaction == Action.SELL, models.MarketOrder.remainamount > 0)).all()



def get_order_history(db: Session, market: models.Market):
    # return market.listmarkethistory
    return db.query(models.OrderHistory).filter(models.OrderHistory.marketid == market.marketid).order_by(desc(models.OrderHistory.orderhistoryid)).all()



def get_my_order(db: Session, market: models.Market, username: str):
    historydata: models.OrderHistory = db.query(models.OrderHistory).filter(
        models.OrderHistory.marketid == market.marketid).order_by(desc(models.OrderHistory.orderhistoryid)).all()
    myorder = []
    for history in historydata:
        orderdata: models.MarketOrder = db.query(models.MarketOrder).filter(
            models.MarketOrder.marketorderid == history.orderhistoryid).first()
        if orderdata is None:
            continue
        if orderdata.username == username:
            myorder.append(orderdata)
    return myorder



def get_last_price(db: Session, market: models.Market):
    historydata: models.OrderHistory = db.query(models.OrderHistory).filter(
        models.OrderHistory.marketid == market.marketid).order_by(desc(models.OrderHistory.orderhistoryid)).first()
    if historydata is None:
        return "history data is null"
    orderdata: models.MarketOrder = db.query(models.MarketOrder).filter(
        models.MarketOrder.marketorderid == historydata.marketorderid).first()
    if orderdata.orderaction == Action.BUY:
        return {"BUY", orderdata.price}
    return {"SELL", orderdata.price}



def get_24h_volume(db: Session, market: models.Market):
    timee = datetime.utcnow() - timedelta(hours=24)
    historydata: models.OrderHistory = db.query(models.OrderHistory).filter(and_(
        models.OrderHistory.marketid == market.marketid, models.OrderHistory.orderedat >= timee)).order_by(desc(models.OrderHistory.orderhistoryid)).all()
    if historydata is None:
        return "history data is null"
    sum = 0
    for order in historydata:
        orderdata: models.MarketOrder = db.query(models.MarketOrder).filter(
            models.MarketOrder.marketorderid == order.marketorderid).first()
        if orderdata.orderaction == Action.SELL:
            sum = sum + order.amount
    return sum



def get_24h_low(db: Session, market: models.Market):
    timee = datetime.utcnow() - timedelta(hours=24)
    historydata: models.OrderHistory = db.query(models.OrderHistory).filter(and_(
        models.OrderHistory.marketid == market.marketid, models.OrderHistory.orderedat >= timee)).all()
    if historydata is None:
        return "history data is null"
    low = sys.float_info.max
    for order in historydata:
        orderdata: models.MarketOrder = db.query(models.MarketOrder).filter(
            models.MarketOrder.marketorderid == order.marketorderid).first()
        if orderdata.orderaction == Action.SELL:
            low = min(low, orderdata.price)
    return low


def get_24h_high(db: Session, market: models.Market):
    timee = datetime.utcnow() - timedelta(hours=24)
    historydata: models.OrderHistory = db.query(models.OrderHistory).filter(and_(
        models.OrderHistory.marketid == market.marketid, models.OrderHistory.orderedat >= timee)).all()
    if historydata is None:
        return "history data is null"
    high = 0
    for order in historydata:
        orderdata: models.MarketOrder = db.query(models.MarketOrder).filter(
            models.MarketOrder.marketorderid == order.marketorderid).first()
        if orderdata.orderaction == Action.SELL:
            high = max(high, orderdata.price)
    return high


def check_order(db: Session, market_order_id: int):
    return db.query(models.MarketOrder).filter(models.MarketOrder.marketorderid == market_order_id).first()


def chart(db: Session, market: models.Market):
    tsnow = datetime.timestamp(datetime.utcnow())
    timee = math.floor(tsnow / 3600)
    timee = timee * 3600
    time_open = datetime.utcfromtimestamp(timee)
    historydata = db.query(models.OrderHistory).filter(and_(models.OrderHistory.marketid == market.marketid,
                                                            models.OrderHistory.orderedat >= time_open)).order_by(desc(models.OrderHistory.orderhistoryid)).all()
    if historydata is None:
        return "history data is null"
    history_open: models.OrderHistory = db.query(models.OrderHistory).filter(and_(
        models.OrderHistory.marketid == market.marketid, models.OrderHistory.orderedat >= time_open)).order_by(asc(models.OrderHistory.orderedat)).all()
    if history_open is None:
        return "history data is null"
    data_open: models.MarketOrder = None
    for order in history_open:
        orderdata: models.MarketOrder = db.query(models.MarketOrder).filter(
            models.MarketOrder.marketorderid == order.marketorderid).first()
        if orderdata.orderaction == Action.SELL:
            data_open = orderdata
            break
    if data_open is None:
        return "history data is null"
    Open = data_open.price
    history_close: models.OrderHistory = db.query(models.OrderHistory).filter(and_(models.OrderHistory.marketid == market.marketid,
                                                                                   models.OrderHistory.orderedat >= time_open)).order_by(desc(models.OrderHistory.orderedat)).all()
    if history_close is None:
        return "history data is null"
    data_close: models.MarketOrder = None
    for order in history_close:
        orderdata: models.MarketOrder = db.query(models.MarketOrder).filter(
            models.MarketOrder.marketorderid == order.marketorderid).first()
        if orderdata.orderaction == Action.SELL:
            data_close = orderdata
            break
    if data_close is None:
        return "history data is null"
    close = data_close.price
    low = sys.float_info.max
    high = 0
    for order in historydata:
        orderdata: models.MarketOrder = db.query(models.MarketOrder).filter(
            models.MarketOrder.marketorderid == order.marketorderid).first()
        if orderdata.orderaction == Action.SELL:
            low = min(low, orderdata.price)
            high = max(high, orderdata.price)
    script_location = Path(__file__).absolute().parent
    file_location = script_location / 'datachart.json'
    a_file = open(file_location, 'r')
    json_object = json.load(a_file)
    a_file.close()
    have_market_chart = false
    market_name = market.token1 + "-" + market.token2
    for martket_chart in json_object:
        if martket_chart['market'] == market_name:
            have_market_chart = true
            chartdata = martket_chart['data']
            last_element = chartdata[-1]
            if last_element['time'] == timee:
                last_element['open'] = Open
                last_element['close'] = close
                last_element['low'] = low
                last_element['high'] = high
                chartdata[-1] = last_element
                martket_chart['data'] = chartdata
            else:
                martket_chart['data'].append({
                    "time": timee,
                    "open": Open,
                    "close": close,
                    "high": high,
                    "low": low})
            break
    if have_market_chart == false:
        data = []
        data.append({
            "time": timee,
            "open": Open,
            "close": close,
            "high": high,
            "low": low})
        json_object.append({"market": market_name, "data": data})
    
    a_file = open(file_location, 'w')
    json.dump(json_object, a_file, indent=4)
    a_file.close()
    return "OK"


def get_full_data_market(db: Session):
    script_location = Path(__file__).absolute().parent
    file_location = script_location / 'datachart.json'
    a_file = open(file_location, 'r')
    json_object = json.load(a_file)
    a_file.close()
    full_data = []
    market_used = []
    for mk in json_object:
        tk = mk['market'].split("-")
        token1 = tk[0]
        token2 = tk[1]
        market: models.Market = find_market(db, token1, token2)
        data = mk['data']
        timee = datetime.timestamp(datetime.utcnow()) - 86400
        print(timee)
        Open = 0.0
        close = 0.0
        data_24h = []
        for d in data[::-1]:     
               if d['time'] < timee:
                   break
               data_24h.append(d)
        if len(data_24h) == 0:
            continue
        market_used.append(mk['market'])
        close = data_24h[0]['close']
        Open = data_24h[-1]['open']
        state = "INC"
        if close < Open:
            state = "DEC"
        full_data.append({"token1": token1, "token2": token2, "high": get_24h_high(db, market), "low": get_24h_low(db, market) , "volume": get_24h_volume(db, market), "lastprice": close, "state": state})
    
        
    data_market = db.query(models.Market).all()
    
    for m in data_market:
        market: models.Market = m
        market_name = market.token1 + "-" + market.token2
        if market_name in market_used:
            continue
        close = random.randint(70, 160) + random.random()
        Open = random.randint(70, 160) + random.random()
        state = "INC"
        if close < Open:
            state = "DEC"
        high = random.randint(170, 200) + random.random()
        low = random.randint(20, 60) + random.random()
        
        volume = random.randint(1000000, 1000000000) + random.random()
        full_data.append({"token1": market.token1, "token2": market.token2, "high": high, "low": low, "volume": volume, "lastprice": close, "state": state})
    return full_data
        
def get_datachart(db: Session):
    script_location = Path(__file__).absolute().parent
    file_location = script_location / 'datachart.json'
    a_file = open(file_location, 'r')
    json_object = json.load(a_file)
    a_file.close()
    return json_object
        
        