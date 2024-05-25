import tkinter as tk
from tkinter import filedialog
import pygame

def play_music():
    file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def main():
    root = tk.Tk()
    root.title("음악 재생기")

    play_button = tk.Button(root, text="음악 재생", command=play_music)
    play_button.pack(pady=10)

    stop_button = tk.Button(root, text="음악 정지", command=stop_music)
    stop_button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
