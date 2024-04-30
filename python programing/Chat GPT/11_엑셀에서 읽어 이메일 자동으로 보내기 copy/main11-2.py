import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_emails(excel_file, sender_email, sender_password):
    try:
        # Excel 파일 읽기
        df = pd.read_excel(excel_file)
        
        # SMTP 서버 설정
        smtp_server = 'smtp.gmail.com'  # 이메일 서비스에 따라 다를 수 있음
        smtp_port = 587  # TLS 포트

        # SMTP 서버 연결
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        
        # 로그인
        server.login(sender_email, sender_password)
        
        # 이메일 보내기
        for index, row in df.iterrows():
            recipient_email = row['이메일']  # 열 이름에 맞게 수정
            name = row['이름']  # 열 이름에 맞게 수정
            subject = f"{name} 님 환영합니다."
            body = f"{name} 님 늦지 않게 와주세요."

            # 이메일 메시지 생성
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            # 이메일 보내기
            server.send_message(msg)
        
        # SMTP 서버 연결 종료
        server.quit()
        
        print("이메일이 성공적으로 전송되었습니다.")
    except Exception as e:
        print(f"오류 발생: {e}")

if __name__ == "__main__":
    excel_file = "Chat GPT/11_엑셀에서 읽어 이메일 자동으로 보내기/이메일.xlsx"  # 엑셀 파일 경로
    sender_email = "cjihyun052594@gmail.com"  # 보내는 이메일 주소
    sender_password = "upjj mpiy tuee jkmm"  # 보내는 이메일 계정 비밀번호

    send_emails(excel_file, sender_email, sender_password)
