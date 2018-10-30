from app.mac import mac, signals
import os
from colorama import Fore, Back, Style
import threading
import youtube_dl
'''
Signals this module listents to:
1. When a message is received (signals.command_received)
==========================================================
'''
@signals.command_received.connect
def handle(message):
    print(Back.GREEN +"MENSAJE RECIBIDO... "+message.command)
    #print(Back.RED + "Numero es..." + message.conversation)
    print(Style.RESET_ALL) 
    if message.command == "hi":
        hi(message)
    elif message.command == "help": 
        help(message)
    elif message.command.startswith("video"):
        video(message)
    elif message.command.startswith("audio"):
        audio(message)


'''
Youtube downloader methods
==========================================================
'''
#Esto lo descarga en un mp3 de 192kbps
def download_song(song_url, song_title):
    '''
    Downloads song from youtube-dl
    '''
    outtmpl = song_title + '.%(ext)s'
    ydl_opts = {
        'format': 'bestvideo[height<=480]+bestaudio[ext=m4a]/bestvideo+bestaudio',
        'outtmpl': outtmpl,

    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(song_url, download=True) 

'''
Actual module code
==========================================================
'''
def hi(message):
    who_name = message.who_name
    answer = "Bueeeena **" + who_name + "**"
    mac.send_message(answer, message.conversation)
    #mac.send_image("modules/hihelp/test.png", message.conversation)
    #mac.send_video("modules/hihelp/test.mp4", message.conversation)
    
def help(message):
    answer = "hola, estoy en el help"
    mac.send_message(answer, message.conversation)
    download_song("https://www.youtube.com/watch?v=CiIS5yRF_vA", "test")

def video(message):
    os.system("youtube-dl -f \'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4\' -o " + message.conversation[:11] + " " + message.command[5:])
    mac.send_message("Ya lo baje... Lo envio ahorita", message.conversation)
    print(Back.BLUE+"EL NOMBRE DEL VIDEO ES... " + message.conversation[:11] + ".mp4")
    print(Style.RESET_ALL)
    mac.send_video(message.conversation[:11] + ".mp4", message.conversation)

def audio(message):
    print("nombre audio ."+message.conversation[:11]+".")
    print("link es ."+message.command[5:]+".")
    os.system("youtube-dl -f bestaudio --extract-audio --audio-format mp3 -o " + message.conversation[:11] + ".mp3 " + message.command[5:])
    mac.send_message("Ya tengo el audio, te lo mando", message.conversation)
    mac.send_audio(message.conversation[:11] + ".mp3", message.conversation)

def printit():
    threading.Timer(180.0, printit).start()

for item in os.listdir():
    if item.endswith(".mp4"):
        #os.remove(os.path.join(dir_name, item))
        print("nombre archivo: "+item)
        os.remove(item)

    elif item.endswith(".mp3"):
        print("nombre archivo: "+item)
        os.remove(item)

printit()