import psutil
import time

def get_system_info():
    # CPU 사용량 가져오기
    cpu_percent = psutil.cpu_percent(interval=0.1)  # 0.1초 간격으로 CPU 사용량 측정
    print(f"CPU 사용량: {cpu_percent}%")

    # RAM 사용량 가져오기
    ram = psutil.virtual_memory()
    ram_percent = ram.percent
    print(f"RAM 사용량: {ram_percent}%")

    # 네트워크 사용량 가져오기
    network = psutil.net_io_counters()
    sent_bytes = network.bytes_sent
    received_bytes = network.bytes_recv
    print(f"네트워크 전송량: {sent_bytes} bytes")
    print(f"네트워크 수신량: {received_bytes} bytes")

# 1초마다 시스템 정보 출력
while True:
    get_system_info()
    print("-" * 50)
    time.sleep(1)
