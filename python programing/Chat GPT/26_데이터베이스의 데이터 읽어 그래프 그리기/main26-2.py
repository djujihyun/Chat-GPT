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

# 그래프 시각화 함수
def plot_graphs(dates, prices):
    plt.figure(figsize=(15, 10))

    # 선 그래프
    plt.subplot(2, 2, 1)
    plt.plot(dates, prices, label='Bitcoin Price (KRW)')
    plt.xlabel('Date')
    plt.ylabel('Price (KRW)')
    plt.title('Line Graph')
    plt.legend()
    plt.grid(True)

    # 막대 그래프
    plt.subplot(2, 2, 2)
    plt.bar(dates, prices, label='Bitcoin Price (KRW)')
    plt.xlabel('Date')
    plt.ylabel('Price (KRW)')
    plt.title('Bar Graph')
    plt.legend()
    plt.grid(True)

    # 산점도
    plt.subplot(2, 2, 3)
    plt.scatter(dates, prices, label='Bitcoin Price (KRW)', color='red')
    plt.xlabel('Date')
    plt.ylabel('Price (KRW)')
    plt.title('Scatter Plot')
    plt.legend()
    plt.grid(True)

    # 히스토그램 (가격 분포)
    plt.subplot(2, 2, 4)
    plt.hist(prices, bins=30, label='Bitcoin Price (KRW)', color='green')
    plt.xlabel('Price (KRW)')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# 그래프 시각화 호출
plot_graphs(dates, prices)

# 데이터베이스 연결 종료
conn.close()
