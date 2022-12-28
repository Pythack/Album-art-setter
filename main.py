from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error
import tkinter as tk
from tkinter import filedialog
import magic

mime = magic.Magic(mime=True)

root = tk.Tk()
root.withdraw()

audio_path = filedialog.askopenfilename()
albumart_path = filedialog.askopenfilename()
mimetype = mime.from_file(albumart_path)

audio = MP3(audio_path, ID3=ID3)
try:
    audio.add_tags()
except error:
    pass
audio.tags.add(
    APIC(mime=mimetype, type=3, desc="Cover", data=open(albumart_path, "rb").read())
)
audio.save()
