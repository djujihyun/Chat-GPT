import pyttsx3

def text_to_speech(text):
    try:
        # pyttsx3 엔진 초기화
        engine = pyttsx3.init()
        
        # 한글 텍스트를 음성으로 출력
        engine.say(text)
        
        # 음성 출력 시작
        engine.runAndWait()
    except Exception as e:
        print("음성 출력에 실패했습니다:", e)

if __name__ == "__main__":
    korean_text = "안녕하세요. 반갑습니다."
    text_to_speech(korean_text)