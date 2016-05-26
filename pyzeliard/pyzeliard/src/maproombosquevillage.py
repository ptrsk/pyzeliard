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

#보스크 마을에대한 정의를 함
#배경, 상점위치, 등.. 
#Todo: NPC 처리, 대화, 이벤트처리
class MaproomBosqueVillage(Maproomvillage):
    "Dungeon"

    # 보스크 마을내에 어디쯤에 뭐가 있는지를 기술했음.
    # xx : x값
    # yy : y값
    # ww : 폭
    # hh : 높이
    def __init__(self, xx,yy,ww,hh):
        
        Maproomvillage.__init__(self,xx,yy,ww,hh) # 마을설정
        self.fgimage = pygame.image.load('./images/bg-bosquevillage.png') # 마을 배경 넣기
        
        self.bgimage = pygame.image.load('./images/bg-mountain.png') # 산 이미지
        
        #self.locationtext = "보스크Bosque".encode('cp949') # 마을이름  문제점: 한글출력은 안된다.
        self.locationtext = "보스크" # 마을이름  문제점: 한글출력은 안된다.
        self.roomnumber = 1
        self.gameobjects.append(Box(0,300,2000,12)) # xx,yy,ww,hh 으로 저장됨.
        
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
