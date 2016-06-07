# -*- coding: utf-8 -*-
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
        self.bgimage = None  # background image
        self.fgimage = None  # foreground image
        self.ground_back_image = None  # foreground image
        self.ground_front_image = None  # foreground image
        self.bank_image = None  # Bank Image
        self.gameobjects = []  # 배열로 처리?
        self.roofs = []
        self.ropes = []
        self.exits = []  # 출구 위치
        
        self.playerdx = 16  # 캐릭터 속도??

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

    def draw(self, screen, player, taskbar):
        """
        draw room's bacground, foreground, land, etc.
        """
        print "Maproombase Draw"
        ### print "relx=%d rely=%d" % (self.relativex, self.relativey)
        x= 0 # 좌측 석상의 폭이 95임 set 96
        y= 26 # 상단 돌의 폭이 25임 set 26
        screen.blit(self.bgimage, (x,y))
        #screen.blit(self.fgimage, (self.relativex, self.relativey+28))
        # 반복해서 찍을것
        ##screen.blit(self.ground_back_image, (self.relativex, self.relativey + 284))
        """
        for i in range (0,10):
            screen.blit(self.ground_back_image, (self.relativex+(self.ground_back_image.get_width() * i+1), self.relativey+ 284))
        #screen.blit(self.ground_front_image, (self.relativex, self.relativey + 299))
        for i in range(0, 10):
            #screen.blit(self.ground_front_image, (self.ground_front_image.get_width() * i+1, self.relativey + 299))
            screen.blit(self.ground_front_image, (self.relativex+(self.ground_front_image.get_width() * i+1), self.relativey + 299))
        """
        for go in self.gameobjects:
            go.draw(screen,self)
        for r in self.ropes:
            r.draw(screen,self)

    def moveleft(self):
        self.relativex += self.playerdx
        #if self.gameobjects
        #print self.relativex,  self.playerdx

    def moveright(self):
        self.relativex -= self.playerdx

    # 객체가 점프하는 속도
    def moveup(self):
        self.relativey += 10
        #self.relativey += 3

    # 객체가 떨어지는 속도
    # NOTE : 이속도는 pyzeliard.py 파일에서 self.player = Player(280,240)에 영향을 줌
    # 그러니 둘다 맞춰야한다. 안맞추면 캐릭터가 땅으로 꺼져버린다.
    def movedown(self):
        self.relativey -= 10
        #self.relativey -= 3

    def fall(self, player):
        #캐릭터 중력상태 유지 평상시에도 유지됨.
        # 반환값 
        # 2 : 바닥에 있을때
        # 0: 언젠지 모르겠음 

        self.movedown() # 상대적 Y축을 -3누적
        #self.relativey -= 3
        #print(self.relativey)

        for i in self.gameobjects:
            if i != None and i.fallcollide(self, player)==True: # 착지상태
                self.moveup() # self.relativey 값을 0으로 유지하기위한듯
                #print "movedown() 2반환"
                # 착지가 똑바로 안되서 아래코드 삽입함
                if self.relativey > -10 :
                    self.relativey = 0
            return 2 # 1 kills game
        
        # 이하는 땅이 없을때임 계속 떨어짐. -저객체를 생략하니 계속 추락함. 
        #self.gameobjects.append(Box(0,300,2000,12)) # xx,yy,ww,hh 으로 저장됨. #땅?
        print"gameobject 가 없을때"
        return 0 

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
