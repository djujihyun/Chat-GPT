import requests

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def main():
    api_key = "YOUR_API_KEY"  # OpenWeatherMap API 키
    city = input("도시 이름을 입력하세요: ")

    try:
        weather_data = get_weather(api_key, city)
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        print(f"{city}의 현재 날씨: {description}, 온도: {temperature}°C")
    except Exception as e:
        print("날씨 정보를 가져오는 중 오류 발생:", e)

if __name__ == "__main__":
    main()
