from googletrans import Translator

def translate_english_to_korean(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        english_text = file.read()

    translator = Translator()
    translated_text = translator.translate(english_text, dest='ko').text

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(translated_text)

if __name__ == "__main__":
    input_file = "Chat GPT/09_영어 문서를 한글로 자동번역/영어문서.txt"
    output_file = "Chat GPT/09_영어 문서를 한글로 자동번역/한글번역.txt"

    try:
        translate_english_to_korean(input_file, output_file)
        print("번역이 완료되었습니다.")
    except Exception as e:
        print(f"에러 발생: {e}")
