from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error
import tkinter as tk
from tkinter import filedialog
import magic
import sys
from sys import argv, exit
from os import path


def resource_path(relative_path):
    try:
        base_path = _MEIPASS
    except Exception:
        base_path = path.abspath(".")

    return path.join(base_path, relative_path)


def change_albumart(audio_path, albumart_path):
    mimetype = mime.from_file(albumart_path)

    audio = MP3(audio_path, ID3=ID3)
    try:
        audio.add_tags()
    except error:
        pass
    audio.tags.add(APIC(mime=mimetype, type=3, data=open(albumart_path, "rb").read()))
    audio.save()


def ask_for_audio():
    audio_path = filedialog.askopenfilename()
    if audio_path == "":
        exit()
    return audio_path


def ask_for_audio():
    albumart_path = filedialog.askopenfilename()
    if albumart_path == "":
        exit()
    return albumart_path


mime = magic.Magic(mime=True)

root = tk.Tk()
root.iconbitmap(resource_path("./icon.ico"))
root.withdraw()

if len(argv) == 3:
    audio_path = argv[1]
    albumart_path = argv[2]
else:
    audio_path = ask_for_audio()
    albumart_path = ask_for_image()

change_albumart(audio_path, albumart_path)
