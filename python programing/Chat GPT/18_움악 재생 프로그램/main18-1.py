from gtts import gTTS

# 텍스트를 음성으로 변환
text = "안녕하세요"
tts = gTTS(text, lang='ko')

# mp3 파일로 저장
tts.save("hello.mp3")

print("음성 파일이 생성되었습니다.")
