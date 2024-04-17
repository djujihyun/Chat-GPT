import zipfile
import os

def zip_files(file_paths, zip_name):
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for file_path in file_paths:
            zipf.write(file_path, os.path.basename(file_path))

if __name__ == "__main__":
    file_paths = []
    num_files = int(input("압축할 파일 수를 입력하세요: "))
    
    for i in range(num_files):
        file_path = input(f"{i+1}번째 파일 경로를 입력하세요: ")
        if os.path.exists(file_path):
            file_paths.append(file_path)
        else:
            print(f"경로 '{file_path}'에 파일이 없습니다.")

    zip_name = input("압축 파일의 이름을 입력하세요: ") + '.zip'

    try:
        zip_files(file_paths, zip_name)
        print(f"'{zip_name}' 파일이 생성되었습니다.")
    except Exception as e:
        print(f"에러 발생: {e}")
