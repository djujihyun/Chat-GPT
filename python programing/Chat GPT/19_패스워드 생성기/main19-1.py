import random
import string

def generate_password(length=8, include_digits=True, include_special_chars=True):
    chars = string.ascii_letters  # 영문 대소문자

    if include_digits:
        chars += string.digits  # 숫자 포함

    if include_special_chars:
        chars += string.punctuation  # 특수문자 포함

    return ''.join(random.choice(chars) for _ in range(length))

def main():
    length = int(input("생성할 패스워드의 길이를 입력하세요: "))
    include_digits = input("숫자를 포함할까요? (Y/N): ").upper() == 'Y'
    include_special_chars = input("특수문자를 포함할까요? (Y/N): ").upper() == 'Y'

    password = generate_password(length, include_digits, include_special_chars)
    print("생성된 패스워드:", password)

if __name__ == "__main__":
    main()
