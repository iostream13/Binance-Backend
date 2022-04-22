from operator import index
from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String, column, true, Enum, DateTime
from sqlalchemy.orm import relationship
import enum

from .database import Base

class Action(str, enum.Enum):
    BUY = "BUY"
    SELL = "SELL"
    
class User(Base):
    __tablename__ = "user"
    
    username = Column(String, primary_key = True, index = True)
    password = Column(String)
    userbio = Column(String)
    
    balanceuser = relationship("UserBalance", back_populates = "user")
    userorders = relationship("MarketOrder", back_populates = "user")
    
class Token(Base):
    __tablename__ = "token"
    
    tokenname = Column(String, primary_key = True, index = True)
    tokensymbol = Column(String)
    tokenimage = Column(String)
    marketcap = Column(Float)
    totalsupply = Column(Float)
    maxsupply = Column(Float)
    coingeckoprice = Column(Float)
    
    listtokenhistory = relationship("TokenHistory", back_populates = "token")
    balancetoken = relationship("UserBalance", back_populates = "token")
    
class TokenHistory(Base):
    __tablename__ = "tokenhistory"
    
    tokenhistoryid = Column(Integer, primary_key = True, index = True)
    tokenname = Column(String, ForeignKey("token.tokenname"))
    volume = Column(Float)
    
    token = relationship("Token", back_populates = "listtokenhistory")
    
class UserBalance(Base):
    __tablename__ = "userbalance"
    
    username = Column(String, ForeignKey("user.username"), primary_key = True)
    tokenname = Column(String, ForeignKey("token.tokenname"), primary_key = True)
    amount = Column(Float)
    
    user = relationship("User", back_populates = "balanceuser")
    token = relationship("Token", back_populates = "balancetoken")
    
class Market(Base):
    __tablename__ = "market"
    
    marketid = Column(Integer, primary_key = True, index = True)
    token1 = Column(String)
    token2 = Column(String)
    
    listmarkethistory = relationship("MarketHistory", back_populates = "market")
    marketorders = relationship("MarketOrder", back_populates = "market")
    
class MarketHistory(Base):
    __tablename__ = "markethistory"
    
    markethistoryid = Column(Integer, primary_key = True, index = True)
    marketid = Column(Integer, ForeignKey("market.marketid"))
    volume = Column(Float)
    
    market = relationship("Market", back_populates = "listmarkethistory")
    
class MarketOrder(Base):
    __tablename__ = "marketorder"
    
    marketorderid = Column(Integer, primary_key = True, index = True)
    username = Column(String, ForeignKey("user.username"))
    marketid = Column(Integer, ForeignKey("market.marketid"))
    orderaction = Column(Enum(Action))
    totalamount = Column(Float)
    remainamount = Column(Float)
    price = Column(Float)
    
    user = relationship("User", back_populates = "userorders")
    market = relationship("Market", back_populates = "marketorders")
    listmarketorders = relationship("OrderHistory", back_populates = "marketorder")
    
class OrderHistory(Base):
    __tablename__ = "orderhistory"
    
    orderhistoryid = Column(Integer, primary_key = True, index = True)
    marketorderid = Column(Integer, ForeignKey("marketorder.marketorderid"))
    amount = Column(Float)
    orderedat = Column(DateTime)
    
    marketorder = relationship("MarketOrder", back_populates = "listmarketorders")


    