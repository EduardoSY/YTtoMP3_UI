from cgitb import text
import tkinter as tk
from tkinter import filedialog
from webbrowser import get
import pytube
import os
from moviepy.editor import *

downloadpath = os.getcwd()
ventana = tk.Tk()

def yt_mp3_download(url):
    yt = pytube.YouTube(url)
    nombreCancion.config(text = str("Título del video:\n" + yt.title))
    duracionCancion.config(text = str("Duración: " + str(yt.length//60) +":"+str("{:02d}".format(yt.length%60))))
    print(downloadpath)
    archivo_descarga = yt.streams.get_audio_only().download(output_path=downloadpath)
    #print("ITAG usado: ")
    #print(yt.streams.get_audio_only())
    #print(*yt.streams, sep='\n')

    audioclip = AudioFileClip(archivo_descarga)
    audioclip.write_audiofile(audioclip.filename.replace('.mp4', '.mp3'), bitrate='128k')
    #os.remove(archivo_descarga)


def setDownloadPath():
    pathDescarga = filedialog.askdirectory()
    global downloadpath
    downloadpath = pathDescarga
    print(downloadpath)
    pathlabel.config(text = downloadpath)

ventana.title('Youtube to Mp3')
ventana.geometry('300x200')
# Paso 1. Seleccionar ruta
tk.Label(ventana, text='1. Selecciona la ruta de descarga').pack()
pathlabel = tk.Label(ventana, text= downloadpath)
pathlabel.pack()
path_button = tk.Button(
    ventana,
    text='Seleccionar ruta',
    command = setDownloadPath
)
path_button.pack()

#Paso 2. Poner URL
tk.Label(ventana, text='URL').pack()
entry1 = tk.Entry(ventana)
entry1.pack()

download_button = tk.Button(
    ventana,
    text='Download',
    command = lambda: yt_mp3_download(entry1.get())
)
download_button.pack()

#3. Informacion de la cancion
nombreCancion = tk.Label(ventana, text='')
nombreCancion.pack()
duracionCancion = tk.Label(ventana, text='')
duracionCancion.pack()




ventana.mainloop() #Necesario para que la ventana aparezca y se mantenga abierta

