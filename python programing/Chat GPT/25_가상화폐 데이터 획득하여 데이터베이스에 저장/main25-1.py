import pyupbit
import sqlite3
from datetime import datetime

# SQLite 데이터베이스 연결
conn = sqlite3.connect('crypto_prices.db')
c = conn.cursor()

# 테이블 생성
c.execute('''
    CREATE TABLE IF NOT EXISTS bitcoin_prices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        price REAL
    )
''')

# 현재 시세 조회 함수
def fetch_and_store_price():
    # 비트코인 현재 시세 조회
    price = pyupbit.get_current_price("KRW-BTC")
    
    # 현재 시간 가져오기
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # 데이터베이스에 삽입
    c.execute("INSERT INTO bitcoin_prices (timestamp, price) VALUES (?, ?)", (now, price))
    conn.commit()
    print(f"Inserted data: {now} - {price}")

# 시세 조회 및 저장 실행
fetch_and_store_price()

# 데이터베이스 연결 종료
conn.close()
