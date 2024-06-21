import os
import time
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox
from distutils.dir_util import copy_tree

# 백업 함수
def backup_folder(source_folder, destination_folder):
    try:
        current_time = time.strftime('%Y%m%d_%H%M%S')
        destination_path = os.path.join(destination_folder, f"backup_{current_time}")

        if not os.path.exists(destination_path):
            os.makedirs(destination_path)

        copy_tree(source_folder, destination_path)
        messagebox.showinfo("Success", f"Backup completed successfully from {source_folder} to {destination_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Error during backup: {e}")

# 폴더 선택 함수
def select_source_folder():
    folder = filedialog.askdirectory()
    source_entry.delete(0, 'end')
    source_entry.insert(0, folder)

def select_destination_folder():
    folder = filedialog.askdirectory()
    destination_entry.delete(0, 'end')
    destination_entry.insert(0, folder)

# GUI 설정
root = Tk()
root.title("Backup Program")
root.geometry("300x200")

# 소스 폴더 선택
Label(root, text="Source Folder:").pack(pady=5)
source_entry = Entry(root, width=40)
source_entry.pack(pady=5)
Button(root, text="Browse", command=select_source_folder).pack(pady=5)

# 대상 폴더 선택
Label(root, text="Destination Folder:").pack(pady=5)
destination_entry = Entry(root, width=40)
destination_entry.pack(pady=5)
Button(root, text="Browse", command=select_destination_folder).pack(pady=5)

# 백업 시작 버튼
Button(root, text="Start Backup", command=lambda: backup_folder(source_entry.get(), destination_entry.get())).pack(pady=20)

# GUI 실행
root.mainloop()
