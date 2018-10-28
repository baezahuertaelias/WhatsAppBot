from app.mac import mac, signals
import os
from colorama import Fore, Back, Style
import threading
'''
Signals this module listents to:
1. When a message is received (signals.command_received)
==========================================================
'''
@signals.command_received.connect
def handle(message):
    print(Back.GREEN +"MENSAJE RECIBIDO... "+message.command[7:])
    #print(Back.RED + "Numero es..." + message.conversation)
    print(Style.RESET_ALL) 
    if message.command == "hi":
        hi(message)
    elif message.command == "help": 
        help(message)
    elif message.command.startswith("youtube"):
        youtube(message)

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

def youtube(message):
    print(Back.BLUE +"Entonces en el comando youtube tenemos ."+message.command[7:])
    print(Style.RESET_ALL)
    os.system("youtube-dl -f \'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4\' -o " + message.conversation[:11] + " " + message.command[7:])
    mac.send_message("Ya lo baje... Lo envio ahorita", message.conversation)
    print("EL NOMBRE DEL VIDEO ES... " + message.conversation[:11] + ".mp4")
    print(os.listdir())
    mac.send_video(message.conversation[:11] + ".mp4", message.conversation)

def printit():
    threading.Timer(180.0, printit).start()

for item in os.listdir():
    if item.endswith(".mp4"):
        #os.remove(os.path.join(dir_name, item))
        print("nombre archivo: "+item)
        os.remove(item)

printit()