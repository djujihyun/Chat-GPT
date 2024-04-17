import requests

def get_exchange_rate(base_currency, target_currency):
    url = f'https://v6.exchangeratesapi.io/latest?base={base_currency}&symbols={target_currency}'
    
    response = requests.get(url)
    data = response.json()
    
    if 'error' in data:
        raise Exception(f"Error: {data['error']}")
    
    if target_currency not in data['rates']:
        raise Exception(f"Currency '{target_currency}' is not supported.")
    
    return data['rates'][target_currency]

def convert_currency(amount, base_currency, target_currency):
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    converted_amount = amount * exchange_rate
    return converted_amount

if __name__ == "__main__":
    amount = float(input("변환할 금액을 입력하세요: "))
    base_currency = input("변환하려는 통화를 입력하세요 (예: USD): ").upper()
    target_currency = input("원하는 통화를 입력하세요 (예: KRW): ").upper()

    try:
        converted_amount = convert_currency(amount, base_currency, target_currency)
        print(f"{amount} {base_currency}은(는) {converted_amount} {target_currency}입니다.")
    except Exception as e:
        print(f"에러 발생: {e}")
