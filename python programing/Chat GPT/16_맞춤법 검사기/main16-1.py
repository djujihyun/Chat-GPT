import requests

def check_spelling(text):
    url = "https://m.search.naver.com/p/csearch/ocontent/spellchecker.nhn"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    data = {
        "q": text
    }
    response = requests.post(url, headers=headers, data=data)
    result = response.json()
    return result['message']['result']['html']

def main():
    text = input("맞춤법을 검사할 문장을 입력하세요: ")
    result_html = check_spelling(text)
    print("검사 결과:")
    print(result_html)

if __name__ == "__main__":
    main()
