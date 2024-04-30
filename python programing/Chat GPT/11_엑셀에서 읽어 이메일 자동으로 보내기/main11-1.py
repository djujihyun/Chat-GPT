import pandas as pd

def print_email_and_name(excel_file):
    try:
        # Excel 파일 읽기
        df = pd.read_excel(excel_file)
        
        # 이메일 주소와 이름 출력
        for index, row in df.iterrows():
            email = row['이메일']  # '이메일 주소'는 실제 열 이름으로 대체해야 합니다.
            name = row['이름']  # '이름'은 실제 열 이름으로 대체해야 합니다.
            print(f"이메일 주소: {email}, 이름: {name}")
    except Exception as e:
        print(f"오류 발생: {e}")

if __name__ == "__main__":
    excel_file = "Chat GPT/11_엑셀에서 읽어 이메일 자동으로 보내기/이메일.xlsx"  # 실제 파일 경로로 대체하십시오.
    
    print_email_and_name(excel_file)
