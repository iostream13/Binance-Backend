import imp
from statistics import mode
from sqlalchemy.orm import Session
from . import models, schemas
import json
from .models import Action


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

def create_balance(db: Session, username: str, tokenname: str, amount: float):
    db_userbalance = models.UserBalance(
        username=username, tokenname=tokenname, amount = amount)
    db.add(db_userbalance)
    db.commit()
    db.refresh(db_userbalance)
    return db_userbalance

def create_user(db: Session, user: schemas.UserCreate):
    bio = ""
    if user.userbio is not None:
        bio = user.userbio
    db_user = models.User(username=user.username,
                          password=user.password, userbio=bio)
    create_balance(db, user.username, tokenname="Bitcoin", amount=13.08)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def find_token(db: Session, token: str):
    data_token = db.query(models.Token).filter(models.Token.tokenname == token).first()
    return data_token


def sort_tokens(token1: str, token2: str):
    if token1 > token2:
        token1, token2 = token2, token1
    return token1, token2

tokens = ["bitcoin", "ethereum", "tether", "bnb", "usd coin"]

def check_market(db: Session, token1: str, token2: str):
    if token1 not in tokens and token2 not in tokens:
        return "NO"
    return "ok"

def find_market(db: Session, token1: str, token2: str):
    token1, token2 = sort_tokens(token1, token2)
    db_market = db.query(models.Market).filter(
        models.Market.token1 == token1 and models.Market.token2 == token2).first()
    return db_market.marketid


def order(db: Session, market_order: schemas.MarketOrder):
    db_order = models.MarketOrder(username=market_order.username, marketid=market_order.marketid,
                                  orderaction=market_order.orderaction.value, totalamount=market_order.totalamount, remainamount=market_order.remainamount, price=market_order.price)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def deal(db: Session, order_id_buy: int, order_id_sell: int):
    order_buy = db.query(models.MarketOrder).filter(models.MarketOrder.marketorderid == order_id_buy).first()
    order_sell = db.query(models.MarketOrder).filter(models.MarketOrder.marketorderid == order_id_sell).first()
    market = db.query(models.Market).filter(models.Market.marketid == order_buy.marketid).first()
    token1 = market.token1
    token2 = market.token2
    user_buy = db.query(models.UserBalance).filter(models.UserBalance.username == order_buy.username).all()
    user_sell = db.query(models.UserBalance).filter(models.UserBalance.username == order_sell.username).all()
    ok = 0
    for balance in user_buy:
        if balance.tokenname == token2:
            ok = 1
    
    

def relax_market(db: Session, token1: str, token2: str):
    if check_market(db, token1, token2) == "OK":
        market_id = find_market(token1, token2)
        list_sell = db.query(models.MarketOrder).filter(models.MarketOrder.orderaction == Action.SELL).all()
        list_buy = db.query(models.MarketOrder).filter(models.MarketOrder.orderaction == Action.BUY).all()
        ok = 0
        for obuy in list_buy:
            for osell in list_sell:
                if obuy.price > osell.price:
                    ok = 1
                    
                
        
def test(db: Session, token1: str, token2: str):
    print("YESSSS")
    token1, token2 = sort_tokens(token1, token2)
    db_market = db.query(models.Market).filter(
        models.Market.token1 == token1 and models.Market.token2 == token2).first()
    if db_market is None:
        print("NO")
    return db_market.marketid
