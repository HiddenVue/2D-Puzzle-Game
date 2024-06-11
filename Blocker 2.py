import Game
import Data
import pygame
import sys
import ctypes
import threading
import time

pygame.init()

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

try:
    BackgroundTileImage = pygame.transform.scale(pygame.image.load("Assets/BackgroundTile.png"),(50,50)) # 
    PlayerImage         = pygame.transform.scale(pygame.image.load("Assets/Player.png"),(50,50)) # @
    PlayerBodyImage     = pygame.transform.scale(pygame.image.load("Assets/PlayerBody.png"),(50,50)) 
    WallTileImage       = pygame.transform.scale(pygame.image.load("Assets/WallTile.png"),(50,50)) # #

    TelelportTileImage             = pygame.transform.scale(pygame.image.load("Assets/TeleportTile.png"),(50,50)) # < > ^ |
    DoubleTelelportTileImage       = pygame.transform.scale(pygame.image.load("Assets/DoubleTeleportTile.png"),(50,50)) # 1 2 3 4
    TripleTelelportTileImage       = pygame.transform.scale(pygame.image.load("Assets/TripleTeleportTile.png"),(50,50)) # 5 6 7 8

    EmptyTile                      = pygame.transform.scale(pygame.image.load("Assets/TripleTeleportTile.png"),(50,50)) # 9
    MovingEmeny                    = pygame.transform.scale(pygame.image.load("Assets/EmptyTile.png"),(50,50)) # 0 )

    ArrowImage                          = pygame.transform.scale(pygame.image.load("Assets/Arrow.png"),(50,50))
    ButtonFrame                          = pygame.transform.scale(pygame.image.load("Assets/ButtonFrame.png"),(200,50))
except:
    Mbox("Error","Unable to load assets",0)
    sys.exit()

DATA = None
DEVMODE = None

try:
    DATA = Data.LOAD()
    DEVMODE = DATA["DEVMODE"]
except:
    Mbox("Error","Unable to load data file",0)
    sys.exit()

CLOCK = pygame.time.Clock()

WINDOW = None

WINDOW = pygame.display.set_mode((1000,1000))

try:
    IconImage = pygame.transform.scale(pygame.image.load("Assets/Game Icon.ico"),(1000,1000))
except:
    Mbox("Error","Unable to load assets",0)
    sys.exit()

pygame.display.set_caption("Blocker 2")
pygame.display.set_icon(IconImage)

def DrawText(Window,Size,Position,FontPath,Text,Color):
    FONT = pygame.font.Font(FontPath, Size)
    TEXT = FONT.render(Text,True,Color)

    TEXTRECT = TEXT.get_rect()
    TEXTRECT.center = (Position[0] // 2, Position[1] // 2)

    Window.blit(TEXT,TEXTRECT)

def RenderBackgroundTiles(WINDOW):
    for Y in range(20):
        for X in range(20):
            WINDOW.blit(WallTileImage,(50 * X,50 * Y))

Close = False

def start_playlist(Window): 
 
    pygame.mixer.music.load("Sounds/Background Music.wav") 
    pygame.mixer.music.play() 
    for _ in range(85):
        if Close == True:
            break
        time.sleep(1)

    pygame.mixer.music.load("Sounds/Background Music2.wav") 
    pygame.mixer.music.play()
    for _ in range(85):
        if Close == True:
            break
        time.sleep(1)

    pygame.mixer.music.load("Sounds/Background Music3.wav")
    pygame.mixer.music.play()
    for _ in range(155):
        if Close == True:
            break
        time.sleep(1)

def MusicThread(Window):
    while Window != None:
        start_playlist(Window)

musicthread = threading.Thread(target=MusicThread,args=[WINDOW])
musicthread.start()

CLICKING = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and CLICKING == False:
            CLICKING = True

        if event.type == pygame.QUIT:
            Close = True
            pygame.quit()
            sys.exit()

    WINDOW.fill((0,0,0))

    RenderBackgroundTiles(WINDOW)

    if pygame.mouse.get_pos()[0] > 400 and pygame.mouse.get_pos()[0] < 600 and pygame.mouse.get_pos()[1] > 450 and pygame.mouse.get_pos()[1] < 500 and CLICKING:
        Game.RUNGAME(WINDOW,CLOCK,DEVMODE,DATA)

    if pygame.mouse.get_pos()[0] > 400 and pygame.mouse.get_pos()[0] < 600 and pygame.mouse.get_pos()[1] > 550 and pygame.mouse.get_pos()[1] < 600 and CLICKING:
        Close = True
        pygame.quit()
        sys.exit()

    if pygame.mouse.get_pos()[0] > 400 and pygame.mouse.get_pos()[0] < 600 and pygame.mouse.get_pos()[1] > 450 and pygame.mouse.get_pos()[1] < 500:
        WINDOW.blit(pygame.transform.scale(ButtonFrame,(212.5,65.5)),(395.5,445.5))

        
        DrawText(WINDOW,38,(1000,960),"Fonts/Font1.ttf","Play",(166,233,166)) # Shadow
        DrawText(WINDOW,38,(1000,950),"Fonts/Font1.ttf","Play",(211,255,211))
    else:
        WINDOW.blit(ButtonFrame,(400,450))
        
        DrawText(WINDOW,32,(1000,960),"Fonts/Font1.ttf","Play",(166,233,166)) # Shadow
        DrawText(WINDOW,32,(1000,950),"Fonts/Font1.ttf","Play",(211,255,211))

    if pygame.mouse.get_pos()[0] > 400 and pygame.mouse.get_pos()[0] < 600 and pygame.mouse.get_pos()[1] > 550 and pygame.mouse.get_pos()[1] < 600:
        WINDOW.blit(pygame.transform.scale(ButtonFrame,(212.5,65.5)),(395.5,545.5))

        DrawText(WINDOW,38,(1000,1160),"Fonts/Font1.ttf","Quit",(222,166,166)) # Shadow
        DrawText(WINDOW,38,(1000,1150),"Fonts/Font1.ttf","Quit",(255,211,211))
    else:
        WINDOW.blit(ButtonFrame,(400,550))

        DrawText(WINDOW,32,(1000,1160),"Fonts/Font1.ttf","Quit",(222,166,166)) # Shadow
        DrawText(WINDOW,32,(1000,1150),"Fonts/Font1.ttf","Quit",(255,211,211))

    DrawText(WINDOW,50,(1000,110),"Fonts/Font1.ttf","Blocker",(211,166,166)) # Shadow
    DrawText(WINDOW,50,(1000,100),"Fonts/Font1.ttf","Blocker",(255,166,166))

    DrawText(WINDOW,80,(1400,110),"Fonts/Font1.ttf","2",(211,122,122)) # Shadow
    DrawText(WINDOW,80,(1400,100),"Fonts/Font1.ttf","2",(255,122,122))


    pygame.display.update()

    CLICKING = False

