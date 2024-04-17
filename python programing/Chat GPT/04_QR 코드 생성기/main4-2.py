import os
import qrcode

# 저장될 파일 경로 설정
save_path = r'C:\Users\COMPUTER\Desktop\python programing\Chat GPT\04_QR 코드 생성기\QRcord'
if not os.path.exists(save_path):
    os.makedirs(save_path)

# QR 코드에 저장될 데이터
data = "https://www.openai.com/"

# QR 코드 생성
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)

# 이미지 생성
img = qr.make_image(fill_color="black", back_color="white")

# 파일로 저장
file_path = os.path.join(save_path, "openai_qr_code.png")
img.save(file_path)

print("QR 코드가 다음 위치에 저장되었습니다:", file_path)
