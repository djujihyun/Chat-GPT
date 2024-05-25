import requests
from bs4 import BeautifulSoup

def get_stock_data(symbol):
    url = f"https://finance.yahoo.com/quote/{symbol}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 주식 시세 정보가 포함된 요소를 찾습니다.
    price_element = soup.find("div", {"class": "D(ib) Mend(20px)"})
    price = price_element.find("span").text

    return price

def main():
    symbol = input("주식 심볼을 입력하세요 (예: AAPL): ")

    print("주식 시세를 조회 중입니다...")
    try:
        stock_price = get_stock_data(symbol)
        print(f"{symbol}의 현재 주가는 ${stock_price}입니다.")
    except Exception as e:
        print("주식 시세 조회 중 오류 발생:", e)

if __name__ == "__main__":
    main()

