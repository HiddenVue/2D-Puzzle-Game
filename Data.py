import pygame
import os
import json

def LOAD():
    with open("Data.json","r") as File:
        return json.load(File)

    return False
