import qrcode

# QR 코드에 저장될 데이터
data = "https://www.openai.com/"

# QR 코드 생성
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)

# 이미지 생성
img = qr.make_image(fill_color="black", back_color="white")

# 파일로 저장
img.save("openai_qr_code.png")