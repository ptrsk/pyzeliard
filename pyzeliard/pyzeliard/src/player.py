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

# 캐릭터 그리기
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
        self.direction = self.RIGHT #오른쪽방향보고있을것 
        self.pre_direction = self.LEFT #소소한건데 방향을 바꾸면 항상 시작하는 이미지번호가 일정함 그것을 맞춰주기위함임.

        self.hitpoints = 1200 #hp 1200으로 설정함 왜 1200?
        self.jumpcounter = 0

        self.rng = RNG(self)

        # enum 처럼 사용함.
        self.STATE_STANDING = 0
        self.STATE_WALKING = 1
        self.STATE_RUNNING = 2
        self.STATE_SITTING = 3
        self.STATE_JUMPING = 4
        self.STATE_ATACKING = 5
        self.STATE_DIE = 9
        
        self.walk_rate = 0.01 # 걷기 이미지 속도
         
        #initialize
        self.state = self.STATE_STANDING
        
        
        self.PLACE_TOWN = 1
        self.PLACE_DUNGEON = 2
        self.player_place = self.PLACE_TOWN
        
        # se this to 10 and it draws an attack picture loop
        self.fightcounter = 0
        
        #=======================================================================
        # player image loading
        #=======================================================================

        ##################
        # Action Image Loading
        # 애니메이션을 사용하기위해서 통합함. pyganim라이브러리 사용
        # creating the PygAnimation objects for walking/running in all directions
        animTypes = 'walk_left run_left run_right'.split() #현재 존재하는 그림만 추가할것
        #animTypes = 'walk_right walk_left run_right run_left jump_left jump_right fight_left fight_right'.split()
        self.animObjs = {}
        for animType in animTypes:
            imagesAndDurations = [('./images/duke_%s_%s.png' % (animType, str(num).rjust(1, '0')), 0.09) for num in range(4)]
            self.animObjs[animType] = pyganim.PygAnimation(imagesAndDurations)  # 이미지 불러오기
        
        self.animObjs['walk_right'] = self.animObjs['walk_left'].getCopy()  # 이미지 복사
        self.animObjs['walk_right'].flip(True, False)
        self.animObjs['walk_right'].makeTransformsPermanent()

        ##################
        # 벽타는 이미지
        self.stimlibclimbing = Stateimagelibrary() 
        image = pygame.image.load('./pics/player-climb1-30x70.png').convert()
        image.set_colorkey((0,0,0))# 투명화할색을 설정함.
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

        # 왼쪽 보고 전투 이미지
        self.stimlibleftfight = Stateimagelibrary() 
        image = pygame.image.load('./pics/player-left-fight-1.png').convert()
        image.set_colorkey((0,0,0))
        self.stimlibleftfight.addpicture(image)
        
         # 오른쪽 보고 전투 이미지
        self.stimlibrightfight = Stateimagelibrary()
        image = pygame.image.load('./pics/player-right-fight-1.png').convert()
        image.set_colorkey((0,0,0))
        self.stimlibrightfight.addpicture(image)

        self.moveConductor = pyganim.PygConductor(self.animObjs) # 정지 재생 여부 이미지 로딩이완료된시점에서 할것 안그러면 그이하의 그림들은 짤림

        
 
    def getrng(self):
        return self.rng
 
    def draw(self, screen, room):

        """
        싸움하려는 키가 눌러졌을때 (fightcounter)
        싸움장면 그림
        고쳐야함.
        """
        if self.fightcounter > 0:
            self.fightcounter -= 1
            if self.direction == self.LEFT:
                self.stimlibleftfight.draw(screen, self.x,self.y) 
            elif self.direction == self.RIGHT:
                self.stimlibrightfight.draw(screen, self.x,self.y) 
            return

        if self.state == self.STATE_STANDING :
            """
            Standing
            """
            self.moveConductor.pause()
            if self.direction == self.LEFT:
                if self.pre_direction == self.RIGHT:
                    #거의 의미 없는 부분임 그렇지만 원본과 일치시키기 위함임
                    self.animObjs['walk_left'].setCurrentFrame(0)
                self.animObjs['walk_left'].blit(screen, (self.x, self.y))
                ##self.stimlibleft.drawstatic(screen, self.x,self.y)
                self.pre_direction = self.LEFT
            elif self.direction == self.RIGHT:
                if self.pre_direction == self.LEFT:
                    #거의 의미 없는 부분임 그렇지만 원본과 일치시키기 위함임
                    self.animObjs['walk_left'].setCurrentFrame(2)
                self.animObjs['walk_right'].blit(screen, (self.x, self.y))
                #self.stimlibright.drawstatic(screen, self.x,self.y)

        elif self.state == self.STATE_WALKING :
            """
            Walking
            """

            self.moveConductor.play()            
            if self.direction == self.LEFT:
                #self.stimlibleft.draw(screen, self.x,self.y, self.walk_rate)
                self.animObjs['walk_left'].blit(screen, (self.x, self.y))
            elif self.direction == self.RIGHT:
                #self.stimlibright.draw(screen, self.x,self.y, self.walk_rate) 
                self.animObjs['walk_right'].blit(screen, (self.x, self.y))
                

        elif self.state == self.STATE_RUNNING :
            """
            Running
            """
            self.moveConductor.play()
            if self.direction == self.LEFT:                
                #self.stimlibleft.draw(screen, self.x,self.y, self.walk_rate)
                self.animObjs['run_left'].blit(screen, (self.x, self.y))
            elif self.direction == self.RIGHT:
                self.animObjs['run_right'].blit(screen, (self.x, self.y))
                #self.stimlibright.draw(screen, self.x,self.y, self.walk_rate) 
        
        elif self.state == self.STATE_ATTACKING :
            """
            Attacking
            """
            print "공격"
            
    def drawclimbing(self, screen, room):
        self.stimlibclimbing.draw(screen, self.x,self.y) 


    def notintheair(self):
	if self.jumpcounter == 0:
		return 1
	else:
		return 0

    # 주인공 점프
    def jump(self, room):
        self.jumpcounter = 33

    # 주인공 상태 갱신
    # 점프중이면 일정높이까지 점프시킴
    def update(self,room):
        #if self.jumpcounter > 0 and self.jumpcounter < 140:# 점프상승상태이면
        if self.jumpcounter > 0 and self.jumpcounter < 50:# 점프상승상태이면
            for r in room.roofs: # 값이 안들어있음. 잘못된거아님?
                print "안타는게 들어옴!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                if r.collide(room, self):
                    self.jumpcounter = 140 # 이곳 루틴을 타면 50으로 바뀌어야할듯
                    ###FIXMEroom.relativey -= 45 
                    room.relativey -= 34 
                    return
            room.relativey += 33 #숫자가 크면 높이오른다.
            self.jumpcounter += 15
            #time.sleep(1)
        else:
            #하강또는 착지상태
            #print "하강 또는 착지상태"
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
### 참고 : 좌표는 사전에 '상대X(relativex)'와 '상대Y(relativex)'로 변환됩니다.

    def collidewithropep(self, ropeimp):
        if (self.x + self.w/2 > ropeimp.x and
            self.x - self.w/2 < ropeimp.x+ropeimp.w and
            self.y > ropeimp.y and
            self.y < ropeimp.y + ropeimp.h):
            return 1
        return 0
