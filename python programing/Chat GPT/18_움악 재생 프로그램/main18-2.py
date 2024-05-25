import pygame

def play_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def main():
    file_path = input("재생할 음악 파일 경로를 입력하세요: ")
    play_music(file_path)

    input("음악 재생 중... 종료하려면 아무 키나 누르세요.")

    pygame.mixer.music.stop()
    pygame.mixer.quit()

if __name__ == "__main__":
    main()
