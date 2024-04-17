import socket

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

if __name__ == "__main__":
    internal_ip = get_internal_ip()
    if internal_ip:
        print("내부 IP:", internal_ip)