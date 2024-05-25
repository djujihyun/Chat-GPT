import tkinter as tk
from tkinter import messagebox
import requests

def get_stock_price(stock_code):
    url = f"https://api.finance-data.kr/api/v1/stock/single?code={stock_code}&type=quote"
    response = requests.get(url)
    data = response.json()

    if data.get('error'):
        raise ValueError(data.get('error'))

    price = data.get('trade_price')
    return price

def display_stock_price():
    stock_code = entry.get()

    try:
        stock_price = get_stock_price(stock_code)
        messagebox.showinfo("주식 시세", f"{stock_code}의 현재 주가는 {stock_price}원입니다.")
    except Exception as e:
        messagebox.showerror("오류", f"주식 시세 조회 중 오류 발생: {e}")

# GUI 생성
root = tk.Tk()
root.title("주식 시세 조회")

label = tk.Label(root, text="종목번호를 입력하세요:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="조회", command=display_stock_price)
button.pack(pady=5)

root.mainloop()
