import pyupbit

def print_all_market_info():
    try:
        # 모든 가상화폐의 티커(symbol) 가져오기
        tickers = pyupbit.get_tickers()
        
        for ticker in tickers:
            try:
                ticker_info = pyupbit.get_current_price(ticker)
                if ticker_info is not None:
                    print(f"현재 {ticker}의 가격은 {ticker_info:,} 원입니다.")  # 가격을 천 단위로 쉼표로 구분하여 출력
                else:
                    print(f"{ticker}의 정보를 가져올 수 없습니다.")
            except Exception as e:
                print(f"{ticker}의 데이터를 가져오는 중 오류가 발생했습니다: {str(e)}")
    except Exception as e:
        print(f"가상화폐 티커를 가져오는 중 오류가 발생했습니다: {str(e)}")

if __name__ == "__main__":
    # 모든 가상화폐의 시세 출력 함수 호출
    print_all_market_info()
