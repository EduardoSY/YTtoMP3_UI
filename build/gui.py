
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
import tkinter as tkinter
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog, font
from cgitb import text
from webbrowser import get
import pytube
import os
from moviepy.editor import *
from threading import Thread



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")
DOWNLOAD_PATH = os.getcwd()
YOUTUBE_URL = ""

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

def yt_mp3_download(url):
    global YOUTUBE_URL
    YOUTUBE_URL = str(url)
    entry_4.delete(0, len(entry_4.get()))
    info = pytube.YouTube(url)
    titulo_cancion.set(str(info.title))
    duracion_cancion.set(str(str(info.length//60) +":"+str("{:02d}".format(info.length%60))))

def setDownloadPath():
    pathDescarga = filedialog.askdirectory()
    global DOWNLOAD_PATH
    DOWNLOAD_PATH = pathDescarga
    print(DOWNLOAD_PATH)
    entry_1.delete(0, len(entry_1.get()))
    entry_1.insert(0, DOWNLOAD_PATH)
    
def download_process(select):
    print("PROCESO DESCARGA INICIADO")
    print(YOUTUBE_URL)
    yt = pytube.YouTube(YOUTUBE_URL)
    
    print(DOWNLOAD_PATH)
    if(select == "audio"):
        archivo_descarga = yt.streams.get_audio_only().download(output_path=DOWNLOAD_PATH)
        audioclip = AudioFileClip(archivo_descarga)
        audioclip.write_audiofile(audioclip.filename.replace('.mp4', '.mp3'), bitrate='128k')
        os.remove(archivo_descarga)
    elif(select == "video"):
        #video_descarga = yt.streams.get_by_resolution("720p").download(output_path=DOWNLOAD_PATH)
        get_video_download_opt(yt)
    else:
        print("Error: Opcion de descarga desconocida.")

def get_video_download_opt(x: pytube.YouTube):
    total_streams = x.streams.filter(file_extension='mp4', type="video")
    options = []
    for element in total_streams:
        if(element.itag != 134): #360p30fps ya se puede descargar con el itag 18
            options.append((element.itag, str(str(element.resolution) + str(element.fps)+"fps")))
    
    for x in options:
        print(x)



def download_thread(selection):
    """ Crea un nuevo hilo para realizar la descarga del video o audio

    Args:
        selection: Indica si la descarga va a ser de un audio o de un video
    """
    hilo = Thread(target=download_process, args=[selection])
    print("Nuevo hilo")
    hilo.start()
    # No uso hilo.join() porque estaríamos en el mismo caso que queriamos solucionar.
    # Si hiciera eso el hilo principal ha de esperar a que este hilo termine.

window.geometry("827x578")
window.title('You2Me')
window.configure(bg = "#FFFFFF")
logo = PhotoImage(
    file=relative_to_assets("Logo_You2Me.png"))
window.iconphoto(False, logo)
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 578,
    width = 827,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: download_thread("video"),
    relief="flat"
)
button_1.place(
    x=612.0,
    y=509.0,
    width=165.0,
    height=50.0
)

# button_0 = Button(
#     image=button_image_1,
#     borderwidth=0,
#     highlightthickness=0,
#     command=lambda: print("pepe"),
#     relief="flat"
# )
# button_0.place(
#     x=612.0,
#     y=460.0,
#     width=165.0,
#     height=50.0
# )

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: download_thread("audio"),
    relief="flat"
)
button_2.place(
    x=415.0,
    y=509.0,
    width=165.0,
    height=50.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command= setDownloadPath,
    relief="flat"
)
button_3.place(
    x=733.0,
    y=441.0,
    width=37.0,
    height=37.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    562.0,
    460.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#F9EAEA",
    highlightthickness=0,
    font=font.Font(family="Arial", size=12)
)
entry_1.insert(0, DOWNLOAD_PATH)
entry_1.place(
    x=424.0,
    y=430.0,
    width=276.0,
    height=58.0
)

canvas.create_text(
    415.0,
    397.0,
    anchor="nw",
    text="Ubicacion de guardado",
    fill="#000000",
    font=("Inter Regular", 20 * -1)
)

# DURACION - ENTRY
entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    733.0,
    346.0,
    image=entry_image_2
)
duracion_cancion = tkinter.StringVar()
entry_2 = Entry(
    bd=0,
    readonlybackground ="#F9EAEA",
    highlightthickness=0,
    textvariable=duracion_cancion,
    state="readonly",
    font=font.Font(family="Arial", size=12),
    justify='center'
)
#entry_2.insert(0, 'default text 2')

entry_2.place(
    x=699.0,
    y=316.0,
    width=68.0,
    height=58.0
)

canvas.create_text(
    689.0,
    284.0,
    anchor="nw",
    text="Duracion",
    fill="#000000",
    font=("Inter Regular", 20 * -1)
)

# TITULO - ENTRY
entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    544.5,
    346.0,
    image=entry_image_3
)
titulo_cancion = tkinter.StringVar()
entry_3 = Entry(
    bd=0,
    bg="#F9EAEA",
    highlightthickness=0,
    textvariable=titulo_cancion,
    font=font.Font(family="Arial", size=12)
)
#entry_3.insert(0, 'default text 3')
entry_3.place(
    x=424.0,
    y=316.0,
    width=241.0,
    height=58.0
)

canvas.create_text(
    414.0,
    284.0,
    anchor="nw",
    text="Titulo",
    fill="#000000",
    font=("Inter Regular", 20 * -1)
)

canvas.create_text(
    414.0,
    241.0,
    anchor="nw",
    text="Verifica la informacion",
    fill="#C4302B",
    font=("Inter Regular", 24 * -1)
)

canvas.create_rectangle(
    396.0,
    218.0,
    796.0,
    220.0,
    fill="#C4302B",
    outline="")

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: yt_mp3_download(entry_4.get()),
    relief="flat"
)
button_4.place(
    x=522.0,
    y=165.0,
    width=147.0,
    height=43.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    595.5,
    125.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#F9EAEA",
    highlightthickness=0,
    font=font.Font(family="Arial", size=12)
)
#entry_4.insert(0, 'default text 4')

entry_4.place(
    x=424.0,
    y=99.0,
    width=343.0,
    height=51.0
)

canvas.create_text(
    414.0,
    68.0,
    anchor="nw",
    text="URL del video",
    fill="#000000",
    font=("Inter Regular", 20 * -1)
)

canvas.create_text(
    414.0,
    24.0,
    anchor="nw",
    text="Introduce la URL",
    fill="#C4302B",
    font=("Inter Regular", 24 * -1)
)

canvas.create_rectangle(
    0.0,
    0.0,
    365.0,
    578.0,
    fill="#C4302B",
    outline="")

canvas.create_text(
    25.0,
    497.0,
    anchor="nw",
    text="Este es un proyecto personal con el unico proposito de\naprender sobre distintas herramientas. No me hago\nresponsable de un uso ulicito de esta aplicacion.",
    fill="#FFFFFF",
    font=("Inter Regular", 12 * -1)
)

canvas.create_text(
    21.0,
    266.0,
    anchor="nw",
    text="Encuentra la URL del video que deseas.\nPegala en la casilla URL del video y \npresiona Buscar. \n\nSi el video ha sido encontrado, aparece\nel titulo y la duracion en la parte de\nVerifica la informacion. Verifica que todo\nesta correcto, selecciona la ubicacion de\nguardado y, finalmente, presiona la opcion\nde guardado deseada.",
    fill="#FFFFFF",
    font=("Inter Regular", 16 * -1)
)

canvas.create_text(
    21.0,
    234.0,
    anchor="nw",
    text="Como usar:",
    fill="#FFFFFF",
    font=("Inter Bold", 20 * -1)
)

canvas.create_text(
    21.0,
    102.0,
    anchor="nw",
    text="You2Me es una aplicacion que\npermite guardar en tu dispositivo\nun video o audio procedente de\nYoutube.",
    fill="#FFFFFF",
    font=("Inter Regular", 20 * -1)
)

canvas.create_text(
    118.0,
    24.0,
    anchor="nw",
    text="You2Me",
    fill="#FFFFFF",
    font=("Inter Bold", 32 * -1)
)
window.resizable(False, False)
window.mainloop()
