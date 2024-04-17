import os
import qrcode

# QR 코드 생성 함수
def generate_qr_code(data, save_path):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(save_path)

# 파일 경로 설정
data_file = r'C:\Users\COMPUTER\Desktop\python programing\Chat GPT\04_QR 코드 생성기\Qrdata.txt'
output_folder = r'C:\Users\COMPUTER\Desktop\python programing\Chat GPT\04_QR 코드 생성기\QRcord'

# 출력 폴더가 없으면 생성
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 파일에서 데이터 읽어와서 QR 코드 생성
with open(data_file, 'r') as file:
    for idx, line in enumerate(file):
        # 각 라인의 데이터를 기반으로 QR 코드 생성
        data = line.strip()
        file_name = f"qr_code_{idx+1}.png"
        save_path = os.path.join(output_folder, file_name)
        generate_qr_code(data, save_path)
        print(f"QR 코드가 {save_path} 에 저장되었습니다.")
