loading = """

█    ████▄ ██   ██▄   ▄█    ▄     ▄▀          
█    █   █ █ █  █  █  ██     █  ▄▀            
█    █   █ █▄▄█ █   █ ██ ██   █ █ ▀▄          
███▄ ▀████ █  █ █  █  ▐█ █ █  █ █   █         
    ▀         █ ███▀   ▐ █  █ █  ███ ██ ██ ██ 
             █           █   ██               
            ▀                                 
"""

print(loading)

#in python
import os
from pprint import pprint
import re
import socket
from time import sleep
import random
import hashlib
import sys
import string

#no in python
import requests
import qrcode
from pystyle import *
from faker import Faker
import uuid
import fake_useragent

bannerint = 1
colorint = 1

banner = """─══════════════════════════════════════════════════════════════════════════════════════════════════─
 ▄▄▄       ▄▄▄▄     ██████ ▄▄▄█████▓ ██▀███   ▄▄▄       ▄████▄  ▄▄▄█████▓ ▄████▄   ▄▄▄     ▄▄▄█████▓ 
▒████▄    ▓█████▄ ▒██    ▒ ▓  ██▒ ▓▒▓██ ▒ ██▒▒████▄    ▒██▀ ▀█  ▓  ██▒ ▓▒▒██▀ ▀█  ▒████▄   ▓  ██▒ ▓▒
▒██  ▀█▄  ▒██▒ ▄██░ ▓██▄   ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▒ ▓██░ ▒░▒▓█    ▄ ▒██  ▀█▄ ▒ ▓██░ ▒░
░██▄▄▄▄██ ▒██░█▀    ▒   ██▒░ ▓██▓ ░ ▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒░ ▓██▓ ░ ▒▓▓▄ ▄██▒░██▄▄▄▄██░ ▓██▓ ░ 
 ▓█   ▓██▒░▓█  ▀█▓▒██████▒▒  ▒██▒ ░ ░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░  ▒██▒ ░ ▒ ▓███▀ ░ ▓█   ▓██▒ ▒██▒ ░ 
 ▒▒   ▓▒█░░▒▓███▀▒▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░  ▒ ░░   ░ ░▒ ▒  ░ ▒▒   ▓▒█░ ▒ ░░   
  ▒   ▒▒ ░▒░▒   ░ ░ ░▒  ░ ░    ░      ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒       ░      ░  ▒     ▒   ▒▒ ░   ░    
  ░   ▒    ░    ░ ░  ░  ░    ░        ░░   ░   ░   ▒   ░          ░      ░          ░   ▒    ░      
      ░  ░ ░            ░              ░           ░  ░░ ░               ░ ░            ░  ░        
                ░                                      ░                 ░                          
─══════════════════════════════════════════════════════════════════════════════════════════════════─
"""

banner2 = """─═════════════════════════════════════════════════════════════════════════════════════════─
 █████╗ ██████╗ ███████╗████████╗██████╗  █████╗  ██████╗████████╗ ██████╗ █████╗ ████████╗
██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗╚══██╔══╝
███████║██████╔╝███████╗   ██║   ██████╔╝███████║██║        ██║   ██║     ███████║   ██║   
██╔══██║██╔══██╗╚════██║   ██║   ██╔══██╗██╔══██║██║        ██║   ██║     ██╔══██║   ██║   
██║  ██║██████╔╝███████║   ██║   ██║  ██║██║  ██║╚██████╗   ██║   ╚██████╗██║  ██║   ██║   
╚═╝  ╚═╝╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝╚═╝  ╚═╝   ╚═╝   
─═════════════════════════════════════════════════════════════════════════════════════════─
"""

banner3 = """─════════════════════════════════════════════════════════════════════════════════════════════════════════════─
           88                                                                                                   
           88                      ,d                                       ,d                           ,d     
           88                      88                                       88                           88     
,adPPYYba, 88,dPPYba,  ,adPPYba, MM88MMM 8b,dPPYba, ,adPPYYba,  ,adPPYba, MM88MMM ,adPPYba, ,adPPYYba, MM88MMM  
""     `Y8 88P'    "8a I8[    ""   88    88P'   "Y8 ""     `Y8 a8"     ""   88   a8"     "" ""     `Y8   88     
,adPPPPP88 88       d8  `"Y8ba,    88    88         ,adPPPPP88 8b           88   8b         ,adPPPPP88   88     
88,    ,88 88b,   ,a8" aa    ]8I   88,   88         88,    ,88 "8a,   ,aa   88,  "8a,   ,aa 88,    ,88   88,    
`"8bbdP"Y8 8Y"Ybbd8"'  `"YbbdP"'   "Y888 88         `"8bbdP"Y8  `"Ybbd8"'   "Y888 `"Ybbd8"' `"8bbdP"Y8   "Y888  
─════════════════════════════════════════════════════════════════════════════════════════════════════════════─
"""

banner4 = """─══════════════════════════════════════════════════════════─
 ▄▄▄· ▄▄▄▄· .▄▄ · ▄▄▄▄▄▄▄▄   ▄▄▄·  ▄▄· ▄▄▄▄▄ ▄▄·  ▄▄▄· ▄▄▄▄▄
▐█ ▀█ ▐█ ▀█▪▐█ ▀. •██  ▀▄ █·▐█ ▀█ ▐█ ▌▪•██  ▐█ ▌▪▐█ ▀█ •██  
▄█▀▀█ ▐█▀▀█▄▄▀▀▀█▄ ▐█.▪▐▀▀▄ ▄█▀▀█ ██ ▄▄ ▐█.▪██ ▄▄▄█▀▀█  ▐█.▪
▐█ ▪▐▌██▄▪▐█▐█▄▪▐█ ▐█▌·▐█•█▌▐█ ▪▐▌▐███▌ ▐█▌·▐███▌▐█ ▪▐▌ ▐█▌·
 ▀  ▀ ·▀▀▀▀  ▀▀▀▀  ▀▀▀ .▀  ▀ ▀  ▀ ·▀▀▀  ▀▀▀ ·▀▀▀  ▀  ▀  ▀▀▀ 
 ─══════════════════════════════════════════════════════════─
"""

banner5 = """─══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════─
   ▄████████ ▀█████████▄     ▄████████     ███        ▄████████    ▄████████  ▄████████     ███      ▄████████    ▄████████     ███     
  ███    ███   ███    ███   ███    ███ ▀█████████▄   ███    ███   ███    ███ ███    ███ ▀█████████▄ ███    ███   ███    ███ ▀█████████▄ 
  ███    ███   ███    ███   ███    █▀     ▀███▀▀██   ███    ███   ███    ███ ███    █▀     ▀███▀▀██ ███    █▀    ███    ███    ▀███▀▀██ 
  ███    ███  ▄███▄▄▄██▀    ███            ███   ▀  ▄███▄▄▄▄██▀   ███    ███ ███            ███   ▀ ███          ███    ███     ███   ▀ 
▀███████████ ▀▀███▀▀▀██▄  ▀███████████     ███     ▀▀███▀▀▀▀▀   ▀███████████ ███            ███     ███        ▀███████████     ███     
  ███    ███   ███    ██▄          ███     ███     ▀███████████   ███    ███ ███    █▄      ███     ███    █▄    ███    ███     ███     
  ███    ███   ███    ███    ▄█    ███     ███       ███    ███   ███    ███ ███    ███     ███     ███    ███   ███    ███     ███     
  ███    █▀  ▄█████████▀   ▄████████▀     ▄████▀     ███    ███   ███    █▀  ████████▀     ▄████▀   ████████▀    ███    █▀     ▄████▀   
                                                     ███    ███                                                                         
─══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════─
"""

banner6 = """─════════════════════════════════════════════════════════════════════════════════════════════════════════─
           █████              █████                                  █████                        █████   
          ░░███              ░░███                                  ░░███                        ░░███    
  ██████   ░███████   █████  ███████   ████████   ██████    ██████  ███████    ██████   ██████   ███████  
 ░░░░░███  ░███░░███ ███░░  ░░░███░   ░░███░░███ ░░░░░███  ███░░███░░░███░    ███░░███ ░░░░░███ ░░░███░   
  ███████  ░███ ░███░░█████   ░███     ░███ ░░░   ███████ ░███ ░░░   ░███    ░███ ░░░   ███████   ░███    
 ███░░███  ░███ ░███ ░░░░███  ░███ ███ ░███      ███░░███ ░███  ███  ░███ ███░███  ███ ███░░███   ░███ ███
░░████████ ████████  ██████   ░░█████  █████    ░░████████░░██████   ░░█████ ░░██████ ░░████████  ░░█████ 
 ░░░░░░░░ ░░░░░░░░  ░░░░░░     ░░░░░  ░░░░░      ░░░░░░░░  ░░░░░░     ░░░░░   ░░░░░░   ░░░░░░░░    ░░░░░  
─════════════════════════════════════════════════════════════════════════════════════════════════════════─
"""

dei = """
╔═════════════════════════════════════════╦═════════════════════════════════════════╦═══════════════════════════╗
║ Free Edition                            ║ Tool by Abstraction                     ║ Version - Alpha 0.21      ║
╠═════════════════════════════════════════╬═════════════════════════════════════════╬═══════════════════════════╣
║ 1) Пробив по айпи                       ║ 7) Преобразование хостнейма в IP-адрес  ║ 0) Выход                  ║
║ 2) Пробив по номеру телефона            ║ 8) Генерация фио                        ║                           ║
║ 3) Изменение текста                     ║ 9) Бомбер [Не работает]                 ║                           ║
║ 4) Проверка цены биткоина               ║ 10) Преобразование текста в MD5-хеш     ║                           ║
║ 5) Генерация QR-кода                    ║ 11) Майнкрафт                           ║                           ║
║ 6) Сгенерировать пароли                 ║ 12) Изменение худа                      ║                           ║
╚═════════════════════════════════════════╩═════════════════════════════════════════╩═══════════════════════════╝
"""

def bombermenu(number):
    try:
        response = requests.post("https://shop.vsk.ru/ajax/auth/postSmsX/", headers={"user_agent": fake_useragent.UserAgent().random}, 
            data={"phone": number})
        colorprint(f"Готово! псс.. {response}")
    except:
        colorprint("Ошибка")

def get_ip_by_hostname():
    hostname = input(colorik('Please enter a website address(URL): '))
    try:
        return f'Hostname: {hostname}\nIP address: {socket.gethostbyname(hostname)}'
    except socket.gaierror as error:
        return f'Invalid Hostname - {error}'

def generate_password(length):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for i in range(length))
    return password

def clear_console():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

def colorprint(txt):
    if colorint == 1:
        print(Colorate.Horizontal(Colors.red_to_yellow,txt))
    if colorint == 2:
        print(Colorate.Horizontal(Colors.purple_to_blue,txt))
    if colorint == 3:
        print(Colorate.Horizontal(Colors.green_to_cyan,txt))
    if colorint == 4:
        print(Colorate.Horizontal(Colors.purple_to_red,txt))
    if colorint == 5:
        print(Colorate.Horizontal(Colors.white_to_green,txt))

def colorik(txt):
    if colorint == 1:
        return Colorate.Horizontal(Colors.red_to_yellow,txt)
    if colorint == 2:
        return Colorate.Horizontal(Colors.purple_to_blue,txt)
    if colorint == 3:
        return Colorate.Horizontal(Colors.green_to_cyan,txt)
    if colorint == 4:
        return Colorate.Horizontal(Colors.purple_to_red, txt)
    if colorint == 5:
        return Colorate.Horizontal(Colors.white_to_green, txt)

def colorchange():
    global colorint
    clear_console()
    colorprint("""

▄█▄    ████▄ █    ████▄ █▄▄▄▄        ▄▄▄▄▄   ▄███▄     ▄▄▄▄▀ ▄▄▄▄▀ ▄█    ▄     ▄▀    ▄▄▄▄▄   
█▀ ▀▄  █   █ █    █   █ █  ▄▀       █     ▀▄ █▀   ▀ ▀▀▀ █ ▀▀▀ █    ██     █  ▄▀     █     ▀▄ 
█   ▀  █   █ █    █   █ █▀▀▌      ▄  ▀▀▀▀▄   ██▄▄       █     █    ██ ██   █ █ ▀▄ ▄  ▀▀▀▀▄   
█▄  ▄▀ ▀████ ███▄ ▀████ █  █       ▀▄▄▄▄▀    █▄   ▄▀   █     █     ▐█ █ █  █ █   █ ▀▄▄▄▄▀    
▀███▀            ▀        █                  ▀███▀    ▀     ▀       ▐ █  █ █  ███            
                         ▀                                            █   ██                 
1 - Красно-желтый [Лиса]
2 - Сине-фиолетовый [+-]
3 - Зелено-голубой [Токсичный]
4 - Красно-фиолетовый [+-]
5 - Зелено-белый [+-]
6 - Вернуться
""")
    mmmm = int(input(colorik("Выберите пункт:")))
    if mmmm == 1:
        sleep(0.5)
        colorint = 1
        colorprint("Изменено.")
        sleep(0.5)
        colorchange()
    if mmmm == 2:
        sleep(0.5)
        colorint = 2
        colorprint("Изменено.")
        sleep(0.5)
        colorchange()
    if mmmm == 3:
        sleep(0.5)
        colorint = 3
        colorprint("Изменено.")
        sleep(0.5)
        colorchange()
    if mmmm == 4:
        sleep(0.5)
        colorint = 4
        colorprint("Изменено.")
        sleep(0.5)
        colorchange()
    if mmmm == 5:
        sleep(0.5)
        colorint = 5
        colorprint("Изменено.")
        sleep(0.5)
        colorchange()
    if mmmm == 6:
        hudsettings()
    else:
        colorprint("Ошибка")

def stylesettings():
    global bannerint
    clear_console()
    colorprint("""

   ▄▄▄▄▄      ▄▄▄▄▀ ▀▄    ▄ █     ▄███▄          ▄▄▄▄▄   ▄███▄     ▄▄▄▄▀ ▄▄▄▄▀ ▄█    ▄     ▄▀    ▄▄▄▄▄   
  █     ▀▄ ▀▀▀ █      █  █  █     █▀   ▀        █     ▀▄ █▀   ▀ ▀▀▀ █ ▀▀▀ █    ██     █  ▄▀     █     ▀▄ 
▄  ▀▀▀▀▄       █       ▀█   █     ██▄▄        ▄  ▀▀▀▀▄   ██▄▄       █     █    ██ ██   █ █ ▀▄ ▄  ▀▀▀▀▄   
 ▀▄▄▄▄▀       █        █    ███▄  █▄   ▄▀      ▀▄▄▄▄▀    █▄   ▄▀   █     █     ▐█ █ █  █ █   █ ▀▄▄▄▄▀    
             ▀       ▄▀         ▀ ▀███▀                  ▀███▀    ▀     ▀       ▐ █  █ █  ███            
                                                                                  █   ██                 
1 - Bloody
2 - ANSII Shadow
3 - Universe
4 - Elite
5 - Delta Corps Priest 1
6 - DOS Rebel
7 - Вернуться
""")
    m = int(input(colorik("Выберите пункт:")))
    if m == 1:
        bannerint = 1
        colorprint("Изменено.")
        sleep(0.5)
        stylesettings()
    if m == 2:
        bannerint = 2
        colorprint("Изменено.")
        sleep(0.5)
        stylesettings()
    if m == 3:
        bannerint = 3
        colorprint("Изменено.")
        sleep(0.5)
        stylesettings()
    if m == 4:
        bannerint = 4
        colorprint("Изменено.")
        sleep(0.5)
        stylesettings()
    if m == 5:
        bannerint = 5
        colorprint("Изменено.")
        sleep(0.5)
        stylesettings()
    if m == 6:
        bannerint = 6
        colorprint("Изменено.")
        sleep(0.5)
        stylesettings()
    if m == 7:
        hudsettings()

def hudsettings():
    clear_console()
    colorprint("""

 ▄  █   ▄   ██▄          ▄▄▄▄▄   ▄███▄     ▄▄▄▄▀ ▄▄▄▄▀ ▄█    ▄     ▄▀    ▄▄▄▄▄   
█   █    █  █  █        █     ▀▄ █▀   ▀ ▀▀▀ █ ▀▀▀ █    ██     █  ▄▀     █     ▀▄ 
██▀▀█ █   █ █   █     ▄  ▀▀▀▀▄   ██▄▄       █     █    ██ ██   █ █ ▀▄ ▄  ▀▀▀▀▄   
█   █ █   █ █  █       ▀▄▄▄▄▀    █▄   ▄▀   █     █     ▐█ █ █  █ █   █ ▀▄▄▄▄▀    
   █  █▄ ▄█ ███▀                 ▀███▀    ▀     ▀       ▐ █  █ █  ███            
  ▀    ▀▀▀                                                █   ██                 
                                                                                 
1 - Изменить стиль баннера в главном меню
2 - Изменить цвет текста
3 - Вернуться в главное меню
""")
    s = int(input(colorik("Выберите пункт: ")))
    if s == 1:
        stylesettings()
    if s == 2:
        colorchange()
    if s == 3:
        clear_console()
        main()
    else:
        colorprint("Ошибка")


clear_console()
def printbanner():
    if bannerint == 1:
        colorprint(banner)
    if bannerint == 2:
        colorprint(banner2)
    if bannerint == 3:
        colorprint(banner3)
    if bannerint == 4:
        colorprint(banner4)
    if bannerint == 5:
        colorprint(banner5)
    if bannerint == 6:
        colorprint(banner6)


def minecraftmenu():
    colorprint("""

█▀▄▀█ ▄█    ▄   ▄███▄   ▄█▄    █▄▄▄▄ ██   ▄████     ▄▄▄▄▀     █▀▄▀█ ▄███▄      ▄     ▄   
█ █ █ ██     █  █▀   ▀  █▀ ▀▄  █  ▄▀ █ █  █▀   ▀ ▀▀▀ █        █ █ █ █▀   ▀      █     █  
█ ▄ █ ██ ██   █ ██▄▄    █   ▀  █▀▀▌  █▄▄█ █▀▀        █        █ ▄ █ ██▄▄    ██   █ █   █ 
█   █ ▐█ █ █  █ █▄   ▄▀ █▄  ▄▀ █  █  █  █ █         █         █   █ █▄   ▄▀ █ █  █ █   █ 
   █   ▐ █  █ █ ▀███▀   ▀███▀    █      █  █       ▀             █  ▀███▀   █  █ █ █▄ ▄█ 
  ▀      █   ██                 ▀      █    ▀                   ▀           █   ██  ▀▀▀  
                                      ▀                                                  
╔═════════════════════════╦═══════════╗
║ 1) Создать базу для рп  ║ 0) Назад  ║
╚═════════════════════════╩═══════════╝
""")
    msg = int(input(colorik("Выберите пункт: ")))
    if msg == 1:
        namepkg = input(colorik("Введите название пака: "))
        os.mkdir(namepkg)
        os.chdir(namepkg)
        f = open("manifest.json", "w+")
        f.write('''{
   "format_version" : 1,
   "header" : {
      "description" : "generated by abstractcat",
      "name" : "generated by abstractcat",
      "uuid" : "'''+str(uuid.uuid4())+'''",
      "version" : [ 1, 0, 0 ]
   },
   "metadata" : {
      "authors" : [ "ABSTRACT"],
      "url" : "https://t.me/arbuziypublic"
   },
   "modules" : [
      {
         "description" :"generated by abstractcat",
         "type" : "resources",
         "uuid" : "'''+str(uuid.uuid4())+'''",
         "version" : [ 1, 0, 0 ]
      }
   ]
}

''')
        f.close()
        os.mkdir("textures")
        os.chdir("textures")
        os.mkdir("items")
        os.mkdir("blocks")
        colorprint("Создано.")
        minecraftmenu()
    if msg == 0:
        clear_console()
        main()


def main():
    printbanner()
    colorprint(dei)
    msg = int(input(colorik('Выберите пункт: ')))
    if msg == 1:
        ip = input(colorik("Введите айпи: "))
        try:
            response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
            data = {
                '[IP]': response.get('query'),
                '[Int prov]': response.get('isp'),
                '[Org]': response.get('org'),
                '[Country]': response.get('country'),
                '[Region Name]': response.get('regionName'),
                '[City]': response.get('city'),
                '[ZIP]': response.get('zip'),
                '[Lat]': response.get('lat'),
                '[Lon]': response.get('lon'),
            }
            for k, v in data.items():
                colorprint(f'{k}: {v}')
        except:
            colorprint("Ошибка!")
        main()
    if msg == 2:
        num = input(colorik("Введите номер телефона (7xxx...): "))
        response = requests.get(f"https://mobile-location.org/emulator/check?driver=geo&country=RU&provider=phone&uid=+{num}&mode=undefined&_=1698494081981").json()
        pprint(response)
        main()
    if msg == 3:
        txt = input(colorik("Введите текст: "))
        txt = txt.lower()
        txt = txt.replace("а", "@")
        txt = txt.replace("г", "7")
        txt = txt.replace("д", "d")
        txt = txt.replace("е", "€")
        txt = txt.replace("з", "3")
        txt = txt.replace("и", "u")
        txt = txt.replace("к", "k")
        txt = txt.replace("л", "l")
        txt = txt.replace("м", "m")
        txt = txt.replace("о", "0")
        txt = txt.replace("п", "n")
        txt = txt.replace("т", "t")
        colorprint(txt)
        main()
    if msg == 4:
        req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
        response = req.json()
        data_koron = response["btc_usd"]["sell"]
        colorprint(f"1 Биткоин - {data_koron} долларов")
        main()
    if msg == 5:
        img = qrcode.make(input(colorik("Введите ссылку: ")))
        img.save(input(colorik("Введите название файла: ")))
        colorprint("QR-Code был сгенерирован.")
        main()
    if msg == 6:
        length = int(input(colorik("Длина пароля: ")))
        shtuki = int(input(colorik("Число паролей: ")))
        autohash = input(colorik("Автохэширование в MD5? y/n: "))
        fileset = input(colorik("Засунуть пароли в файл? y/n: "))
        for _ in range(shtuki):
            if autohash == "y":
                if fileset == "y":
                    Set = hashlib.md5(generate_password(length).encode()).hexdigest()
                    GeneratePass = "".join(random.sample(Set,int(length)))
                    with open("passwords.txt", "a") as file:
                        file.write(GeneratePass + "\n\n")
                        file.close()
                    colorprint("Успешно!")
                else:
                    colorprint(hashlib.md5(generate_password(length).encode()).hexdigest())
            else:
                if fileset == "y":
                    Set = generate_password(length)
                    GeneratePass = "".join(random.sample(Set,int(length)))
                    with open("passwords.txt", "a") as file:
                        file.write(GeneratePass + "\n\n")
                        file.close()
                    colorprint("Успешно!")
                else:
                    colorprint(generate_password(length))
        main()
    if msg == 7:
        colorprint(get_ip_by_hostname())
        main()
    if msg == 8:
        fake = Faker("ru_RU")
        colorprint(fake.name())
        main()
    if msg == 9:
        num = input(colorik("Введите номер телефона [+7xx..]: "))
        bombermenu(num)
        main()
    if msg == 10:
        txt = input(colorik("Введите текст: "))
        md5_hash = hashlib.md5(txt.encode()).hexdigest()
        print(colorik(f"MD5 хеш для вводных данных:{md5_hash}"))
        main()
    if msg == 11:
        minecraftmenu()
    if msg == 12:
        hudsettings()
    if msg == 993:
        x = 1000 - 7
        while x > 7:
            colorprint(f"{x} - 7 = {x-7}")
            x -= 7
            sleep(0.05)
        colorprint('нихуя ты гуль')
        main()
    if msg == 0:
        exit
    else:
        colorprint("Такой команды не существует!")
        main()


main()