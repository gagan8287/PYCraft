# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 15:41:12 2019

@author: Gagan Panwar,Firtosh kumar,Damandeep singh 

"""

import pygame
import random
Wwidth = 400
Wheight = 600
SIZE = 400
HEIGHT = 20
WIDTH = 20 
PLAYERX = 0
PLAYERY = 0
XCHAN = 20
YCHAN = 20

INVENTORY = {'grass':10,'wood':10,'brick':0,'water':10,'glass':0,'sand':10,'plank':0,'dirt':99999}
CRAFTING = {'brick':{'water':1,'dirt':2},'plank':{'wood':3},'glass':{'sand':3}}




WORLD = [[]*20]
for i in  range(20):
    WORLD.insert(i,['','','','','','','','','','','','','','','','','','','',''])
  
    
    
pygame.init()
gameDisplay = pygame.display.set_mode((Wwidth,Wheight),pygame.RESIZABLE)
pygame.display.set_caption("PY-Craft")
clock = pygame.time.Clock()    
    
playerimg = pygame.transform.scale(pygame.image.load("E:\MINECRAFT\player.gif"),[WIDTH,HEIGHT])
woodimg = pygame.transform.scale(pygame.image.load('E:\Minecraft\wood.gif'),[WIDTH,HEIGHT])
waterimg = pygame.transform.scale(pygame.image.load('E:\Minecraft\water.gif'),[WIDTH,HEIGHT])
plankimg = pygame.transform.scale(pygame.image.load('E:\Minecraft\plank.gif'),[WIDTH,HEIGHT])
glassimg = pygame.transform.scale(pygame.image.load('E:\Minecraft\glass.gif'),[WIDTH,HEIGHT])
brickimg = pygame.transform.scale(pygame.image.load('E:\Minecraft\grick.gif'),[WIDTH,HEIGHT])
sandimg = pygame.transform.scale(pygame.image.load('E:\Minecraft\sand.gif'),[WIDTH,HEIGHT])
dirtimg = pygame.transform.scale(pygame.image.load('E:\Minecraft\dirt.gif'),[WIDTH,HEIGHT])
grassimg = pygame.transform.scale(pygame.image.load('E:\Minecraft\grass.gif'),[WIDTH,HEIGHT])




def drawplayer(x,y):
    gameDisplay.blit(playerimg,(x,y))
def dirt(x,y):
    gameDisplay.blit(dirtimg,(x,y))
def grass(x,y):
    gameDisplay.blit(grassimg,(x,y))
def wood(x,y):
    gameDisplay.blit(woodimg,(x,y))
def plank(x,y):
    gameDisplay.blit(plankimg,(x,y))
def glass(x,y):
    gameDisplay.blit(glassimg,(x,y))
def sand(x,y):
    gameDisplay.blit(sandimg,(x,y))
def water(x,y):
    gameDisplay.blit(waterimg,(x,y))
def brick(x,y):
    gameDisplay.blit(brickimg,(x,y))
    
    
    
def worldcreate():
    for x in range(0,SIZE,WIDTH):
        for y in range(0,SIZE,HEIGHT):
            i = int(x/20)
            j = int(y/20)
            rand = random.randint(0,12)
            if rand >= 0 and rand <=3 :
                WORLD[i][j] = "dirt"
            elif rand > 3 and rand < 6:
                WORLD[i][j] = "water"
            elif rand >= 6 and rand <= 8:
                WORLD[i][j] = "grass"    
            elif rand >= 9 and rand <= 10:
                WORLD[i][j] = "sand" 
            elif rand >= 11 and rand <= 12:
                WORLD[i][j] = "wood" 

def drawworld():
    for x in range(0,SIZE,WIDTH):
            for y in range(0,SIZE,HEIGHT):
                i = int(x/20)
                j = int(y/20)
                
                TILE = WORLD[i][j]    
                if TILE == 'dirt':
                    dirt(x,y)
                elif TILE == 'grass':
                    grass(x,y)
                elif TILE == 'wood':
                    wood(x,y)
                elif TILE == 'water':
                    water(x,y)
                elif TILE == 'glass':
                    glass(x,y)
                elif TILE == 'plank':
                    plank(x,y)
                elif TILE == 'sand':
                    sand(x,y)
                elif TILE == 'brick':
                    brick(x,y)
                    
def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()

def message_display(text,X,Y):
    largeText = pygame.font.Font('freesansbold.ttf',10)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((X),(Y))
    gameDisplay.blit(TextSurf, TextRect)

    
    

    
    






worldcreate()


run = True
while run:
    gameDisplay.fill((255,255,255)) 
    drawworld()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if PLAYERY+HEIGHT < SIZE:
                    PLAYERY += YCHAN
            if event.key == pygame.K_RIGHT:
                if PLAYERX+HEIGHT < SIZE:
                    PLAYERX += XCHAN
            if event.key == pygame.K_LEFT:
                if PLAYERX > 0:
                    PLAYERX -= XCHAN
            if event.key == pygame.K_UP:
                if PLAYERY > 0:
                    PLAYERY -= YCHAN
            if event.key  == pygame.K_1:
                X = int(PLAYERX/20)
                Y = int(PLAYERY/20)
                if INVENTORY['grass']!=0 and WORLD[X][Y] != 'grass' :
                    TILE = WORLD[X][Y]
                    if(TILE!='dirt'):
                        INVENTORY[TILE] += 1
                    WORLD[X][Y] = 'grass' 
                    INVENTORY['grass'] -= 1
                    
            if event.key  == pygame.K_2:
                X = int(PLAYERX/20)
                Y = int(PLAYERY/20)
                if INVENTORY['wood']!=0 and WORLD[X][Y] != 'wood': 
                    TILE = WORLD[X][Y]
                    if(TILE!='dirt'):
                        INVENTORY[TILE] += 1
                    WORLD[X][Y] = 'wood'
                    INVENTORY['wood'] -= 1
                    
            if event.key  == pygame.K_3:
                X = int(PLAYERX/20)
                Y = int(PLAYERY/20)
                if INVENTORY['water']!=0 and WORLD[X][Y] != 'water':
                    TILE = WORLD[X][Y]
                    if(TILE!='dirt'):
                        INVENTORY[TILE] += 1
                    WORLD[X][Y] = 'water'
                    INVENTORY['water'] -= 1
                    
            if event.key  == pygame.K_4:
                X = int(PLAYERX/20)
                Y = int(PLAYERY/20)
                if INVENTORY['glass']!=0 and WORLD[X][Y] != 'glass':
                    TILE = WORLD[X][Y]
                    if(TILE!='dirt'):
                        INVENTORY[TILE] += 1
                    WORLD[X][Y] = 'glass'
                    INVENTORY['glass'] -= 1
                    
            if event.key  == pygame.K_5:
                X = int(PLAYERX/20)
                Y = int(PLAYERY/20)
                if INVENTORY['plank']!=0 and WORLD[X][Y] != 'plank':
                    TILE = WORLD[X][Y]
                    if(TILE!='dirt'):
                        INVENTORY[TILE] += 1
                    WORLD[X][Y] = 'plank'
                    INVENTORY['plank'] -= 1
                    
            if event.key  == pygame.K_6:
                X = int(PLAYERX/20)
                Y = int(PLAYERY/20)
                if INVENTORY['brick']!=0 and WORLD[X][Y] != 'brick':
                    TILE = WORLD[X][Y]
                    if(TILE!='dirt'):
                        INVENTORY[TILE] += 1
                    WORLD[X][Y] = 'brick'
                    INVENTORY['brick'] -= 1
                    
            if event.key  == pygame.K_7:
                X = int(PLAYERX/20)
                Y = int(PLAYERY/20)
                if INVENTORY['sand']!=0 and WORLD[X][Y] != 'sand':
                    TILE = WORLD[X][Y]
                    if(TILE!='dirt'):
                        INVENTORY[TILE] += 1
                    WORLD[X][Y] = 'sand'
                    INVENTORY['sand'] -= 1
                    
            if event.key == pygame.K_r:
                if INVENTORY['water'] >=CRAFTING['brick']['water'] and INVENTORY['dirt'] >=CRAFTING['brick']['dirt']:
                    INVENTORY['brick'] += 1
                    INVENTORY['water'] -= 1
                    INVENTORY['dirt'] -= 1
                    
            if event.key == pygame.K_u:
                if INVENTORY['wood'] >=CRAFTING['plank']['wood'] :
                    INVENTORY['plank'] += 1
                    INVENTORY['wood'] -= 3
                    
            if event.key == pygame.K_i:
                if INVENTORY['sand'] >=CRAFTING['glass']['sand'] :
                    INVENTORY['glass'] += 1
                    INVENTORY['sand'] -= 3    
                   
                    
            if event.key == pygame.K_SPACE:
                X = int(PLAYERX/20)
                Y = int(PLAYERY/20)
                TILE = WORLD[X][Y]
                WORLD[X][Y] = 'dirt'
                INVENTORY[TILE] = INVENTORY[TILE]+1
                print(INVENTORY[TILE])
                
      

    message_display('GRASS',80,450)
    message_display('WOOD',120,450)
    message_display('WATER',160,450)
    message_display('GLASS',200,450)
    message_display('PLANK',240,450)
    message_display('BRICK',280,450)
    message_display('SAND',320,450)
    
    message_display('CRAFT',20,510)
    message_display('i',200,510)
    message_display('u',240,510)
    message_display('r',280,510)
    
    grass(70,460)
    wood(110,460)
    water(150,460)
    glass(190,460)
    plank(230,460)
    brick(270,460)
    sand(310,460)            
                
                
    message_display('INVENTORY',30,490)            
    message_display(str(INVENTORY['grass']),80,490)
    message_display(str(INVENTORY['wood']),120,490)
    message_display(str(INVENTORY['water']),160,490)
    message_display(str(INVENTORY['glass']),200,490)
    message_display(str(INVENTORY['plank']),240,490)
    message_display(str(INVENTORY['brick']),280,490)
    message_display(str(INVENTORY['sand']),320,490)  


    message_display('Crafting Rule :',200,540)       
    message_display('1 brick -> 1 water + 2 dirt',200,550)      
    message_display('1 plank -> 3 wood',200,560)      
    message_display('1 glass -> 3 sand',200,570)      
    for y in range(0,SIZE, HEIGHT):
        pygame.draw.line(gameDisplay,(0,0,0),(0,y),(SIZE,y))
        pygame.draw.line(gameDisplay,(0,0,0),(y,0),(y,SIZE))
    
    #D.rect(gameDisplay,(255,0,0),(PLAYERX,PLAYERY,HEIGHT,WIDTH))
    drawplayer(PLAYERX,PLAYERY) 
    pygame.display.update()
    clock.tick(120)
    
pygame.quit()
quit()