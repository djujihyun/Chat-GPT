import sqlite3

# SQLite 데이터베이스 연결
conn = sqlite3.connect('crypto_prices.db')
c = conn.cursor()

# 데이터 조회 함수
def fetch_data():
    c.execute("SELECT * FROM bitcoin_prices")
    rows = c.fetchall()
    return rows

# 데이터 출력 함수
def print_data(rows):
    for row in rows:
        print(f"ID: {row[0]}, Timestamp: {row[1]}, Price: {row[2]}")

# 데이터 조회 및 출력
data = fetch_data()
print_data(data)

# 데이터베이스 연결 종료
conn.close()
