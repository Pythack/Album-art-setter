from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error
import tkinter as tk
from tkinter import filedialog
import magic
from sys import argv

mime = magic.Magic(mime=True)

root = tk.Tk()
root.withdraw()


def changealbumart(audio_path, albumart_path):
    mimetype = mime.from_file(albumart_path)

    audio = MP3(audio_path, ID3=ID3)
    try:
        audio.add_tags()
    except error:
        pass
    audio.tags.add(APIC(mime=mimetype, type=3, data=open(albumart_path, "rb").read()))
    audio.save()


if len(argv) == 3:
    audio_path = argv[1]
    albumart_path = argv[2]
else:
    audio_path = filedialog.askopenfilename()
    albumart_path = filedialog.askopenfilename()
changealbumart(audio_path, albumart_path)
