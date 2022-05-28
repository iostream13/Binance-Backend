import imp
from statistics import mode
from sqlalchemy import Interval, and_, asc, or_, not_, desc, asc, func
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import sys
import math
import json


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
    db_balance = db.query(models.UserBalance).filter(and_(models.UserBalance.username == username, models.UserBalance.tokenname == tokenname)).first()
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
     #return db_order
     

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
    user: models.UserBalance = db.query(models.UserBalance).filter(and_(models.UserBalance.username == username, models.UserBalance.tokenname == token)).first()
    if user is None or user.amount < amount:
        return "NO"
    return "OK"

def order(db: Session, market_order: schemas.MarketOrder):
    market: models.Market = db.query(models.Market).filter(models.Market.marketid == market_order.marketid).first()
    token1 = market.token1
    token2 = market.token2
    ok = "YES"
    if market_order.orderaction == Action.BUY:
        ok = check_balance(db, market_order.username, token2, market_order.remainamount)
    else:
        ok = check_balance(db, market_order.username, token1, market_order.remainamount)
    if ok == "NO":
        return None
    db_order = models.MarketOrder(username=market_order.username, marketid=market_order.marketid,
                                  orderaction=market_order.orderaction.value, totalamount=market_order.totalamount, remainamount=market_order.remainamount, price=market_order.price)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    print("orderid: ")
    print(db_order.marketorderid)
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
    print("hjhjhj")
    now = datetime.utcnow()
    db_order = models.OrderHistory(marketorderid=marketorderid, marketid=marketid,
                                   amount=amount, orderedat=now)
    db.add(db_order)
    db.commit()
    print("okay")


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
    print(check1)
    print(check2)
    if check1 == "NO" or check2 == "NO":
        print("ddd")
        return "NO"
    
    increase_user_token_balance(
        db, order_buy.username, token2, -amount_deal * order_buy.price)
    increase_user_token_balance(
        db, order_sell.username, token1, -amount_deal)
    increase_user_token_balance(
        db, order_buy.username, token1, amount_deal)
    increase_user_token_balance(
        db, order_sell.username, token2, amount_deal * order_sell.price)
    
    create_order_history(db, market.marketid, order_buy.marketorderid, amount_deal)
    create_order_history(db, market.marketid, order_sell.marketorderid, amount_deal)
    
    db.query(models.MarketOrder).filter(models.MarketOrder.marketorderid == order_buy.marketorderid).update({"remainamount": order_buy.remainamount - amount_deal})
    db.commit()
    db.query(models.MarketOrder).filter(models.MarketOrder.marketorderid == order_sell.marketorderid).update({"remainamount": order_sell.remainamount - amount_deal})
    db.commit()

def relax_market(db: Session, token1: str, token2: str):
    #print("hjhj")
    market: models.Market = find_market(db, token1, token2)
    while 1 > 0:
        sell: models.MarketOrder = db.query(models.MarketOrder).filter(and_(
            models.MarketOrder.marketid == market.marketid, models.MarketOrder.orderaction == Action.SELL, models.MarketOrder.remainamount > 0)).order_by(asc(models.MarketOrder.price)).first()
        buy: models.MarketOrder = db.query(models.MarketOrder).filter(and_(
            models.MarketOrder.marketid == market.marketid, models.MarketOrder.orderaction == Action.BUY, models.MarketOrder.remainamount > 0)).order_by(desc(models.MarketOrder.price)).first()
        if sell is None or buy is None or sell.price > buy.price:
            break
        if sell.username == buy.username:
            continue
        deal(db, buy, sell)

def get_order_buy(db: Session, market: models.Market):
    return db.query(models.MarketOrder).filter(and_(models.MarketOrder.marketid == market.marketid, models.MarketOrder.orderaction == Action.BUY, models.MarketOrder.remainamount > 0)).all()

def get_order_sell(db: Session, market: models.Market):
    return db.query(models.MarketOrder).filter(and_(models.MarketOrder.marketid == market.marketid, models.MarketOrder.orderaction == Action.SELL, models.MarketOrder.remainamount > 0)).all()
    
#check
def get_order_history(db: Session, market: models.Market):
    #return market.listmarkethistory
    return db.query(models.OrderHistory).filter(models.OrderHistory.marketid == market.marketid).order_by(desc(models.OrderHistory.orderhistoryid)).all()

#get my order
def get_my_order(db: Session, market: models.Market, username: str):
    historydata: models.OrderHistory = db.query(models.OrderHistory).filter(models.OrderHistory.marketid == market.marketid).order_by(desc(models.OrderHistory.orderhistoryid)).all()
    myorder = []
    for history in historydata:
        orderdata: models.MarketOrder = db.query(models.MarketOrder).filter(models.MarketOrder.marketorderid == history.orderhistoryid).first()
        if orderdata is None: 
            continue
        if orderdata.username == username:
            myorder.append(orderdata)
    return myorder

#get last price
def get_last_price(db: Session, market: models.Market):
    historydata: models.OrderHistory = db.query(models.OrderHistory).filter(models.OrderHistory.marketid == market.marketid).order_by(desc(models.OrderHistory.orderhistoryid)).first()
    orderdata: models.MarketOrder = db.query(models.MarketOrder).filter(models.MarketOrder.marketorderid == historydata.marketorderid).first()
    if orderdata.orderaction == Action.BUY:
        return {"BUY", orderdata.price}
    return {"SELL", orderdata.price}
 
#24h volume
def get_24h_volume(db: Session, market: models.Market):
    timee = datetime.utcnow() - timedelta(hours=24)
    historydata: models.OrderHistory = db.query(models.OrderHistory).filter(and_(models.OrderHistory.marketid == market.marketid, models.OrderHistory.orderedat >= timee)).order_by(desc(models.OrderHistory.orderhistoryid)).first()
    sum = 0
    for order in historydata:
        sum = sum + order.amount
    return sum

#24h low
def get_24h_low(db: Session, market: models.Market):
    timee = datetime.utcnow() - timedelta(hours=24)
    historydata: models.OrderHistory = db.query(models.OrderHistory).filter(and_(models.OrderHistory.marketid == market.marketid, models.OrderHistory.orderedat >= timee)).all()
    low = sys.float_info.max
    for order in historydata:
        orderdata: models.MarketOrder = db.query(models.MarketOrder).filter(models.MarketOrder.marketorderid == order.marketorderid).first()
        if orderdata.orderaction == Action.SELL:
            low = min(low, orderdata.price)
    return low

#24h high
def get_24h_high(db: Session, market: models.Market):
    timee = datetime.utcnow() - timedelta(hours=24)
    historydata: models.OrderHistory = db.query(models.OrderHistory).filter(and_(models.OrderHistory.marketid == market.marketid, models.OrderHistory.orderedat >= timee)).all()
    high = 0
    for order in historydata:
        orderdata: models.MarketOrder = db.query(models.MarketOrder).filter(models.MarketOrder.marketorderid == order.marketorderid).first()
        if orderdata.orderaction == Action.SELL:
            high = max(high, orderdata.price)
    return high

def check_order(db: Session, market_order_id: int):
    return db.query(models.MarketOrder).filter(models.MarketOrder.marketorderid == market_order_id).first()
    
def chart(db: Session, market: models.Market):
    tsnow = datetime.timestamp(datetime.utcnow())
    timee = math.floor(tsnow / 3600)
    timee = timee * 3600
    historydata = db.query(models.OrderHistory).filter(and_(models.OrderHistory.marketid == market.marketid, models.OrderHistory.orderedat >= timee)).order_by(desc(models.OrderHistory.orderhistoryid)).all()
    open = db.query(models.OrderHistory).filter(and_(models.OrderHistory.marketid == market.marketid, models.OrderHistory.orderedat >= timee)).order_by(asc(models.OrderHistory.orderhistoryid)).first()
    close = db.query(models.OrderHistory).filter(and_(models.OrderHistory.marketid == market.marketid, models.OrderHistory.orderedat >= timee)).order_by(desc(models.OrderHistory.orderhistoryid)).first()
    low = sys.float_info.max
    high = 0
    for order in historydata:
        orderdata: models.MarketOrder = db.query(models.MarketOrder).filter(models.MarketOrder.marketorderid == order.marketorderid).first()
        if orderdata.orderaction == Action.SELL:
            low = min(low, orderdata.price)
            high = max(high, orderdata.price)
    a_file = open("datachart.json", "r")
    json_object = json.load(a_file)
    a_file.close()
    last_element = json_object[-1]
    if last_element['time'] == timee:
        last_element['open'] = open 
        last_element['close'] = close
        last_element['low'] = low 
        last_element['high'] = high
        json_object[-1] = last_element 
    else:
        json_object.append({
            "time": timee,
            "open": open,
            "close": close,
            "high": high,
            "low": low})
    a_file = open("datachart.json", "w")
    json.dump(json_object, a_file, indent=4)
    a_file.close()
        
    