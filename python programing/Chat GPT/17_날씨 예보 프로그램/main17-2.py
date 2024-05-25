import requests
from openpyxl import Workbook
from datetime import datetime, timedelta
import time

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def save_to_excel(weather_data, file_name):
    wb = Workbook()
    ws = wb.active
    ws.append(["날짜", "시간", "날씨", "온도(°C)"])

    for weather in weather_data:
        date_time = datetime.fromtimestamp(weather['dt'])
        date = date_time.strftime('%Y-%m-%d')
        time = date_time.strftime('%H:%M:%S')
        description = weather['weather'][0]['description']
        temperature = weather['main']['temp']
        ws.append([date, time, description, temperature])

    wb.save(file_name)

def main():
    api_key = "YOUR_API_KEY"  # OpenWeatherMap API 키
    city = input("도시 이름을 입력하세요: ")
    duration = int(input("날씨를 저장할 시간(분)을 입력하세요: "))
    interval = 30  # 30분 간격으로 저장

    weather_data = []

    try:
        for _ in range(duration // interval):
            weather = get_weather(api_key, city)
            weather_data.append(weather)
            time.sleep(interval * 60)  # 분을 초로 변환하여 sleep
    except Exception as e:
        print("날씨 정보를 가져오는 중 오류 발생:", e)

    save_to_excel(weather_data, "날씨저장.xlsx")
    print("날씨 정보가 엑셀 파일에 저장되었습니다.")

if __name__ == "__main__":
    main()
