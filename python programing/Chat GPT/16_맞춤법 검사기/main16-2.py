import os
from hanspell import spell_checker

def correct_spelling(file_path):
    # 파일 읽기
    with open(file_path, 'r', encoding='utf-8') as f:
        original_text = f.read()

    # 맞춤법 보정
    corrected_text = spell_checker.check(original_text).checked

    # 수정된 내용을 새로운 파일에 저장
    file_name, file_extension = os.path.splitext(file_path)
    new_file_path = file_name + "_corrected" + file_extension
    with open(new_file_path, 'w', encoding='utf-8') as f:
        f.write(corrected_text)

    return new_file_path

def main():
    file_path = input("파일 경로를 입력하세요: ")

    try:
        corrected_file_path = correct_spelling(file_path)
        print(f"맞춤법이 보정된 파일이 저장되었습니다: {corrected_file_path}")
    except Exception as e:
        print("오류 발생:", e)

if __name__ == "__main__":
    main()
