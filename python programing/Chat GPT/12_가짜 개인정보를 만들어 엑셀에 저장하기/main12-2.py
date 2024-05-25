from faker import Faker
from openpyxl import Workbook
import random

def generate_fake_data(num_entries):
    fake = Faker()
    data = []
    for _ in range(num_entries):
        # 가짜 이름 및 성별 생성
        fake_name = fake.name()
        fake_gender = random.choice(['Male', 'Female'])

        # 가짜 이메일 생성
        fake_email = fake.email()

        # 가짜 전화번호 생성
        fake_phone_number = fake.phone_number()

        # 생성된 가짜 정보를 리스트에 추가
        data.append((fake_name, fake_gender, fake_email, fake_phone_number))
    return data

def save_to_excel(data, filename):
    wb = Workbook()
    ws = wb.active
    ws.append(["Name", "Gender", "Email", "Phone Number"])
    for row in data:
        ws.append(row)
    wb.save(filename)

if __name__ == "__main__":
    num_entries = 1000
    fake_data = generate_fake_data(num_entries)
    save_to_excel(fake_data, "12_가짜 개인정보를 만들어 엑셀에 저장하기/개인정보.xlsx")
    print(f"{num_entries}개의 가짜 개인정보가 생성되어 엑셀 파일에 저장되었습니다.")
