import pygame
import time
import ctypes
import winsound
import sys

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

class player:
    def __init__(self,DATA,INPUT) -> None:
        self.DATA = DATA
        self.INPUT = INPUT

    def ENTITYINPOSITION(self,X,Y,Moving):
        for Entity in self.Entitys:
            if Moving:
                if Entity[0] == X and Entity[1] == Y and Entity[2] != "TeleportDown" and Entity[2] != "TeleportUp" and Entity[2] != "TeleportRight" and Entity[2] != "TeleportLeft" and Entity[2] != "DoubleTeleportDown" and Entity[2] != "DoubleTeleportUp" and Entity[2] != "DoubleTeleportRight" and Entity[2] != "DoubleTeleportLeft" and Entity[2] != "TripleTeleportDown" and Entity[2] != "TripleTeleportUp" and Entity[2] != "TripleTeleportRight" and Entity[2] != "TripleTeleportLeft":
                    return False
            else:
                if Entity[0] == X and Entity[1] == Y and Entity[2] != "Player" and Entity[2] != "PlayerBody":
                    return False
            
        return True

    def LOGIC(self):
        OLDX = self.DATA[0]
        OLDY = self.DATA[1]

        if self.INPUT == pygame.K_w and self.ENTITYINPOSITION(self.DATA[0],self.DATA[1] - 50,True) == True:
            self.DATA[1] -= 50  

            InsideBody = False
            for Entity in self.Entitys:
                if Entity[0] == OLDX and Entity[1] == OLDY and Entity[2] == "PlayerBody":
                    InsideBody = True

            if InsideBody == False:
                self.Entitys.append((OLDX,OLDY,"PlayerBody"))

            try:
                winsound.PlaySound("Sounds/Jump.wav", winsound.SND_ASYNC)

            except:
                Mbox("Error","Unable to load sounds",1)
                sys.exit()          
            
        if self.INPUT == pygame.K_s and self.ENTITYINPOSITION(self.DATA[0],self.DATA[1] + 50,True) == True:
            self.DATA[1] += 50   

            InsideBody = False
            for Entity in self.Entitys:
                if Entity[0] == OLDX and Entity[1] == OLDY and Entity[2] == "PlayerBody":
                    InsideBody = True

            if InsideBody == False:
                self.Entitys.append((OLDX,OLDY,"PlayerBody"))

            try:
                winsound.PlaySound("Sounds/Jump.wav", winsound.SND_ASYNC)

            except:
                Mbox("Error","Unable to load sounds",1)
                sys.exit()         
            
        if self.INPUT == pygame.K_d and self.ENTITYINPOSITION(self.DATA[0] + 50,self.DATA[1],True) == True:
            self.DATA[0] += 50

            InsideBody = False
            for Entity in self.Entitys:
                if Entity[0] == OLDX and Entity[1] == OLDY and Entity[2] == "PlayerBody":
                    InsideBody = True
                    

            if InsideBody == False:
                self.Entitys.append((OLDX,OLDY,"PlayerBody"))

            try:
                winsound.PlaySound("Sounds/Jump.wav", winsound.SND_ASYNC)

            except:
                Mbox("Error","Unable to load sounds",1)
                sys.exit()

        if self.INPUT == pygame.K_a and self.ENTITYINPOSITION(self.DATA[0] - 50,self.DATA[1],True) == True:
            self.DATA[0] -= 50

            InsideBody = False
            for Entity in self.Entitys:
                if Entity[0] == OLDX and Entity[1] == OLDY and Entity[2] == "PlayerBody":
                    InsideBody = True

            if InsideBody == False:
                self.Entitys.append((OLDX,OLDY,"PlayerBody"))
            try:
                winsound.PlaySound("Sounds/Jump.wav", winsound.SND_ASYNC)
            except:
                Mbox("Error","Unable to load sounds",1)
                sys.exit()

        for Entity in self.Entitys:
            if Entity[0] == self.DATA[0] and Entity[1] == self.DATA[1]:
                if Entity[2] == "TeleportDown":
                    self.DATA[1] += 100
                    try:
                        winsound.PlaySound("Sounds/Jump2.wav", winsound.SND_ASYNC)
                    except:
                        Mbox("Error","Unable to load sounds",1)
                        sys.exit()
                if Entity[2] == "TeleportUp":
                    self.DATA[1] -= 100
                    try:
                        winsound.PlaySound("Sounds/Jump2.wav", winsound.SND_ASYNC)
                    except:
                        Mbox("Error","Unable to load sounds",1)
                        sys.exit()
                if Entity[2] == "TeleportLeft":
                    self.DATA[0] -= 100
                    try:
                        winsound.PlaySound("Sounds/Jump2.wav", winsound.SND_ASYNC)
                    except:
                        Mbox("Error","Unable to load sounds",1)
                        sys.exit()
                if Entity[2] == "TeleportRight":
                    self.DATA[0] += 100
                    try:
                        winsound.PlaySound("Sounds/Jump2.wav", winsound.SND_ASYNC)
                    except:
                        Mbox("Error","Unable to load sounds",1)
                        sys.exit()

                if Entity[2] == "DoubleTeleportDown":
                    self.DATA[1] += 150
                    try:
                        winsound.PlaySound("Sounds/Jump3.wav", winsound.SND_ASYNC)
                    except:
                        Mbox("Error","Unable to load sounds",1)
                        sys.exit()
                if Entity[2] == "DoubleTeleportUp":
                    self.DATA[1] -= 150
                    try:
                        winsound.PlaySound("Sounds/Jump3.wav", winsound.SND_ASYNC)
                    except:
                        Mbox("Error","Unable to load sounds",1)
                        sys.exit()
                if Entity[2] == "DoubleTeleportLeft":
                    self.DATA[0] -= 150
                    try:
                        winsound.PlaySound("Sounds/Jump3.wav", winsound.SND_ASYNC)
                    except:
                        Mbox("Error","Unable to load sounds",1)
                        sys.exit()
                if Entity[2] == "DoubleTeleportRight":
                    self.DATA[0] += 150
                    try:
                        winsound.PlaySound("Sounds/Jump3.wav", winsound.SND_ASYNC)
                    except:
                        Mbox("Error","Unable to load sounds",1)
                        sys.exit()

                if Entity[2] == "TripleTeleportDown":
                    self.DATA[1] += 200
                    try:
                        winsound.PlaySound("Sounds/Jump4.wav", winsound.SND_ASYNC)
                    except:
                        Mbox("Error","Unable to load sounds",1)
                        sys.exit()
                if Entity[2] == "TripleTeleportUp":
                    self.DATA[1] -= 200
                    try:
                        winsound.PlaySound("Sounds/Jump4.wav", winsound.SND_ASYNC)
                    except:
                        Mbox("Error","Unable to load sounds",1)
                        sys.exit()
                if Entity[2] == "TripleTeleportLeft":
                    self.DATA[0] -= 200
                    try:
                        winsound.PlaySound("Sounds/Jump4.wav", winsound.SND_ASYNC)
                    except:
                        Mbox("Error","Unable to load sounds",1)
                        sys.exit()
                if Entity[2] == "TripleTeleportRight":
                    self.DATA[0] += 200
                    try:
                        winsound.PlaySound("Sounds/Jump4.wav", winsound.SND_ASYNC)
                    except:
                        Mbox("Error","Unable to load sounds",1)
                        sys.exit()

        self.INPUT = None

    def RESTARTLEVEL(self,Players):

        if len(self.Entitys) == 400:
            return True
        
        return False

    def GETINPUT(self,Key):
        self.INPUT = Key
    
    def GETENTITYS(self,Entitys):
        self.Entitys = Entitys
