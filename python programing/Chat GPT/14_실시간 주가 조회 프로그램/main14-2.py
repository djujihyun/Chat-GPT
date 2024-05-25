import requests

def get_stock_price(stock_code):
    url = f"https://api.finance-data.kr/api/v1/stock/single?code={stock_code}&type=quote"
    response = requests.get(url)
    data = response.json()

    if data.get('error'):
        raise ValueError(data.get('error'))

    price = data.get('trade_price')
    return price

def main():
    stock_code = input("종목번호를 입력하세요 (예: 005930): ")

    print("주식 시세를 조회 중입니다...")
    try:
        stock_price = get_stock_price(stock_code)
        print(f"{stock_code}의 현재 주가는 {stock_price}원입니다.")
    except Exception as e:
        print("주식 시세 조회 중 오류 발생:", e)

if __name__ == "__main__":
    main()
