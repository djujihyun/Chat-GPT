import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime

# SQLite 데이터베이스 연결
conn = sqlite3.connect('crypto_prices.db')
c = conn.cursor()

# 데이터 조회 함수
def fetch_data():
    c.execute("SELECT timestamp, price FROM bitcoin_prices")
    rows = c.fetchall()
    return rows

# 데이터 변환 함수
def transform_data(rows):
    dates = [datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S') for row in rows]
    prices = [row[1] for row in rows]
    return dates, prices

# 데이터 조회 및 변환
data = fetch_data()
dates, prices = transform_data(data)

# 그래프 시각화
plt.figure(figsize=(10, 5))
plt.plot(dates, prices, label='Bitcoin Price (KRW)')
plt.xlabel('Date')
plt.ylabel('Price (KRW)')
plt.title('Bitcoin Price Over Time')
plt.legend()
plt.grid(True)
plt.show()

# 데이터베이스 연결 종료
conn.close()
