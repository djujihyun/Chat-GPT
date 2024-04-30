import pandas as pd

def save_emails_to_excel(emails, excel_file):
    try:
        # DataFrame 생성
        df = pd.DataFrame({'Email': emails})
        
        # Excel 파일로 저장
        df.to_excel(excel_file, index=False)
        print(f"이메일이 '{excel_file}' 파일에 저장되었습니다.")
    except Exception as e:
        print(f"오류 발생: {e}")

if __name__ == "__main__":
    emails = ["example1@example.com", "example2@example.com", "example3@example.com"]  # 이메일 주소를 대체하십시오.
    excel_file = "Chat GPT/10_이메일을 수집하여 엑셀에 기록하기/이메일.xlsx"
    
    save_emails_to_excel(emails, excel_file)
