import os
import time
from distutils.dir_util import copy_tree

# 백업 함수
def backup_folder(source_folder, destination_folder):
    try:
        # 현재 시간을 기준으로 백업 폴더 이름 생성
        current_time = time.strftime('%Y%m%d_%H%M%S')
        destination_path = os.path.join(destination_folder, f"backup_{current_time}")

        # 백업 폴더가 없으면 생성
        if not os.path.exists(destination_path):
            os.makedirs(destination_path)

        # 디렉토리 복사
        copy_tree(source_folder, destination_path)
        print(f"Backup completed successfully from {source_folder} to {destination_path}")
    except Exception as e:
        print(f"Error during backup: {e}")

# 사용자로부터 소스 폴더와 대상 폴더 경로 입력 받기
source_folder = input("Enter the path to the source folder: ")
destination_folder = input("Enter the path to the backup folder: ")

# 경로 유효성 검사
if os.path.exists(source_folder) and os.path.isdir(source_folder):
    backup_folder(source_folder, destination_folder)
else:
    print("Invalid source folder path.")
