from app.mac import mac, signals

'''
Signals this module listents to:
1. When a message is received (signals.command_received)
==========================================================
'''
@signals.command_received.connect
def handle(message):
    if message.command == "hi":
        hi(message)
    elif message.command == "help": 
        help(message)

'''
Actual module code
==========================================================
'''
def hi(message):
    who_name = message.who_name
    answer = "Hi " + who_name
    mac.send_message(answer, message.conversation)
    mac.send_image("modules/hihelp/test.png", message.conversation)
    mac.send_video("modules/hihelp/test.mp4", message.conversation)
    
def help(message):
    answer = "hola, estoy en el help"
    mac.send_message(answer, message.conversation)
