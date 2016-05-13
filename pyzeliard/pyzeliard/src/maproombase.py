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
from gameobject import *

class Maproombase:
    "Base"
    def __init__(self, xx,yy,ww,hh):
        self.relativex = xx
        self.relativey = yy
        self.w = ww
        self.h = hh
        self.bgimage = None #��� �̹���
        self.gameobjects = [] #�迭�� ó��?
        self.roofs = []
        self.ropes = []
        self.exits = [] # �ⱸ ��ġ
        
        self.playerdx = 6

    def collideundomove(self,room,player):
		flag = 0
        	for i in self.gameobjects:
	    		if i:
	    			obj = i.collideundomove(room,player)
				if obj:
					for j in self.gameobjects:
						if j:
							k = j.collideundomove(room,player)
							if k != obj:
								flag += 1
					if flag == 0:
						return 1	
        	return 0

    def draw(self, screen, player,taskbar):
		### print "relx=%d rely=%d" % (self.relativex, self.relativey)
		screen.blit(self.bgimage, (self.relativex, self.relativey+25))
		for go in self.gameobjects:
			go.draw(screen,self)
		for r in self.ropes:
			r.draw(screen,self)

    def moveleft(self):
		self.relativex += self.playerdx 

    def moveright(self):
		self.relativex -= self.playerdx

    # ��ü�� �����ϴ� �ӵ�
    def moveup(self):
        self.relativey += 10
        #self.relativey += 3

    # ��ü�� �������� �ӵ�
    # NOTE : �̼ӵ��� pyzeliard.py ���Ͽ��� self.player = Player(280,240)�� ������ ��
    # �׷��� �Ѵ� ������Ѵ�. �ȸ��߸� ĳ���Ͱ� ������ ����������.
    def movedown(self):
        self.relativey -= 10
        #self.relativey -= 3

    #ĳ���� �߷»��� ���� ���ÿ��� ������.
    # ��ȯ�� 
    # 2 : �ٴڿ� ������
    # 0: ������ �𸣰��� 
    def fall(self, player):
        self.movedown() # ����� Y���� -3����
        #self.relativey -= 3
        #print(self.relativey)

        for i in self.gameobjects:
            if i != None and i.fallcollide(self, player)==True: # ��������
                self.moveup() # self.relativey ���� 0���� �����ϱ����ѵ�
                #print"2��ȯ" 
            return 2 # 1 kills game
    
        print"gameobject �� ������ "
        return 0 # �̰� Ż���� �ִ°ǰ�?

    def collide(self, player):
        for go in self.gameobjects:
            go.collide(self,player)

    def collideropes(self, player):
		for r in self.ropes:
			if r.collide(self,player):
				return 1
		return 0

    def update(self, player):
		1

    def exit(self, game):
		return 0	
