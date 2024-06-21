import pyupbit

def print_market_info(ticker):
    try:
        ticker_info = pyupbit.get_current_price(ticker)
        if ticker_info is not None:
            print(f"현재 {ticker}의 가격은 {ticker_info:,} 원입니다.")  # 가격을 천 단위로 쉼표로 구분하여 출력
        else:
            print(f"{ticker}의 정보를 가져올 수 없습니다. 티커 심볼을 확인해주세요.")
    except Exception as e:
        print(f"{ticker}의 데이터를 가져오는 중 오류가 발생했습니다: {str(e)}")

if __name__ == "__main__":
    # 원하는 가상화폐의 티커 심볼을 입력합니다.
    ticker_symbol = "BTC"  # 예시로 비트코인(BTC)을 기준으로 설정
    
    # 시세 출력 함수 호출
    print_market_info(ticker_symbol)
