A minimalist, floating lyric player for the desktop. Assyncronic takes your local `.mp3` and `.lrc` files and displays the lyrics in sync. The interface is stripped down to the absolute essentials: a clean, borderless window with large text that you can freely drag anywhere on your screen.

## Features
* **Interactive Terminal Selection:** The script automatically scans a `songs/` directory for matching `.mp3` and `.lrc` pairs and provides a simple command-line menu to choose your track.
* **Borderless & Draggable UI:** The lyric window spawns in the center of your screen without system borders or title bars You can click and drag anywhere on the window to reposition it.
* **Clean Aesthetic:** Features a high-contrast white background with left-aligned, large Arial Narrow text for a modern and readable look.
* **Lightweight Audio Sync:** Built purely on `tkinter` for the interface and `pygame` for non-blocking audio playback.

## Prerequisites
Assyncronic requires **Python 3** and the `pygame` library.

```bash
pip install pygame
Directory Structure
The script requires a specific folder structure to detect your tracks. Create a songs/ folder in the exact same directory as main.py:

Plaintext
assyncronic/
├── main.py
└── songs/
    ├── duvet.mp3
    ├── duvet.lrc
    ├── drowned_in_dunkerk.mp3
    └── drowned_in_dunkerk.lrc
Note: Both the audio and lyric files must share the exact same name to be grouped together.

Usage
Run the main script from your terminal:

Bash
python main.py
The terminal will list all available songs. Type the number of the track you want to play, press Enter, and the floating lyric window will appear.