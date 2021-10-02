# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 20:57:29 2021

@author: Lenovo
"""

import pygame
pygame.init()
#hello
win = pygame.display.set_mode((852,480))

pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')
bulletsound = pygame.mixer.Sound('bullet.wav')
hitsound = pygame.mixer.Sound('hit.wav')
music = pygame.mixer.music.load("music.mp3")

pygame.mixer.music.play(-1)

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isjump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpcount = 10
        self.standing = True
        self.hitbox = (self.x + 17, self.y, 29, 652)

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkLeft[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2)
        
    def hit(self):
        self.x = 60
        self.y = 410
        self.walkCount = 0
        self.isjump = False
        self.jumpcount = 10
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('-5', 1, (255, 0, 0))
        win.blit(text, (250 - (text.get_width()/2),200))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing
        
    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
      
class enemy:
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]
    
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width 
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True
        
    def draw(self, win):
        if self.visible:
            self.move()
            if self.walkCount + 1 >= 33:
                self.walkCount = 0
            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            pygame.draw.rect(win, (255,0,0), (self.hitbox[0],self.hitbox[1] - 20, 50, 5))
            pygame.draw.rect(win, (0,144,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 5))
            #pygame.draw.rect(win, (255,0,0), (self.hitbox,2)
            #pygame.draw.rect(win, (255,0,0), self.hitbox,2)
        else:
            text = font.render("Nee Jayichuuu!!", 1, (179, 25, 255))
            win.blit(text, (400, 240))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print('hit')
                
                            
clock = pygame.time.Clock()

def reDrawGameWindow():
    win.blit(bg, (0,0))
    goblin.draw(win)
    text = font.render("Score:" + str(score), 1, (0, 0, 0))
    win.blit(text, (720, 10))
    #goblin2.draw(win)
    man.draw(win)
    #man2.draw(win)
    
    for bullet in bullets:
        bullet.draw(win) 
    pygame.display.update()


man = player(200, 410, 64,64)
#man2 = player(100, 410, 64,64)
goblin = enemy(100, 410, 64, 64, 300)
#goblin2 = enemy(200, 410, 64, 64, 450)
score = 0
font = pygame.font.SysFont('Comic Sans', 30, True)
bullets = []
shootLoop = 0
#main
run = True
while run:
    #pygame.time.delay(50)
    clock.tick(27)
    if goblin.visible:
        if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                man.hit()
                score -= 5
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 5:
        shootLoop = 0
    
    for  event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False
            
    for bullet in bullets:
        if goblin.visible:
            if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]: # Checks x coords
                if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                    # Checks y coords
                    hitsound.play()
                    goblin.hit()
                    score += 100
                    bullets.pop(bullets.index(bullet)) 

        if bullet.x < 852  and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and shootLoop == 0:
        bulletsound.play()
        if man.left:
            facing = -1
        else:
            facing = 1
        
        if len(bullets) < 5:
            bullets.append(projectile(round(man.x+man.width//2),round(man.y+man.height//2), 6, (0,0,0), facing))
        shootLoop = 1
    
    if keys[pygame.K_LEFT] and man.x > 5:
        man.x -= man.vel
        man.left = True 
        man.right = False
        man.standing = False
        
    elif keys[pygame.K_RIGHT] and man.x < 852 - man.width - man.vel:
        man.x+=man.vel
        man.left = False
        man.right = True
        man.standing = False
        
    else:
        man.standing = True
        man.walkCount = 0
        
    if not(man.isjump): 
        if keys[pygame.K_UP]:
            man.isjump = True
            man.left = False
            man.right = False
            man.walkCount = 0
    else:
        if man.jumpcount >= -10:
            man.y -= (man.jumpcount * abs(man.jumpcount)) * 0.25
            man.jumpcount -= 1
        else:
            man.jumpcount = 10
            man.isjump = False
            
    reDrawGameWindow()
          
pygame.quit()
