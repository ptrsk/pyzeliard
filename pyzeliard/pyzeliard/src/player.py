# -*- coding: cp949 -*-
# Copyright (C) Johan Ceuppens 2015
# Copyright (C) Johan Ceuppens 2014
# Copyright (C) Johan Ceuppens 2010 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import pygame
from pygame.locals import *
import random 
import math 
from rng import *
from stateimagelibrary import *

import time #sleep

# ĳ���� �׸���
class Player:
    "Player object"
    
    # xx: 
    # yy:
    def __init__(self, xx,yy):
        self.x = xx 
        self.y = yy
        # default width and height 
        self.w = 56 
        self.h = 56 
        self.SCREENH = 640
        self.SCREENW = 400
        self.LEFT = 0
        self.RIGHT = 1
        self.UP = 2
        self.DOWN = 3
        self.hitpoints = 1200 #hp 1200���� ������ �� 1200?
        self.jumpcounter = 0

        self.rng = RNG(self)

        # ���� ���ִ� �̹���
        self.stimlibleft = Stateimagelibrary()
        image = pygame.image.load('./pics/player-left-1.png').convert()
        image.set_colorkey((0,0,0))
        self.stimlibleft.addpicture(image)

        # ������ ���ִ� �̹���
        self.stimlibright = Stateimagelibrary()
        image = pygame.image.load('./pics/player-right-1.png').convert()
        image.set_colorkey((0,0,0))
        self.stimlibright.addpicture(image)

        # ��Ÿ�� �̹���
        self.stimlibclimbing = Stateimagelibrary() 
        image = pygame.image.load('./pics/player-climb1-30x70.png').convert()
        image.set_colorkey((0,0,0))
        self.stimlibclimbing.addpicture(image)
        image = pygame.image.load('./pics/player-climb1-30x70.png').convert()
        image.set_colorkey((0,0,0))
        self.stimlibclimbing.addpicture(image)
        image = pygame.image.load('./pics/player-climb1-30x70.png').convert()
        image.set_colorkey((0,0,0))
        self.stimlibclimbing.addpicture(image)
        image = pygame.image.load('./pics/player-climb1-30x70.png').convert()
        image.set_colorkey((0,0,0))
        self.stimlibclimbing.addpicture(image)
        image = pygame.image.load('./pics/player-climb2-30x70.png').convert()
        image.set_colorkey((0,0,0))
        self.stimlibclimbing.addpicture(image)
        image = pygame.image.load('./pics/player-climb2-30x70.png').convert()
        image.set_colorkey((0,0,0))
        self.stimlibclimbing.addpicture(image)
        image = pygame.image.load('./pics/player-climb2-30x70.png').convert()
        image.set_colorkey((0,0,0))
        self.stimlibclimbing.addpicture(image)
        image = pygame.image.load('./pics/player-climb2-30x70.png').convert()
        image.set_colorkey((0,0,0))
        self.stimlibclimbing.addpicture(image)

        # ���� ���� ���� �̹���
        self.stimlibleftfight = Stateimagelibrary() 
        image = pygame.image.load('./pics/player-left-fight-1.png').convert()
        image.set_colorkey((0,0,0))
        self.stimlibleftfight.addpicture(image)
        
         # ������ ���� ���� �̹���
        self.stimlibrightfight = Stateimagelibrary()
        image = pygame.image.load('./pics/player-right-fight-1.png').convert()
        image.set_colorkey((0,0,0))
        self.stimlibrightfight.addpicture(image)

        self.direction = self.LEFT 
        # se this to 10 and it draws an attack picture loop
        self.fightcounter = 0
 
    def getrng(self):
        return self.rng
 
    def draw(self, screen, room):
        if self.fightcounter > 0:
            self.fightcounter -= 1
            if self.direction == self.LEFT:
                self.stimlibleftfight.draw(screen, self.x,self.y) 
            elif self.direction == self.RIGHT:
                self.stimlibrightfight.draw(screen, self.x,self.y) 
            return

        if self.direction == self.LEFT:
            self.stimlibleft.draw(screen, self.x,self.y) 
        elif self.direction == self.RIGHT:
            self.stimlibright.draw(screen, self.x,self.y) 

    def drawclimbing(self, screen, room):
        self.stimlibclimbing.draw(screen, self.x,self.y) 


    def notintheair(self):
	if self.jumpcounter == 0:
		return 1
	else:
		return 0

    # ���ΰ� ����
    def jump(self, room):
        self.jumpcounter = 33

    # ���ΰ� ���� ����
    # �������̸� �������̱��� ������Ŵ
    def update(self,room):
        #if self.jumpcounter > 0 and self.jumpcounter < 140:# ������»����̸�
        if self.jumpcounter > 0 and self.jumpcounter < 50:# ������»����̸�
            for r in room.roofs: # ���� �ȵ������. �߸��Ȱžƴ�?
                print "��Ÿ�°� ����!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                if r.collide(room, self):
                    self.jumpcounter = 140 # �̰� ��ƾ�� Ÿ�� 50���� �ٲ����ҵ�
                    ###FIXMEroom.relativey -= 45 
                    room.relativey -= 34 
                    return
            room.relativey += 33 #���ڰ� ũ�� ���̿�����.
            self.jumpcounter += 15
            #time.sleep(1)
        else:
            #�ϰ��Ǵ� ��������
            #print "�ϰ� �Ǵ� ��������"
            self.jumpcounter = 0
            
        print "room.relativey", room.relativey, "self.jumpcounter",self.jumpcounter

    def fight(self,room,player,sword):
        self.sword = sword
        room.fight(self)

    def rollplayersword(self):
        self.sword.roll(self)

 
    def undomove(self):
        1

### NOTE : the coords are transformed with relativex and relativey beforehand
### ���� : ��ǥ�� ������ '���X(relativex)'�� '���Y(relativex)'�� ��ȯ�˴ϴ�.

    def collidewithropep(self, ropeimp):
        if (self.x + self.w/2 > ropeimp.x and
            self.x - self.w/2 < ropeimp.x+ropeimp.w and
            self.y > ropeimp.y and
            self.y < ropeimp.y + ropeimp.h):
            return 1
        return 0
