import os
import pygame
import tkinter as tk
from tkinter import filedialog

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x250")

        pygame.mixer.init()

        self.is_paused = False
        self.current_song_index = 0
        self.songs = []

        self.create_widgets()

    def create_widgets(self):
        
        self.play_button = tk.Button(self.root, text="Play", command=self.play_music)
        self.play_button.pack(pady=5)

        self.pause_button = tk.Button(self.root, text="Pause/Resume", command=self.pause_resume_music)
        self.pause_button.pack(pady=5)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_music)
        self.stop_button.pack(pady=5)

        self.next_button = tk.Button(self.root, text="Next", command=self.next_song)
        self.next_button.pack(pady=5)

        self.prev_button = tk.Button(self.root, text="Previous", command=self.previous_song)
        self.prev_button.pack(pady=5)

        self.select_folder_button = tk.Button(self.root, text="Select Folder", command=self.select_folder)
        self.select_folder_button.pack(pady=5)

    def play_music(self):
        """
        Play the current song or start from the beginning of the list if stopped.
        """
        if not self.songs:
            print("No songs to play! Please select a folder first.")
            return

        if self.is_paused:
            pygame.mixer.music.unpause()
            self.is_paused = False
        else:
            pygame.mixer.music.load(self.songs[self.current_song_index])
            pygame.mixer.music.play()
            print(f"Playing: {os.path.basename(self.songs[self.current_song_index])}")

    def pause_resume_music(self):
        """
        Pause or resume the music depending on the current state.
        """
        if pygame.mixer.music.get_busy():
            if self.is_paused:
                pygame.mixer.music.unpause()
                self.is_paused = False
            else:
                pygame.mixer.music.pause()
                self.is_paused = True

    def stop_music(self):
        """
        Stop the music and reset the pause state.
        """
        pygame.mixer.music.stop()
        self.is_paused = False

    def next_song(self):
        """
        Play the next song in the playlist.
        """
        if self.songs:
            self.current_song_index = (self.current_song_index + 1) % len(self.songs)
            pygame.mixer.music.load(self.songs[self.current_song_index])
            pygame.mixer.music.play()
            print(f"Playing: {os.path.basename(self.songs[self.current_song_index])}")

    def previous_song(self):
        """
        Play the previous song in the playlist.
        """
        if self.songs:
            self.current_song_index = (self.current_song_index - 1) % len(self.songs)
            pygame.mixer.music.load(self.songs[self.current_song_index])
            pygame.mixer.music.play()
            print(f"Playing: {os.path.basename(self.songs[self.current_song_index])}")

    def select_folder(self):
        """
        Open a dialog to select a folder and load all music files from that folder.
        """
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.songs = [os.path.join(folder_path, file) for file in os.listdir(folder_path)
                          if file.endswith(('.mp3', '.wav'))]
            self.songs.sort()
            print(f"Loaded {len(self.songs)} songs from {folder_path}")

            if self.songs:
                self.current_song_index = 0
                self.play_music()

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
