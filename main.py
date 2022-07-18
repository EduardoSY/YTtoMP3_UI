import tkinter as tk
import pytube
import os
from moviepy.editor import *

# def yt_mp3_download(url):
#     yt = pytube.YouTube(url)
#     print("Título del video....." + yt.title)
#     print("Duración............." + str(yt.length//60) +":"+str(yt.length%60))

#     archivo_descarga = yt.streams.get_audio_only().download(output_path="MusicaYT")
#     print("ITAG usado: ")
#     print(yt.streams.get_audio_only())
#     #print(*yt.streams, sep='\n')

#     audioclip = AudioFileClip(archivo_descarga)
#     audioclip.write_audiofile(audioclip.filename.replace('.mp4', '.mp3'), bitrate='128k')

ventana = tk.Tk()



ventana.title('Youtube to Mp3')
ventana.geometry('300x200')
tk.Label(ventana, text='URL').pack()
entry1 = tk.Entry(ventana)
entry1.pack()


def test():
    print("testee")

download_button = tk.Button(
    ventana,
    text='Download',
    command = test
)

download_button.pack()


ventana.mainloop() #Necesario para que la ventana aparezca y se mantenga abierta

