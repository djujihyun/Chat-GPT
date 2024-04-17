import zipfile
import itertools

def crack_zip_password(zip_file_path, characters, length):
    # 가능한 모든 조합 생성
    combinations = itertools.product(characters, repeat=length)

    # zip 파일 열기
    with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
        for combination in combinations:
            # 조합을 문자열로 변환하여 비밀번호 시도
            password = ''.join(combination)
            try:
                zip_file.extractall(pwd=password.encode())
                print(f"비밀번호 발견: {password}")
                return password
            except zipfile.BadPasswordError:
                pass

    print("암호를 찾을 수 없습니다.")
    return None

# 함수 사용 예시
zip_file_path = (r'C:\Users\COMPUTER\Desktop\python programing\Chat GPT\06_압축파일 암호푸는 프로그램\암호.zip')  # 암호화된 zip 파일 경로
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'  # 가능한 문자열
length = 4  # 암호의 길이
password = crack_zip_password(zip_file_path, characters, length)
if password:
    print(f"압축 파일의 비밀번호는 '{password}' 입니다.")
else:
    print("압축 파일의 비밀번호를 찾을 수 없습니다.")
