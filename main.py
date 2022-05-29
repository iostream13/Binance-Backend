import email
import imp
from lib2to3.pgen2 import token
from telnetlib import STATUS
from typing import List

from fastapi import Depends, FastAPI, Query, Body, status, Form, File, UploadFile, HTTPException, Request
from typing import List, Optional, Set
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse, PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from sqlalchemy.orm import Session

from sql_app import crud, models, schemas
from sql_app.database import SessionLocal, engine 
from sql_app.models import Action

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.get("/")
def show():
    return "hello"

@app.post("/user/", response_model=schemas.UserInfor)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, user_name=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="username already registered")
    return crud.create_user(db, user)

@app.post("/user/addbalance/{user}")
def create_balance(user: str, token: str, amount: float, db: Session = Depends(get_db)):
    user_db = crud.get_user_by_name(db, user)
    if user_db is None:
        raise HTTPException(status_code=404, detail="user not found")
        return None
    token_db = crud.find_token(db, token)
    if token_db is None:
        raise HTTPException(status_code=404, detail="token not found")
        return None
    if amount < 0: 
        raise HTTPException(status_code=400, detail="Bad request! Amount must be positive!")
        return None
    return crud.create_balance(db, user, token, amount)

@app.get("/users/", response_model=List[schemas.UserInfor])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip, limit)
    return users 

@app.get("/user/{user_name}")
def read_user(user_name: str, db: Session = Depends(get_db)):
    user = crud.get_user_by_name(db, user_name)
    if user is None:
        raise HTTPException(status_code=404, detail="user not found")
    balance = crud.get_user_balance_by_name_and_token(db, user_name)
    # res = []
    # res.append(user)
    # res.append(balance)
    return balance

@app.get("/user/password/{user_name}")
def read_password_user(user_name: str, db: Session = Depends(get_db)):
    user: models.User = crud.get_user_by_name(db, user_name)
    if user is None:
        raise HTTPException(status_code=404, detail="user not found")
    return user.password

class order_model(BaseModel):
    username: str = ""
    token1: str = ""
    token2: str = ""
    orderaction: Action
    totalamount: float 
    price: float
    
@app.post("/order/")
def create_order(order: order_model, db: Session = Depends(get_db)):
    user = crud.get_user_by_name(db, order.username)
    ok = 1
    if user is None:
        ok = 0
        raise HTTPException(status_code=400, detail="Bad request. User not found")
    t1 = crud.find_token(db, order.token1)
    t2 = crud.find_token(db, order.token2)
    if t1 is None or t2 is None:
        ok = 0
        raise HTTPException(status_code=400, detail="Bad request. Token not found!")
    order.token1 = order.token1.lower()
    order.token2 = order.token2.lower()
    if crud.check_market(db, order.token1, order.token2) == "NO":
        ok = 0
        raise HTTPException(status_code=400, detail="Bad request. Market not found")
    market: models.Market = crud.find_market(db, order.token1, order.token2)
    if ok == 1:
        ordermodel = schemas.MarketOrder
        ordermodel.username = order.username
        ordermodel.marketid = market.marketid
        ordermodel.orderaction = order.orderaction
        ordermodel.totalamount = order.totalamount
        ordermodel.remainamount = order.totalamount
        ordermodel.price = order.price
        a = crud.order(db, ordermodel)
        if a is None:
            raise HTTPException(status_code=400, detail="Bad request. Balance isn't enough")
            return a
        crud.relax_market(db, order.token1, order.token2)
        return a
    
@app.post("/update_user/", status_code = status.HTTP_201_CREATED)
def update(username: str, bio: str, db: Session = Depends(get_db)):
    db.query(models.User).filter(models.User.username == username).update({"userbio": bio})
    db.commit()
    
@app.get("/chart/")
def chart(token1: str, token2: str, db: Session = Depends(get_db)):
    t1 = crud.find_token(db, token1)
    t2 = crud.find_token(db, token2)
    if t1 is None or t2 is None:
        ok = 0
        raise HTTPException(status_code=400, detail="Bad request. Token not found!")
    token1 = token1.lower()
    token2 = token2.lower()
    if crud.check_market(db, token1, token2) == "NO":
        ok = 0
        raise HTTPException(status_code=400, detail="Bad request. Market not found")
    market: models.Market = crud.find_market(db, token1.lower(), token2.lower())
    if market is None:
        raise HTTPException(status_code=400, detail="Bad request. Market not found")
    return crud.chart(db, market)
    
@app.get("/market/buy/")
def get_order_buy(token1: str, token2: str, db: Session = Depends(get_db)):
    t1 = crud.find_token(db, token1)
    t2 = crud.find_token(db, token2)
    if t1 is None or t2 is None:
        ok = 0
        raise HTTPException(status_code=400, detail="Bad request. Token not found!")
    token1 = token1.lower()
    token2 = token2.lower()
    if crud.check_market(db, token1, token2) == "NO":
        ok = 0
        raise HTTPException(status_code=400, detail="Bad request. Market not found")
    market: models.Market = crud.find_market(db, token1.lower(), token2.lower())
    if market is None:
        raise HTTPException(status_code=400, detail="Bad request. Market not found")
    return crud.get_order_buy(db, market)

@app.get("/market/sell/")
def get_order_sell(token1: str, token2: str, db: Session = Depends(get_db)):
    t1 = crud.find_token(db, token1)
    t2 = crud.find_token(db, token2)
    if t1 is None or t2 is None:
        ok = 0
        raise HTTPException(status_code=400, detail="Bad request. Token not found!")
    token1 = token1.lower()
    token2 = token2.lower()
    if crud.check_market(db, token1, token2) == "NO":
        ok = 0
        raise HTTPException(status_code=400, detail="Bad request. Market not found")
    market: models.Market = crud.find_market(db, token1.lower(), token2.lower())
    if market is None:
        raise HTTPException(status_code=400, detail="Bad request. Market not found")
    return crud.get_order_sell(db, market)

@app.get("/markets/")
def get_markets(db: Session = Depends(get_db)):
    return crud.get_markets(db)

@app.get("/tokens/")
def get_tokens(db: Session = Depends(get_db)):
    return crud.get_tokens(db)

@app.get("/market/history/")
def get_history(token1: str, token2: str, db: Session = Depends(get_db)):
    t1 = crud.find_token(db, token1)
    t2 = crud.find_token(db, token2)
    if t1 is None or t2 is None:
        ok = 0
        raise HTTPException(status_code=400, detail="Bad request. Token not found!")
    token1 = token1.lower()
    token2 = token2.lower()
    if crud.check_market(db, token1, token2) == "NO":
        ok = 0
        raise HTTPException(status_code=400, detail="Bad request. Market not found!")
    market: models.Market = crud.find_market(db, token1.lower(), token2.lower())
    return crud.get_order_history(db, market)

@app.get("/market/check/{orderid}")
def check_order(orderid: int, db: Session = Depends(get_db)):
    order = crud.check_order(db, orderid)
    if order is None:
        raise HTTPException(status_code=404, detail="MarketOrderID not found!")
    return order

@app.get("/market/volume24h")
def get_24hvolume(token1: str, token2: str, db: Session = Depends(get_db)):
    t1 = crud.find_token(db, token1)
    t2 = crud.find_token(db, token2)
    if t1 is None or t2 is None:
        ok = 0
        raise HTTPException(status_code=400, detail="Bad request. Token not found!")
    token1 = token1.lower()
    token2 = token2.lower()
    if crud.check_market(db, token1, token2) == "NO":
        ok = 0
        raise HTTPException(status_code=400, detail="Bad request. Market not found!")
    market: models.Market = crud.find_market(db, token1.lower(), token2.lower())
    return crud.get_24h_volume(db, market)

@app.get("/market/high24h")
def get_24hhigh(token1: str, token2: str, db: Session = Depends(get_db)):
    t1 = crud.find_token(db, token1)
    t2 = crud.find_token(db, token2)
    if t1 is None or t2 is None:
        ok = 0
        raise HTTPException(status_code=400, detail="Bad request. Token not found!")
    token1 = token1.lower()
    token2 = token2.lower()
    if crud.check_market(db, token1, token2) == "NO":
        ok = 0
        raise HTTPException(status_code=400, detail="Bad request. Market not found!")
    market: models.Market = crud.find_market(db, token1.lower(), token2.lower())
    return crud.get_24h_high(db, market)

@app.get("/market/low24h")
def get_24hlow(token1: str, token2: str, db: Session = Depends(get_db)):
    t1 = crud.find_token(db, token1)
    t2 = crud.find_token(db, token2)
    if t1 is None or t2 is None:
        ok = 0
        raise HTTPException(status_code=400, detail="Bad request. Token not found!")
    token1 = token1.lower()
    token2 = token2.lower()
    if crud.check_market(db, token1, token2) == "NO":
        ok = 0
        raise HTTPException(status_code=400, detail="Bad request. Market not found!")
    market: models.Market = crud.find_market(db, token1.lower(), token2.lower())
    return crud.get_24h_low(db, market)

@app.get("/market/lastprice")
def get_last_price(token1: str, token2: str, db: Session = Depends(get_db)):
    t1 = crud.find_token(db, token1)
    t2 = crud.find_token(db, token2)
    if t1 is None or t2 is None:
        ok = 0
        raise HTTPException(status_code=400, detail="Bad request. Token not found!")
    token1 = token1.lower()
    token2 = token2.lower()
    if crud.check_market(db, token1, token2) == "NO":
        ok = 0
        raise HTTPException(status_code=400, detail="Bad request. Market not found!")
    market: models.Market = crud.find_market(db, token1.lower(), token2.lower())
    return crud.get_last_price(db, market)

@app.get("/market_full")
def get_full_data_market(db: Session = Depends(get_db)):
    return crud.get_full_data_market(db)

@app.get("/getcharts/")
def get_data_chart(db: Session = Depends(get_db)):
    return crud.get_datachart(db)

@app.get("/market/chart")
def get_last_price(token1: str, token2: str, db: Session = Depends(get_db)):
    t1 = crud.find_token(db, token1)
    t2 = crud.find_token(db, token2)
    if t1 is None or t2 is None:
        ok = 0
        raise HTTPException(status_code=400, detail="Bad request. Token not found!")
    token1 = token1.lower()
    token2 = token2.lower()
    if crud.check_market(db, token1, token2) == "NO":
        ok = 0
        raise HTTPException(status_code=400, detail="Bad request. Market not found!")
    market: models.Market = crud.find_market(db, token1.lower(), token2.lower())
    return crud.get_datachart_of_market(db, market)