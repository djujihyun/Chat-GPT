import requests
from bs4 import BeautifulSoup
import re

def extract_emails_from_url(url):
    try:
        # 웹페이지의 HTML 가져오기
        response = requests.get(url)
        html_content = response.text
        
        # BeautifulSoup을 사용하여 HTML 파싱
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # 정규표현식을 사용하여 이메일 주소 추출
        emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', html_content)
        
        return emails
    except Exception as e:
        print(f"오류 발생: {e}")
        return []

if __name__ == "__main__":
    url = input("이메일을 수집할 웹페이지 URL을 입력하세요: ")
    
    extracted_emails = extract_emails_from_url(url)
    
    if extracted_emails:
        print("수집된 이메일 주소:")
        for email in extracted_emails:
            print(email)
    else:
        print("이메일 주소를 찾을 수 없습니다.")
