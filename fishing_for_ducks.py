import pgzrun
from random import randint
import pygame, sys, random, time
from pygame import *

count= 1
WIDTH= 800
HEIGHT= 800
fruit= Actor("pixil-frame-0 (47) (1).png")
decoy= Actor("pixil-frame-0 (44) (1).png")
duck= Actor("pixil-frame-0 (47) (1).png")
yellow= Actor("pixil-frame-0 (47) (1).png")
decoy2= Actor("pixil-frame-0 (44) (1).png")
decoy3= Actor("pixil-frame-0 (44) (1).png")
why= Actor("pixil-frame-0 (47) (1).png")
decoy4= Actor("pixil-frame-0 (44) (1).png")
yay= Actor("pixil-frame-0 (47) (1).png")
decoy5= Actor("pixil-frame-0 (44) (1).png")
charecter= Actor("pixil-frame-0 (48) (1).png")
boss = Actor("pixil-frame-0 (58).png")
sprite = Actor("pixil-frame-0 (59).png")
start = Actor("fa4a4d5b-a0cf-490a-a6dd-36c5f8778b9a_200x200.png")

lose = False
bossbeaten = False
right = False
time = False
speedx= 0
speedy= 0
strat = False
draw_game = False

mixer.init()
mixer.music.load("bensound-moose.mp3")
mixer.music.set_volume(0.7)
mixer.music.play()
def draw():
    print(draw_game)
    if draw_game == True:
        screen.clear()
        screen.fill("sky blue")
        screen.draw.text("POINTS= " + str(count),(25,10), color= "chartreuse1", ocolor = "black", owidth = 3)
        screen.draw.text("FISHING FOR DUCKS", (200,10), color= "chartreuse1", fontsize= 50, ocolor = "black", owidth = 3)
        fruit.draw()
        decoy.draw()
        duck.draw()
        yellow.draw()
        decoy2.draw()
        decoy3.draw()
        why.draw()
        decoy4.draw()
        yay.draw()
        decoy5.draw()
        sprite.draw()        
    if lose == True:
        screen.clear()
        screen.fill("sky blue")
        screen.draw.text("GAME OVER", (180, 250), ocolor = "black", owidth = 3, fontsize = 100, color = "tomato")
        mixer.music.pause()
        mixer.music.load("bensound-extremeaction.mp3")
        mixer.music.set_volume(0.7)
        mixer.music.play()
    else:
        screen.clear()
        screen.fill("white")
        start.draw()        
  

def place_fruit(): 
    global speedx
    global speedy    
    fruit.x= randint(100, WIDTH-100)
    fruit.y= randint(100, HEIGHT-50)
    decoy.x= randint(100, WIDTH-100)
    decoy.y= randint(100, HEIGHT-50)
    duck.x= randint(100, WIDTH-100)
    duck.y= randint(100, HEIGHT-50)
    yellow.x= randint(100, WIDTH-100)
    yellow.y= randint(100, HEIGHT-50)    
    decoy2.x= randint(100, WIDTH-100)
    decoy2.y= randint(100, HEIGHT-50)  
    decoy3.x= randint(100, WIDTH- 100)
    decoy3.y= randint(100, HEIGHT-50)
    why.x= randint(100, WIDTH-100)
    why.y= randint(100, HEIGHT-50)    
    decoy4.x= randint(100, WIDTH-100)
    decoy4.y= randint(100, HEIGHT-50)    
    yay.x= randint(100, WIDTH-100)
    yay.y= randint(100, HEIGHT-50)    
    decoy5.x= randint(100, WIDTH-100)
    decoy5.y= randint(100, HEIGHT-50) 
    boss.x = randint(100, WIDTH-100)
    boss.y = randint(100, HEIGHT-100)
    start.x = randint(100, WIDTH-100)
    start.y = randint(100, HEIGHT-80)
    speedx= randint(0, 1)
    speedy= randint(0, 1)
    if speedx == 0:
        speedx = -3
    else:
        speedx = 3

    if speedy == 0:
        speedy = -3
    
    else:
        speedy = 3    

def update():
    global lose
    global speedx
    global speedy
    global count
    global bossbeaten
    fruit.x += speedx
    fruit.y += speedy
    decoy.x += speedx
    decoy.y += speedy
    duck.x += speedx
    duck.y += speedy
    yellow.x += speedx
    yellow.y += speedy
    decoy2.x += speedx
    decoy2.y += speedy
    decoy3.x += speedx
    decoy3.y += speedy
    why.x += speedx 
    why.y += speedy  
    decoy4.x += speedx
    decoy4.y += speedy
    yay.x += speedx
    yay.y += speedy
    decoy5.x += speedx
    decoy5.y += speedy  
    if fruit.x > WIDTH or fruit.x < 225 or fruit.y > HEIGHT or fruit.y < 150:
        place_fruit()
    fruit.y= fruit.y + speedy
    decoy.y= decoy.y + speedy
    duck.y= duck.y + speedy
    yellow.y= yellow.y + speedy
    decoy2.y= decoy2.y + speedy
    decoy3.y= decoy3.y + speedy
    why.y= why.y + speedy
    decoy4.y= decoy4.y + speedy
    yay.y= yay.y + speedy
    decoy5.y= decoy5.y + speedy
    boss.x = boss.x+speedx
    boss.y = boss.y+speedy
    if keyboard.left:
        charecter.x = charecter.x - 100
    elif keyboard.right:
        charecter.x = charecter.x + 100
        right = True
    elif keyboard.up:
        charecter.y = charecter.y - 100
    elif keyboard.down:
        charecter.y = charecter.y + 100
    if charecter.colliderect(fruit):
        count= count+1
    elif charecter.colliderect(decoy):
        count= count-1
    elif charecter.colliderect(duck):
        count= count+1
    elif charecter.colliderect(yellow):
        count= count+1
    elif charecter.colliderect(decoy2):
        count= count-1
    elif charecter.colliderect(decoy3):
        count= count-1
    elif charecter.colliderect(boss):
        bossbeaten = True
    if count == -1:
        lose = True
    if keyboard.left:
        sprite.x = sprite.x - 10
    elif keyboard.right:
        sprite.x = sprite.x + 10
        
    elif keyboard.up:
        sprite.y = sprite.y - 10
    elif keyboard.down:
        sprite.y = sprite.y + 10 
    if sprite.colliderect(fruit):
        count= count+1
    elif sprite.colliderect(decoy):
        count= count-1
    elif sprite.colliderect(duck):
        count= count+1
    elif sprite.colliderect(yellow):
        count= count+1
    elif sprite.colliderect(decoy2):
        count= count-1
    elif sprite.colliderect(decoy3):
        count= count-1
    elif sprite.colliderect(boss):
        bossbeaten = True
    if count == -1:
        lose = True    

def on_mouse_down(pos): 
    if start.collidepoint(pos):
        draw_game = True

    

pgzrun.go()

pygame.quit()

