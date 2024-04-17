from gtts import gTTS
import os

def text_to_speech(text, lang='ko'):
    try:
        # gTTS 객체 생성
        tts = gTTS(text=text, lang=lang)
        
        # mp3 파일로 저장
        tts.save("output.mp3")
        
        # 시스템 플레이어로 음성 재생
        os.system("start output.mp3")
    except Exception as e:
        print("음성 출력에 실패했습니다:", e)

if __name__ == "__main__":
    # 사용자로부터 텍스트 입력 받기
    user_text = input("텍스트를 입력하세요: ")
    
    # 입력받은 텍스트를 음성으로 변환
    text_to_speech(user_text)