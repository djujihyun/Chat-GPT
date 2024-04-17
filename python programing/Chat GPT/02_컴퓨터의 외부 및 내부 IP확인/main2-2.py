import requests

def get_external_ip():
    try:
        # ipinfo.io 서비스를 사용하여 외부 IP 주소 확인
        response = requests.get('https://ipinfo.io')
        data = response.json()
        external_ip = data['ip']
        return external_ip
    except Exception as e:
        print("외부 IP를 가져오는 데 실패했습니다:", e)
        return None

if __name__ == "__main__":
    external_ip = get_external_ip()
    if external_ip:
        print("외부 IP:", external_ip)