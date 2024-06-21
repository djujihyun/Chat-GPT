import matplotlib.pyplot as plt
import pandas as pd
import pyupbit
from datetime import datetime, timedelta

def get_bitcoin_price(start_date, end_date):
    # 비트코인 가격 데이터 가져오기
    df = pyupbit.get_ohlcv("BTC-KRW", interval="day", to=end_date, count=365)
    
    # 기간 필터링
    df = df[start_date:end_date]
    
    return df

def plot_bitcoin_price(df):
    # 그래프 설정
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['close'], marker='o', linestyle='-', color='b', label='Bitcoin Price (KRW)')
    
    # 그래프 제목과 축 레이블 설정
    plt.title('Bitcoin Price (KRW) - 1 Year')
    plt.xlabel('Date')
    plt.ylabel('Price (KRW)')
    
    # x 축 눈금 간격 설정
    plt.xticks(pd.date_range(start=df.index.min(), end=df.index.max(), freq='1M'), rotation=45)
    
    # 그리드 표시
    plt.grid(True)
    
    # 범례 표시
    plt.legend()
    
    # 그래프 출력
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # 1년 전 날짜와 오늘 날짜 계산
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    
    # 비트코인 가격 데이터 가져오기
    btc_df = get_bitcoin_price(start_date, end_date)
    
    # 그래프 그리기
    plot_bitcoin_price(btc_df)
