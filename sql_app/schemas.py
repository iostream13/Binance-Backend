from enum import Enum
from typing import List
from pydantic import BaseModel
from datetime import datetime

from .models import Action

class UserBase(BaseModel):
    username: str
    userbio: str = ""
    
class UserCreate(UserBase):
    password: str
    
class UserInfor(UserBase):
    userbio: str
    
    class Config:
        orm_mode = True
        
class Token(BaseModel):
    tokenname: str
    tokensymbol: str
    tokenimage: str
    marketcap: float
    totalsupply: float
    maxsupply: float
    coingeckoprice: float
    
    class Config:
        orm_mode = True
        
class TokenHistory(BaseModel):
    tokenhistoryid: int
    tokenname: str
    volume: float
    
    class Config:
        orm_mode = True
        
class UserBalance(BaseModel):
    username: str
    tokenname: str
    amount: float
    
    class Config:
        orm_mode = True
    
class Market(BaseModel):
    marketid: int
    token1: str
    token2: str
    
    class Config:
        orm_mode = True
    
class MarketHistory(BaseModel):
    markethistoryid: int
    marketid: int
    volume: float
    
    class Config:
        orm_mode = True
    
class MarketOrder(BaseModel):
    marketorderid: int
    username: str
    marketid: int
    orderaction: Action
    totalamount: float
    remainamount: float
    price: float
    
    class Config:
        orm_mode = True
    
class OrderHistory(BaseModel):
    orderhistoryid: int
    marketorderid: int
    marketid: int
    amount: float
    orderedat: datetime
    
    class Config:
        orm_mode = True
