import tkinter as tk
from tkinter import ttk
import psutil
import time

class SystemMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("System Monitor")
        self.root.geometry("300x100")

        self.cpu_label = ttk.Label(root, text="CPU 사용량: ")
        self.cpu_label.pack(pady=5)

        self.ram_label = ttk.Label(root, text="RAM 사용량: ")
        self.ram_label.pack(pady=5)

        self.update_info()

    def update_info(self):
        cpu_percent = psutil.cpu_percent(interval=0.1)
        ram_percent = psutil.virtual_memory().percent

        self.cpu_label.config(text=f"CPU 사용량: {cpu_percent}%")
        self.ram_label.config(text=f"RAM 사용량: {ram_percent}%")

        self.root.after(1000, self.update_info)  # 1초마다 업데이트

def main():
    root = tk.Tk()
    app = SystemMonitorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
