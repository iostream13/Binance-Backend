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
        
@app.post("/user/", response_model=schemas.UserInfor)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, user_name=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="username already registered")
    return crud.create_user(db, user)

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
    
@app.put("/update_user/", status_code = status.HTTP_201_CREATED)
def update(username: str, bio: str, db: Session = Depends(get_db)):
    db.query(models.User).filter(models.User.username == username).update({"userbio": bio})
    db.commit()
    
@app.post("/test/")
def test(orderid: int, db: Session = Depends(get_db)):
    #return crud.delete_order(db, orderid)
    db_order = crud.get_order(db, orderid)
    if db_order is None:
        raise HTTPException(status_code=400, detail="Bad request. Not found order")
        return
    db.delete(db_order)
    db.commit()
    
