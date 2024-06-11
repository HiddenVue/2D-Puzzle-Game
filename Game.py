import pygame
import sys
import math
import Player
import time
import ctypes
import winsound
import json

pygame.init()

Close = False

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

def RenderBackgroundTiles(WINDOW):
    for Y in range(20):
        for X in range(20):
            WINDOW.blit(BackgroundTileImage,(50 * X,50 * Y))

def RenderLevel(WINDOW,ENTITYS):
    for ENTITY in ENTITYS:
        if ENTITY[2] == "Wall":
            WINDOW.blit(WallTileImage,(ENTITY[0],ENTITY[1]))

        if ENTITY[2] == "TripleTeleportRight":
            WINDOW.blit(TripleTelelportTileImage,(ENTITY[0],ENTITY[1]))
        if ENTITY[2] == "TripleTeleportLeft":
            WINDOW.blit(pygame.transform.rotate(TripleTelelportTileImage,-180),(ENTITY[0],ENTITY[1]))
        if ENTITY[2] == "TripleTeleportUp":
            WINDOW.blit(pygame.transform.rotate(TripleTelelportTileImage,90),(ENTITY[0],ENTITY[1]))
        if ENTITY[2] == "TripleTeleportDown":
            WINDOW.blit(pygame.transform.rotate(TripleTelelportTileImage,-90),(ENTITY[0],ENTITY[1]))

        if ENTITY[2] == "DoubleTeleportRight":
            WINDOW.blit(DoubleTelelportTileImage,(ENTITY[0],ENTITY[1]))
        if ENTITY[2] == "DoubleTeleportLeft":
            WINDOW.blit(pygame.transform.rotate(DoubleTelelportTileImage,-180),(ENTITY[0],ENTITY[1]))
        if ENTITY[2] == "DoubleTeleportUp":
            WINDOW.blit(pygame.transform.rotate(DoubleTelelportTileImage,90),(ENTITY[0],ENTITY[1]))
        if ENTITY[2] == "DoubleTeleportDown":
            WINDOW.blit(pygame.transform.rotate(DoubleTelelportTileImage,-90),(ENTITY[0],ENTITY[1]))

        if ENTITY[2] == "TeleportRight":
            WINDOW.blit(TelelportTileImage,(ENTITY[0],ENTITY[1]))
        if ENTITY[2] == "TeleportLeft":
            WINDOW.blit(pygame.transform.rotate(TelelportTileImage,-180),(ENTITY[0],ENTITY[1]))
        if ENTITY[2] == "TeleportUp":
            WINDOW.blit(pygame.transform.rotate(TelelportTileImage,90),(ENTITY[0],ENTITY[1]))
        if ENTITY[2] == "TeleportDown":
            WINDOW.blit(pygame.transform.rotate(TelelportTileImage,-90),(ENTITY[0],ENTITY[1]))

        if ENTITY[2] == "PlayerBody":
            WINDOW.blit(PlayerBodyImage,(ENTITY[0],ENTITY[1]))
        if ENTITY[2] == "Player":
            WINDOW.blit(PlayerImage,(ENTITY[0],ENTITY[1]))

def LOADLEVEL(LEVEL,DATA):
    LEVELENTITYSWITHLOGIC = []
    LEVELENTITYS = []

    for Y,Row in enumerate(DATA["Levels"]["LEVEL" + str(LEVEL)]["LevelData"]):
        for X,Letter in enumerate(Row):
            if Letter == "5":
                LEVELENTITYS.append((50 * X,50 * Y,"TripleTeleportRight"))
            if Letter == "6":
                LEVELENTITYS.append((50 * X,50 * Y,"TripleTeleportLeft"))
            if Letter == "7":
                LEVELENTITYS.append((50 * X,50 * Y,"TripleTeleportUp"))
            if Letter == "8":
                LEVELENTITYS.append((50 * X,50 * Y,"TripleTeleportDown"))

            if Letter == "1":
                LEVELENTITYS.append((50 * X,50 * Y,"DoubleTeleportRight"))
            if Letter == "2":
                LEVELENTITYS.append((50 * X,50 * Y,"DoubleTeleportLeft"))
            if Letter == "3":
                LEVELENTITYS.append((50 * X,50 * Y,"DoubleTeleportUp"))
            if Letter == "4":
                LEVELENTITYS.append((50 * X,50 * Y,"DoubleTeleportDown"))

            if Letter == ">":
                LEVELENTITYS.append((50 * X,50 * Y,"TeleportRight"))
            if Letter == "<":
                LEVELENTITYS.append((50 * X,50 * Y,"TeleportLeft"))
            if Letter == "^":
                LEVELENTITYS.append((50 * X,50 * Y,"TeleportUp"))
            if Letter == "|":
                LEVELENTITYS.append((50 * X,50 * Y,"TeleportDown"))

            if Letter == "#":
                LEVELENTITYS.append((50 * X,50 * Y,"Wall"))
            if Letter == "@":
                PlayerData = [50 * X,50 * Y,"Player"]
                LEVELENTITYS.append(PlayerData)

                PlayerClass = Player.player(PlayerData,None)
                LEVELENTITYSWITHLOGIC.append(PlayerClass)

    return LEVELENTITYS,LEVELENTITYSWITHLOGIC

def RUNENTITYLOGIC(ENTITYSWITHLOGIC):
    for ENTITY in ENTITYSWITHLOGIC:
        ENTITY.LOGIC()

def DrawText(Window,Size,Position,FontPath,Text,Color):
    FONT = pygame.font.Font(FontPath, Size)
    TEXT = FONT.render(Text,True,Color)

    TEXTRECT = TEXT.get_rect()
    TEXTRECT.center = (Position[0] // 2, Position[1] // 2)

    Window.blit(TEXT,TEXTRECT)

def RUNGAME(WINDOW,CLOCK,DEVMODE,DATA):
    LEVEL = int(1)
    LEVELENTITYS,LEVELENTITYSWITHLOGIC = LOADLEVEL(LEVEL,DATA)

    for ENTITY in LEVELENTITYSWITHLOGIC:
        ENTITY.GETENTITYS(LEVELENTITYS)
    
    TransparentSurface = pygame.Surface((1000,1000), pygame.SRCALPHA)

    CLICKING = False
    
    while WINDOW:
        CLOCK.tick(60)

        if DEVMODE: pygame.display.set_caption(f"Blocker 2 | DEVMODE ENABLED | FPS: {math.floor(CLOCK.get_fps())} |")
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and CLICKING == False:
                CLICKING = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    with open("Data.json", "w") as File:
                        json.dump(DATA,File,indent=6)
                    return
                
                if event.key == pygame.K_r:
                    try:
                        winsound.PlaySound("Sounds/Lose.wav",winsound.SND_ASYNC)
                    except:
                        Mbox("Error","Unable to load sounds",1)
                        sys.exit()
                    time.sleep(1)
                    LEVELENTITYS.clear()
                    LEVELENTITYSWITHLOGIC.clear()

                    try:
                        LEVELENTITYS,LEVELENTITYSWITHLOGIC = LOADLEVEL(LEVEL,DATA)

                        for ENTITY in LEVELENTITYSWITHLOGIC:
                            ENTITY.GETENTITYS(LEVELENTITYS)
                    except:
                        LEVEL = 1

                        LEVELENTITYS,LEVELENTITYSWITHLOGIC = LOADLEVEL(LEVEL,DATA)

                        for ENTITY in LEVELENTITYSWITHLOGIC:
                            ENTITY.GETENTITYS(LEVELENTITYS)

                    break

                for ENTITY in LEVELENTITYSWITHLOGIC:
                    try:
                        ENTITY.GETINPUT(event.key)
                    except:
                        pass

            if event.type == pygame.QUIT:
                with open("Data.json", "w") as File:
                    json.dump(DATA,File,indent=6)

                return
                
        WINDOW.fill((222,222,222))

        Players = 0
        for Entity in LEVELENTITYS:
            if Entity[2] == "Player":
                Players += 1

        Tiles = 0

        for Entity in LEVELENTITYS:
            if Entity[2] != "TeleportDown" or Entity[2] == "TeleportUp" or Entity[2] == "TeleportRight" or Entity[2] == "TeleportLeft" or Entity[2] != "DoubleTeleportDown" or Entity[2] == "DoubleTeleportUp" or Entity[2] == "DoubleTeleportRight" or Entity[2] == "DoubleTeleportLeft" or Entity[2] == "TripleTeleportDown" or Entity[2] == "TripleTeleportUp" or Entity[2] == "TripleTeleportRight" or Entity[2] == "TripleTeleportLeft":
                Tiles += 1


        if len(LEVELENTITYS) == 400:
            LEVEL += 1 
            DATA["Levels"]["LEVEL" + str(LEVEL - 1)]["BeatenLevel"] = True

        for ENTITY in LEVELENTITYSWITHLOGIC:
            Players = 0
            for Entity in LEVELENTITYS:
                if Entity[2] == "Player":
                    Players += 1

            if ENTITY.RESTARTLEVEL(Players) == True:
                try:

                    if len(LEVELENTITYS) == 400:
                        winsound.PlaySound("Sounds/Win.wav",winsound.SND_ASYNC)
                    else:
                        winsound.PlaySound("Sounds/Lose.wav",winsound.SND_ASYNC)

                except:
                    Mbox("Error","Unable to load sounds",1)
                    sys.exit()

                time.sleep(1)
                LEVELENTITYS.clear()
                LEVELENTITYSWITHLOGIC.clear()

                try:
                    LEVELENTITYS,LEVELENTITYSWITHLOGIC = LOADLEVEL(LEVEL,DATA)

                    for ENTITY in LEVELENTITYSWITHLOGIC:
                        ENTITY.GETENTITYS(LEVELENTITYS)
                except:
                    LEVEL = 1

                    LEVELENTITYS,LEVELENTITYSWITHLOGIC = LOADLEVEL(LEVEL,DATA)

                    for ENTITY in LEVELENTITYSWITHLOGIC:
                        ENTITY.GETENTITYS(LEVELENTITYS)

                break
     

        RUNENTITYLOGIC(LEVELENTITYSWITHLOGIC)

        RenderBackgroundTiles(WINDOW)
        RenderLevel(WINDOW,LEVELENTITYS)

        WINDOW.blit(TransparentSurface,(0,0)) # allows the game to load trasnparent objects

        # GUI LAYER #
        pygame.draw.rect(TransparentSurface, (0,0,0,120),pygame.Rect(0,0,1000,50))

        LEVELSAMOUNT       = len(DATA["Levels"])

        DrawText(WINDOW,32,(200,50),"Fonts/Font1.ttf",f"{str(LEVEL)}/{LEVELSAMOUNT}",(222,222,222))

        if DATA["Levels"]["LEVEL" + str(LEVEL)]["BeatenLevel"] == True:
            DrawText(WINDOW,32,(1625,50),"Fonts/Font1.ttf",f"BEATEN LEVEL",(222,255,222))
            DrawText(WINDOW,32,(800,50),"Fonts/Font1.ttf",f"{str(LEVEL)}",(222,222,222))

            if pygame.mouse.get_pos()[0] > 300 and pygame.mouse.get_pos()[0] < 350 and pygame.mouse.get_pos()[1] > 0 and pygame.mouse.get_pos()[1] < 50 and CLICKING and LEVEL > 1:
                try:
                    winsound.PlaySound("Sounds/Switch.wav",winsound.SND_ASYNC)
                except:
                    Mbox("Error","Unable to load sounds",1)
                    sys.exit()

                time.sleep(0.3)
                LEVELENTITYS.clear()
                LEVELENTITYSWITHLOGIC.clear()

                LEVEL -= 1

                try:
                    LEVELENTITYS,LEVELENTITYSWITHLOGIC = LOADLEVEL(LEVEL,DATA)

                    for ENTITY in LEVELENTITYSWITHLOGIC:
                        ENTITY.GETENTITYS(LEVELENTITYS)
                except:
                    pass

        

            if pygame.mouse.get_pos()[0] > 450 and pygame.mouse.get_pos()[0] < 500 and pygame.mouse.get_pos()[1] > 0 and pygame.mouse.get_pos()[1] < 50 and CLICKING and LEVEL != LEVELSAMOUNT:
                try:
                    winsound.PlaySound("Sounds/Switch.wav",winsound.SND_ASYNC)
                except:
                    Mbox("Error","Unable to load sounds",1)
                    sys.exit()

                time.sleep(0.3)
                LEVELENTITYS.clear()
                LEVELENTITYSWITHLOGIC.clear()

                LEVEL += 1

                try:
                    LEVELENTITYS,LEVELENTITYSWITHLOGIC = LOADLEVEL(LEVEL,DATA)

                    for ENTITY in LEVELENTITYSWITHLOGIC:
                        ENTITY.GETENTITYS(LEVELENTITYS)
                except:
                    pass



            if pygame.mouse.get_pos()[0] > 300 and pygame.mouse.get_pos()[0] < 350 and pygame.mouse.get_pos()[1] > 0 and pygame.mouse.get_pos()[1] < 50 and LEVEL > 1:
                WINDOW.blit(pygame.transform.scale(pygame.transform.rotate(ArrowImage,90),(60,60)),(295,-5))
            elif LEVEL > 1:
                WINDOW.blit(pygame.transform.rotate(ArrowImage,90),(300,0))

            if pygame.mouse.get_pos()[0] > 450 and pygame.mouse.get_pos()[0] < 500 and pygame.mouse.get_pos()[1] > 0 and pygame.mouse.get_pos()[1] < 50 and LEVEL != LEVELSAMOUNT:
                WINDOW.blit(pygame.transform.scale(pygame.transform.rotate(ArrowImage,-90),(60,60)),(445,-5))
            elif LEVEL != LEVELSAMOUNT:
                WINDOW.blit(pygame.transform.rotate(ArrowImage,-90),(450,0))
        else:
            DrawText(WINDOW,32,(1500,50),"Fonts/Font1.ttf",f"LEVEL NOT BEATEN",(255,222,222))
            DrawText(WINDOW,32,(800,50),"Fonts/Font1.ttf",f"{str(LEVEL)}",(222,222,222))

            if pygame.mouse.get_pos()[0] > 300 and pygame.mouse.get_pos()[0] < 350 and pygame.mouse.get_pos()[1] > 0 and pygame.mouse.get_pos()[1] < 50 and CLICKING and LEVEL > 1:
                            try:
                                winsound.PlaySound("Sounds/Switch.wav",winsound.SND_ASYNC)
                            except:
                                Mbox("Error","Unable to load sounds",1)
                                sys.exit()

                            time.sleep(1)
                            LEVELENTITYS.clear()
                            LEVELENTITYSWITHLOGIC.clear()

                            LEVEL -= 1

                            try:
                                LEVELENTITYS,LEVELENTITYSWITHLOGIC = LOADLEVEL(LEVEL,DATA)

                                for ENTITY in LEVELENTITYSWITHLOGIC:
                                    ENTITY.GETENTITYS(LEVELENTITYS)
                            except:
                                pass

            if pygame.mouse.get_pos()[0] > 300 and pygame.mouse.get_pos()[0] < 350 and pygame.mouse.get_pos()[1] > 0 and pygame.mouse.get_pos()[1] < 50 and LEVEL > 1:
                WINDOW.blit(pygame.transform.scale(pygame.transform.rotate(ArrowImage,90),(60,60)),(295,-5))
            elif LEVEL > 1:
                WINDOW.blit(pygame.transform.rotate(ArrowImage,90),(300,0))

        if pygame.mouse.get_pos()[0] > 0 and pygame.mouse.get_pos()[0] < 200 and pygame.mouse.get_pos()[1] > 950 and pygame.mouse.get_pos()[1] < 1000 and CLICKING:
            with open("Data.json", "w") as File:
                json.dump(DATA,File,indent=6)

            return

        if pygame.mouse.get_pos()[0] > 0 and pygame.mouse.get_pos()[0] < 200 and pygame.mouse.get_pos()[1] > 950 and pygame.mouse.get_pos()[1] < 1000:
            WINDOW.blit(pygame.transform.scale(ButtonFrame,(215.5,65.5)),(-15.5,945.5))

            
            DrawText(WINDOW,38,(200,1950),"Fonts/Font1.ttf","Back",(244,244,244)) # Shadow
            DrawText(WINDOW,38,(200,1950),"Fonts/Font1.ttf","Back",(244,244,244))
        else:
            WINDOW.blit(pygame.transform.scale(ButtonFrame,(200,50)),(0,950))

            
            DrawText(WINDOW,32,(200,1950),"Fonts/Font1.ttf","Back",(244,244,244)) # Shadow
            DrawText(WINDOW,32,(200,1950),"Fonts/Font1.ttf","Back",(244,244,244))

        pygame.display.update()

        CLICKING = False