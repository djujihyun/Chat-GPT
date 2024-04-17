import socket
import requests

def get_internal_ip():
    try:
        # 호스트 이름을 가져옴
        hostname = socket.gethostname()
        # 호스트 이름을 IP 주소로 변환
        internal_ip = socket.gethostbyname(hostname)
        return internal_ip
    except Exception as e:
        print("내부 IP를 가져오는 데 실패했습니다:", e)
        return None

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
    internal_ip = get_internal_ip()
    external_ip = get_external_ip()

    if internal_ip:
        print("내부 IP:", internal_ip)
    if external_ip:
        print("외부 IP:", external_ip)