## TÍNH NĂNG
- Show những đồng tiền ảo "đang hot" ở trang chủ.
- Quản lý tài khoản người dùng: Những đồng tiền đang sở hữu - giá trị và số lượng.
- Sàn giao dịch (theo mô hình orderbook)
  + Nhập lượng tiền, giá mong muốn và giao dịch. (giao dịch gồm mua và bán)
  + Thanh % cho số lượng tiền muốn giao dịch.
  + Danh sách các order mua và bán đã có.
  + Đồ thị biểu hiện giáo cả lên xuống theo thời gian.

Example: 
![alt text](https://media.discordapp.net/attachments/684439044817551448/954054183101816852/Screen_Shot_2022-03-17_at_23.30.23.png?width=1011&height=701)

## Nguồn tham khảo
- https://www.binance.com/
- https://www.coingecko.com/

## Chi tiết

### Mô hình cơ sở dữ liệu

![alt text](https://media.discordapp.net/attachments/684439044817551448/966986171899052042/BinanceERR.png?width=504&height=700)


## sql_app
- crud.py : to define method (read,write) to MySQL
- database.py : for connecting MySQL
- main.py: main file for build FastAPI service
- models.py: define class object models for FastAPI
- schemas.py: define schemas for working with the specific API request/response

## repo Front-end
- https://github.com/lvhuy2002/binance-frontend
