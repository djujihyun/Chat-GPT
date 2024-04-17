import random

def guess_number():
    # 1부터 100까지의 무작위 숫자 생성
    target_number = random.randint(1, 100)
    attempts = 0
    
    print("1부터 100 사이의 숫자를 맞춰보세요.")

    while True:
        try:
            # 사용자로부터 숫자 입력 받기
            guess = int(input("숫자를 입력하세요: "))
            attempts += 1

            # 입력한 숫자와 비교하여 결과 출력
            if guess < target_number:
                print("더 큰 숫자를 입력하세요.")
            elif guess > target_number:
                print("더 작은 숫자를 입력하세요.")
            else:
                print(f"축하합니다! {attempts}번 만에 숫자를 맞췄습니다.")
                break  # 숫자를 맞췄으므로 게임 종료
        except ValueError:
            print("올바른 숫자를 입력하세요.")

if __name__ == "__main__":
    guess_number()