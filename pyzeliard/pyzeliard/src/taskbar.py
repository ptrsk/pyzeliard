# -*- coding: cp949 -*-
# Copyright (C) Johan Ceuppens 2015 
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
from shortsword import *

#�ϴ��� ����ǥ����
class Taskbar:
    "Taskbar"
    
    # ����â
    # screen :
    # font : ��Ʈ
    # player :
    def __init__(self, screen, font, player):
        self.screen = screen	
        self.font = font
        self.player = player
        
        #Į �̹���
        self.swordimage = pygame.image.load('./pics/sword1-40x38.png').convert() # Į���
        self.swordimage.set_colorkey((255,0,255)) #�����?
        self.sword = ShortSword(384,341,40,38)

        self.image = pygame.image.load('./pics/taskbar.png').convert() # ����â
        self.image.set_colorkey((255,0,0)) # ������

        self.goldnumber = 0 # ���ʱ�ȭ
        self.almasnumber = 0 # �˸��� �ʱ�ȭ

    def draw(self,game):
        game.screen.blit(self.image, (70, 310))
        game.screen.blit(self.sword.image, (self.sword.x, self.sword.y))
        game.screen.blit(self.font.render(game.room.locationtext, 6, (255,255,255)), (200,348))
        game.screen.blit(self.font.render(str(self.goldnumber), 6, (255,255,255)), (190,372))
        game.screen.blit(self.font.render(str(self.almasnumber), 6, (255,255,255)), (310,372))

    def drawlocationtext(self,text):
        self.screen.blit(self.font.render(text, 6, (255,255,255)), (200,345))


    def setswordimage(self, imagefilename,r,g,b):
        self.swordimage = pygame.image.load(imagefilename).convert()
        self.swordimage.set_colorkey((r,g,b))
