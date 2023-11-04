import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x200")
        self.title("Music Player")
        self.setup_ui()

    def setup_ui(self):
        self.open_button = tk.Button(self, text="Open", command=self.open_file)
        self.open_button.pack(side="bottom", fill="x", padx=10, pady=10)

        self.play_button = tk.Button(self, text="Play", command=self.play_music)
        self.play_button.pack(side="bottom", fill="x", padx=10, pady=10)

        self.pause_button = tk.Button(self, text="Pause", command=self.pause_music)
        self.pause_button.pack(side="bottom", fill="x", padx=10, pady=10)

        self.stop_button = tk.Button(self, text="Stop", command=self.stop_music)
        self.stop_button.pack(side="bottom", fill="x", padx=10, pady=10)

    def open_file(self):
        file = filedialog.askopenfilename()
        pygame.mixer.init()
        pygame.mixer.music.load(file)

    def play_music(self):
        pygame.mixer.music.play()

    def pause_music(self):
        pygame.mixer.music.pause()

    def stop_music(self):
        pygame.mixer.music.stop()

if __name__ == "__main__":
    app = MusicPlayer()
    app.mainloop()