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
import pyganim

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

        # enum ó�� �����.
        self.STATE_STAND = 0
        self.STATE_WALK = 1
        self.STATE_RUN = 2
        self.STATE_SIT = 3
        self.STATE_JUMP = 4
        self.STATE_DIE = 5
        
        self.walk_rate = 0.05 # �ȱ� ó�� �ӵ�
        #initialize
        self.state = self.STATE_STAND
        
        #=======================================================================
        # player image loading
        #=======================================================================
        # ���� ���ִ� �̹���
        self.stimlibleft = Stateimagelibrary()
        #image = pygame.image.load('./pics/player-left-1.png').convert() #old
        image = pygame.image.load('./images/duke_walk_left_0.png').convert()
        image.set_colorkey((0,0,0))
        self.stimlibleft.addpicture(image)

        image = pygame.image.load('./images/duke_walk_left_1.png').convert()
        image.set_colorkey((0,0,0))
        self.stimlibleft.addpicture(image)

        image = pygame.image.load('./images/duke_walk_left_2.png').convert()
        image.set_colorkey((0,0,0))
        self.stimlibleft.addpicture(image)

        image = pygame.image.load('./images/duke_walk_left_3.png').convert()
        image.set_colorkey((0,0,0))
        self.stimlibleft.addpicture(image)


        # ������ ���ִ� �̹���
        self.stimlibright = Stateimagelibrary()
        #image = pygame.image.load('./pics/player-right-1.png').convert() #old
        image = pygame.image.load('./images/duke_walk_right_0.png').convert() # path ./ or not -> same
        image.set_colorkey((0,0,0))
        self.stimlibright.addpicture(image)

        image = pygame.image.load('./images/duke_walk_right_1.png').convert()
        image.set_colorkey((0,0,0))
        self.stimlibright.addpicture(image)

        image = pygame.image.load('./images/duke_walk_right_2.png').convert()
        image.set_colorkey((0,0,0))
        self.stimlibright.addpicture(image)
        
        image = pygame.image.load('./images/duke_walk_right_3.png').convert()
        image.set_colorkey((0,0,0))
        self.stimlibright.addpicture(image)

        ##################
        # image loading
        # �ִϸ��̼��� ����ϱ����ؼ� ������. pyganim���̺귯�� ���
        # creating the PygAnimation objects for walking/running in all directions
        animTypes = 'walk_left walk_right'.split()
        #animTypes = 'walk_right walk_left run_right run_left jump_left jump_right fight_left fight_right'.split()
        self.animObjs = {}
        for animType in animTypes:
            imagesAndDurations = [('./images/duke_%s_%s.png' % (animType, str(num).rjust(1, '0')), 0.1) for num in range(4)]
            self.animObjs[animType] = pyganim.PygAnimation(imagesAndDurations)
        
        self.moveConductor = pyganim.PygConductor(self.animObjs) # ���� ��� ����
        ##################
        
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

        self.direction = self.RIGHT 
        # se this to 10 and it draws an attack picture loop
        self.fightcounter = 0
 
    def getrng(self):
        return self.rng
 
    def draw(self, screen, room):

        """
        �ο��Ϸ��� Ű�� ���������� (fightcounter)
        �ο���� �׸�
        """
        if self.fightcounter > 0:
            self.fightcounter -= 1
            if self.direction == self.LEFT:
                self.stimlibleftfight.draw(screen, self.x,self.y) 
            elif self.direction == self.RIGHT:
                self.stimlibrightfight.draw(screen, self.x,self.y) 
            return

        """
        Standing
        """
        if self.state == self.STATE_STAND :
            if self.direction == self.LEFT:
                self.moveConductor.stop()
                self.stimlibleft.drawstatic(screen, self.x,self.y)
            elif self.direction == self.RIGHT:
                self.stimlibright.drawstatic(screen, self.x,self.y) 

        """
        Walking
        """
        if self.state == self.STATE_WALK :
            if self.direction == self.LEFT:
                self.moveConductor.play()
                self.stimlibleft.draw(screen, self.x,self.y, self.walk_rate)
            elif self.direction == self.RIGHT:
                self.stimlibright.draw(screen, self.x,self.y, self.walk_rate) 

        """
        Running
        """
        if self.state == self.STATE_RUN :
            if self.direction == self.LEFT:
                self.moveConductor.play()
                self.stimlibleft.draw(screen, self.x,self.y, self.walk_rate)
                #self.animObjs['walk_left'].draw(screen, (self.x,self.y-4)) #error
                #self.animObjs['walk_left'].blit(screen, (self.x, self.y)) # �߸���
            elif self.direction == self.RIGHT:
                self.stimlibright.draw(screen, self.x,self.y, self.walk_rate) 
            
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
            
        #print "room.relativey", room.relativey, "self.jumpcounter",self.jumpcounter

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
