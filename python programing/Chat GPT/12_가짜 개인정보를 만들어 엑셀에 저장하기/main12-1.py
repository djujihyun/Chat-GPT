from faker import Faker

# faker 객체 생성
fake = Faker()

# 가짜 이름 생성
fake_name = fake.name()

# 가짜 주소 생성
fake_address = fake.address()

# 가짜 전화번호 생성
fake_phone_number = fake.phone_number()

# 가짜 이메일 생성
fake_email = fake.email()

# 생성된 가짜 정보 출력
print("가짜 이름:", fake_name)
print("가짜 주소:", fake_address)
print("가짜 전화번호:", fake_phone_number)
print("가짜 이메일:", fake_email)
