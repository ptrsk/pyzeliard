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
from maproomvillage import *
from box import *
from exit import *
from ropez import *
from ropeellips import *
from ropesinus import *

#����ũ ���������� ���Ǹ� ��
class MaproomBosqueVillage(Maproomvillage):
    "Dungeon"

    # ������ �����
    # xx : x��
    # yy : y��
    # ww : ��
    # hh : ����
    def __init__(self, xx,yy,ww,hh):
        Maproomvillage.__init__(self,xx,yy,ww,hh)
        self.bgimage = pygame.image.load('./pics/bg-bosquevillage-1.png') # ���� ��� �ֱ�
        #self.locationtext = "����ũBosque".encode('cp949') # �����̸�  ������: �ѱ������ �ȵȴ�.
        self.locationtext = "����ũ" # �����̸�  ������: �ѱ������ �ȵȴ�.
        self.roomnumber = 1
        self.gameobjects.append(Box(0,300,2000,12)) # xx,yy,ww,hh ���� �����.
        
        ###self.ropes.append(Ropez(900,150,100))
        ###self.ropes.append(RopeSinus(700,100,800,100,0.1,0.01,100))
        
        ## To Cavern of Malicia	
        self.exits.append(Exit(1890,180,100,100,0,0,2,"Cavern of Malicia"))
        ## To Weapon and Armour Shop
        self.exits.append(Exit(865,180,45,100,0,0,2,"Weapon and Armour shop")) #xx, yy, ww, hh, xoffset, ypffset, roomnumber, locationtext

    def exit(self, game):
        for e in self.exits:
            if e.exitp(game):
                game.x = e.xoffset
                game.y = e.yoffset
                game.locationtext = e.locationtext
                return e.locationtext
        return "" 
