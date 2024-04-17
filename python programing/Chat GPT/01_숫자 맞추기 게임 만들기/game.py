import random

def get_user_choice():
    while True:
        user_choice = input("가위, 바위, 보 중 하나를 선택하세요: ").lower()
        if user_choice in ['가위', '바위', '보']:
            return user_choice
        else:
            print("올바른 선택이 아닙니다. 다시 선택하세요.")

def get_computer_choice():
    return random.choice(['가위', '바위', '보'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "무승부"
    elif (user_choice == '가위' and computer_choice == '보') or \
         (user_choice == '바위' and computer_choice == '가위') or \
         (user_choice == '보' and computer_choice == '바위'):
        return "사용자 승리"
    else:
        return "컴퓨터 승리"

if __name__ == "__main__":
    print("가위바위보 게임을 시작합니다.")
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"사용자: {user_choice}, 컴퓨터: {computer_choice}")
        
        winner = determine_winner(user_choice, computer_choice)
        print(f"결과: {winner}")
        
        play_again = input("다시 하시겠습니까? (yes/no): ").lower()
        if play_again != 'yes':
            print("게임을 종료합니다.")
            break
