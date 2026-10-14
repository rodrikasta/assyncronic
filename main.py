#!/usr/bin/env python3
import tkinter as tk
import pygame
import re
from pathlib import Path


print("Assyncronic")
print("-----------")

def choose_song():
    songs_dir = Path(__file__).resolve().parent / "songs"
    lrc_files = {path.stem: path for path in songs_dir.glob("*.lrc")}
    mp3_files = {path.stem: path for path in songs_dir.glob("*.mp3")}
    available_songs = sorted(lrc_files.keys() & mp3_files.keys())

    if not available_songs:
        raise SystemExit(f"not found songs in {songs_dir}")

    print("Choose the song to play:")
    for index, song_name in enumerate(available_songs, start=1):
        print(f"{index}. {song_name}")

    while True:
        choice = input("Enter the number of the song: ")
        try:
            song_index = int(choice) - 1
        except ValueError:
            print("Enter a valid number.")
            continue

        if 0 <= song_index < len(available_songs):
            selected_song = available_songs[song_index]
            return str(lrc_files[selected_song]), str(mp3_files[selected_song])

        print(f"Choose a Song from 1 to {len(available_songs)}.")


lrc_file, mp3_file = choose_song()

def load_lrc(file_path):
    #Leera el archivo lrc y convertira los tiempos a milisegundos
    lyrics_lines = []
    #usamos una expresion para detectar los tiempos y las letras
    patron = re.compile(r'\[(\d+):(\d+\.\d+)\](.*)')

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            match = patron.match(line)
            if match:
                minutes = int(match.group(1))
                seconds = float(match.group(2))
                time_ms = int((minutes * 60 + seconds) * 1000)
                line = match.group(3).strip()

                if line:  # Check if the line is not empty
                    lyrics_lines.append({"time": time_ms, "line": line})
    return lyrics_lines

#load the lyrics from the selected lrc file
lyrics = load_lrc(lrc_file)

#setting the window
root = tk.Tk()
window_width = 400
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

start_x = (screen_width - window_width) // 2
start_y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{start_x}+{start_y}")
root.overrideredirect(True)
root.configure(bg="white")

label_lyrics = tk.Label(
    root,
    text="...",
    fg="black",
    bg="white",
    font=("Arial Narrow", 50),
    wraplength=window_width - 40,
    justify="left",
    anchor="w",
    padx=20,
)
label_lyrics.pack(expand=True, fill="both")

drag_offset_x = 0
drag_offset_y = 0


def start_window_drag(event):
    global drag_offset_x, drag_offset_y
    drag_offset_x = event.x_root - root.winfo_x()
    drag_offset_y = event.y_root - root.winfo_y()


def move_window(event):
    x = event.x_root - drag_offset_x
    y = event.y_root - drag_offset_y
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")


for widget in (root, label_lyrics):
    widget.bind("<ButtonPress-1>", start_window_drag)
    widget.bind("<B1-Motion>", move_window)

pygame.mixer.init()
pygame.mixer.music.load(mp3_file)
pygame.mixer.music.play()

current_index = 0


def update_lyrics():
    global current_index

    current_time = pygame.mixer.music.get_pos()
    if current_time == -1 or current_index >= len(lyrics):
        root.destroy()
        return

    next_lyric = lyrics[current_index]
    if current_time >= next_lyric["time"]:
        label_lyrics.config(text=next_lyric["line"])
        current_index += 1

    root.after(50, update_lyrics)


update_lyrics()
root.mainloop()

