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
from maproomvillage import *
from box import *
from exit import *
from ropez import *
from ropeellips import *
from ropesinus import *
from building_satonobank import *

#보스크 마을에대한 정의를 함
#배경, 상점위치, 등.. 
# TODO: NPC 처리, 대화, 이벤트처리
class MaproomBosqueVillage(Maproomvillage):
    "Dungeon"

    def __init__(self, xx,yy,ww,hh):
        # 보스크 마을내에 어디쯤에 뭐가 있는지를 기술했음.
        # xx : x값
        # yy : y값
        # ww : 폭 - 이미지를 연산하여 구할수있어서 삭제함
        # hh : 높이 - 이미지를 연산하여 구할수있어서 삭제함
        # TODO: 나중엔 fgimage 없앨것
        Maproomvillage.__init__(self,xx,yy,ww,hh) # 마을설정 --- 제일먼저 써야함 나중에쓰면 오류남
        #self.fgimage = pygame.image.load('./images/bg-bosquevillage.png') # 마을 배경 넣기 - 사용안함.  이것대신 일일히 만들어 넣을것임
        self.bgimage = pygame.image.load('./images/bg-mountain.png') # 산 이미지
        self.ground_back_image = pygame.image.load('./images/bg-ground_back.png')
        self.ground_front_image = pygame.image.load('./images/bg-ground_front.png')
        #self.bank_image = pygame.image.load('./images/satono_bank.png')
        #ww, hh = self.fgimage.get_rect().size # 사용안함. - 일일히 넣을것임


        self.locationtext = u"보스크" # 마을이름  문제점: 한글출력은 안된다.
        self.roomnumber = 1

        # xx,yy,ww,hh 으로 저장됨. #땅? 그러나 이미지가 없으면 떨어지는듯.
        # 16은 땅두께




        # TODO : 마을내에 건물들 사람들을 배치
        # TODO : BUILDING
        #        X만 놓으면됨
        #        종류 : 출입이 가능여부
        #        트리거 : 위로가는 화살표 건물에서만 작동
        #        대상 : 나무, 벽, 건물, 동굴 입구
        # TODO : NPC
        #        X만 놓으면 됨 자동으로 움직임.
        #        할말도 모두 여기또는 이하의 클래스에서 정함
        #        트리거 : 스페이스(또는 말걸기)
        # 바닥은 고정되게 할것
        self.gameobjects.append(Box(0, 300, ww, 16))  # land



        self.gameobjects.append(Building_SatonoBank(600, 156))  # bank # 바닥에서 높이 빼기

        # TODO: 어느정도 위치에 뭐가 있다 정도로 설계할수있게 할것.
        # self.bgimage = pygame.image.load('./images/satono_bank.png') # 모양
        #self.building= Building_SatonoBank(0,32).draw()
        #self.gameobjects.append(Building_SatonoBank(0,32))

        ###self.ropes.append(Ropez(900,150,100))
        ###self.ropes.append(RopeSinus(700,100,800,100,0.1,0.01,100))
        
        ## To Cavern of Malicia	
        self.exits.append(Exit(1890,180,100,100,0,0,2,"Cavern of Malicia"))
        ## To Weapon and Armour Shop
        self.exits.append(Exit(865,180,45,100,0,0,2,"Weapon and Armour shop")) #xx, yy, ww, hh, xoffset, ypffset, roomnumber, locationtext

        self.exits.append(Exit(600, 156, 45, 100, 0, 0, 2, "The Bank"))

    def exit(self, game):
        #출구 처리
        # self : Exit Class
        # game : Main Class

        for e in self.exits:
            #print "목록:" + e.locationtext
            if e.exitp(game):
                game.x = e.xoffset
                game.y = e.yoffset
                game.locationtext = e.locationtext
                return e.locationtext
        return "" 
