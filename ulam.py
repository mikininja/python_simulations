# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 15:49:53 2017

@author: miki1
"""

import pygame
from pygame.locals import Rect
from math import ceil
from math import sqrt
SIZEX=400
SIZEY=400
def isPrimo(n):
    if n==1 or n==2:
        return True
    for i in range(2,1+int(ceil(sqrt(n)))):
        if n%i==0:
            return False
    return True

class Punto(object):
    def __init__(self,x,y,p):
        self.x=x
        self.y=y
        self.primo=p
class Board(object):
    def __init__(self,sx,sy):
        self.x=sx
        self.y=sy
        pygame.init()
        self.rekt=Rect(0,0,sx,sy)
        self.screen=pygame.display.set_mode(self.rekt.size,0)
        self.bg=pygame.Surface(self.rekt.size)
        self.punti=[]
       
        self.timer=0
        self.curx=int(SIZEX/2)
        self.cury=int(SIZEY/2)
        self.n=0
        self.l=1
        self.curl=0
        self.dir=0
        self.fatto=1
        
    def blit(self):
        self.screen.fill((100,0,100))
        self.n=self.n+1
        
        pr=isPrimo(self.n)
        
        self.punti.append(Punto(self.curx,self.cury,pr))
        for e in self.punti:
            if e.primo==True:
                pygame.draw.circle(self.screen, (255,255,255), (e.x,e.y), 0)
            else:
                pygame.draw.circle(self.screen, (0,0,0), (e.x,e.y), 0)
        
        if self.curl!=0:
            self.curl=self.curl-1
            if self.dir==0:
                self.curx=self.curx+1
            elif self.dir==1:
                if self.fatto==1:
                    self.fatto=0
                else:
                    self.cury=self.cury-1
            elif self.dir==2:
                self.curx=self.curx-1
            elif self.dir==3:
                self.cury=self.cury+1
        else:
            if self.dir==0:
                self.l=self.l+2
                self.curx=self.curx+1
                self.curl=self.l
                self.dir=1
                self.fatto=1
            elif self.dir==1:
                self.curl=self.l
                self.dir=2
            elif self.dir==2:
                self.curl=self.l
                self.dir=3
            elif self.dir==3:
                self.curl=self.l
                self.dir=0
            
                
        
        
      

        pygame.display.update()

    def run(self):
        while 1:
            self.blit()
            #pygame.time.delay(5)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self._running = False
                    pygame.quit()
            

class Splash(object):
    def __init__(self):
        self.x=SIZEX
        self.y=SIZEY

if __name__=="__main__":

    game=Board(SIZEX,SIZEY)
    game.run()
