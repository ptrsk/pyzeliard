# -*- coding: utf-8 -*-
# Copyright (C) Johan Ceuppens 2015
# Copyright (C) Johan Ceuppens 2011
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

import os
import sys

import pygame
from pygame.locals import *
import pyganim

import random
from time import *

from color import *
from bgoverlay import *
from characterscreen import *
from meter import *
from taskbar import *
from player import *
from maproombosquevillage import *
from maproomweaponstorebosque import *
from maproomfortunetellerbosque import *
from maproombankbosque import *
from maproomcavernofmalicia import *


class Game:
    "Main function"

    def __init__(self):

        """
        initialize program
        """

        pygame.init()
        pygame.font.init()

        # set up the window
        self.screen = pygame.display.set_mode((640, 400))  # 윈도우 크기 설정
        # self.screen = pygame.display.set_mode((640, 400), 0, 32) #윈도우 크기 설정
        # self.screen = pygame.display.set_mode((800, 600)) #윈도우 크기 설정
        # 1) 화면 해상도를 480*320으로 초기화. 윈도우 모드, 더블 버퍼 모드로 초기화하는 경우
        # self.screen = pygame.display.set_mode((480, 320), DOUBLEBUF)

        # 2) 화면 해상도를 480*320, 전체 화면 모드, 하드웨어 가속 사용, 더블 버퍼 모드로 초기화하는 경우
        # self.screen = pygame.display.set_mode((480, 320), FULLSCREEN | HWSURFACE | DOUBLEBUF)

        pygame.display.set_caption("젤리아드")  # window title

        # self.font = pygame.font.SysFont("Times", 14) # 타임 폰트
        # self.font = pygame.font.SysFont('./fonts/NanumGothic.ttf', 14) # 타임 폰트
        self.font = pygame.font.Font('./fonts/NanumBrush.ttf', 13)  # 타임 폰트
        # self.font2 = pygame.font.SysFont("Coutier", 28) #코우티어, System 폰트, 한글이 안된다.
        self.font2 = pygame.font.SysFont("Gulim2", 27)
        self.font2 = pygame.font.Font('./fonts/NanumBrush.ttf', 27)  # 타임 폰트

        self.font3 = pygame.font.SysFont("Vera", 52)  # 베라 폰트

        blankimage = pygame.image.load('./pics/blank.png').convert()  # 검은화면
        titleimage = pygame.image.load('./pics/titlescreen.png').convert()  # 로고 화면
        gameover = False  # 게임종료여부 -- 0:게임 안끊남. 1: 끝남

        """
        run logo
        로고화면띄우기
        """
        # print("로고화면")
        while gameover == False:
            pygame.display.update()  # 화면갱신
            self.screen.blit(titleimage, (0, 0))  # 로고화면 출력
            sleep(0.01)
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == KEYDOWN:
                    gameover = True  # 다음넘어가기
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    gameover = True  # 다음넘어가기

        """
        initialize game
        게임 진행 초기화 
        """

        # print("게임진행화면")
        self.meter = Meter()  # 생명줄 생성
        pygame.key.set_repeat(10, 100)  # ??? (지연, 간격)
        ####pygame.key.set_repeat(1000,1000)

        ## offsets for room changing
        self.x = 0  # 방위치?
        self.y = 0

        # self.player = Player(280,252)# 플레이어 위치 (X축, Y축) --화면 중앙에서 얼마나 치우쳐졌는지 확인 화면중앙에서 멀어짐
        self.player = Player(280, 236)  # 플레이어 위치 (X축, Y축) --화면 중앙에서 얼마나 치우쳐졌는지 확인 화면중앙에서 멀어짐
        # self.player = Player(280,199) #-- 이건 원래것

        # 마을 로딩
        self.room = MaproomBosqueVillage(-700, 0, 3312, 288)  # 현재는 보스크마을 등록 x축, y축, 가로크기, 세로크기
        #  self.room = MaproomBosqueVillage(-700, 0)  # 현재는 보스크마을 등록 x축, y축, 가로크기, 세로크기
        # self.room = MaproomBosqueVillage(-700,0,2000,400) #현재는 보스크마을 등록
        ###self.room = MaproomCavernofMalicia(0,0,2000,400)
        ###self.room = MaproomweaponstoreBosque()
        ###self.room = MaproomfortunetellerBosque()
        #self.room = MaproombankBosque()


        self.locationtext = self.room.locationtext  # 방이름 입력
        self.roomnumber = self.room.roomnumber  # 방번호 입력

        self.bgoverlay = BGOverlay(0, 0)  # 전면배경 경계면 (0,0)<-- no use
        self.taskbar = Taskbar(self.screen, self.font2, self.player)  # 작업표시줄 보이기. screen, font, player
        self.characterscreen = CharacterScreen(self.font)  # 인벤토리창

        # gameflag = 0 # 안쓰임. 아무래도 gameover의 오타인듯.

        # print("프로그램 종료")
        # os.system("pause")
        # sys.exit()

        ######################
        # 키보드입력
        ######################
        player_run = False
        gameover = False  # 게임종료여부 -- 0: 진행중 1: 종료

        while gameover == False:
            self.player.h = 72  # NOTE: for ducking, FIXME 48
            sleep(0.01)

            for event in pygame.event.get():
                if event.type == QUIT:  # X버튼
                    print("x:종료")
                    return
                elif event.type == KEYDOWN:
                    self.keydown = 1
                    # self.player 1 key controls

                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                    if event.key in (K_LSHIFT, K_RSHIFT):
                        # NOTE : 원본대로하면 나중엔 던전에서만 달리게 할것
                        # 쉬프트 누르면 달리기 나중엔 쉬프트 뺄것
                        # 쉬프트 누르고 있으면 계속 유지되게.
                        player_run = True

                    if event.key == K_x:
                        print("x:대화")
                        self.talker = self.player.talk(self)  # Todo: 오류남.
                    elif event.key == K_z:  # Z버튼 클릭시 공격 - 원래는 스페이스임
                        print("z:공격")
                        self.player.state = self.player.STATE_ATACKING
                        if self.player.fightcounter == 0:
                            self.player.fight(self.room, self.player, self.taskbar.sword)
                            self.player.fightcounter = 10
                    elif event.key == K_c:  # c마법시전
                        print("c:마법시전")
                        self.player.cast(self)
                    elif event.key == K_p:
                        print("p:파워?")
                        self.player.deitypower(self)
                    elif event.key == K_i:
                        ###########################
                        # 인벤창 처리
                        # Todo: 마우스에도 계속해서 화면이 갱신된다. 마우스는 안되게 할것
                        ###########################
                        self.charscreenover = False
                        while self.charscreenover == False:
                            sleep(0.01)
                            for event in pygame.event.get():
                                if event.type == QUIT:  # 창닫을때.
                                    print("창닫기 게임이 종료됨")
                                    return
                                elif event.type == KEYDOWN:
                                    self.keydown = 1
                                    print("키보드 눌림")
                                    if event.key == K_ESCAPE or event.key == K_i:
                                        print("I 또는 ESC눌림 인벤토리창 닫기")
                                        self.charscreenover = True

                                # 각종창들갱신
                                self.characterscreen.draw(self)  # 인벤창 갱신
                                self.taskbar.draw(self)  # 작업창 갱신
                                self.bgoverlay.draw(self.screen)  # 배경창 갱신
                                self.meter.draw(self.screen)  # 생명표시줄 갱신
                                pygame.display.update();
                                print("i:인벤토리->열림->ESC또는 I키보드 눌림")
                                ###self.screen.blit(blankimage, (0,0))

                    elif event.key == K_DOWN:
                        self.keydown = 2
                        print("키다운")

                        # FIXME keydown = 2
                        # self.room.moveup()
                    elif event.key == K_RIGHT:
                        self.room.moveright()  # 마을을 이동시키기
                        self.room.direction = "left"
                        self.player.direction = self.player.RIGHT

                        if player_run:
                            self.player.state = self.player.STATE_RUNNING
                        else:
                            self.player.state = self.player.STATE_WALKING

                            # print(self.player.x, self.player.y) #캐릭터는 항상 중앙에 있다. 그래서 바뀌지않음.
                            # print(self.room.relativey, self.room.relativex)

                    elif event.key == K_LEFT:
                        self.room.moveleft()
                        self.room.direction = "right"
                        self.player.direction = self.player.LEFT

                        if player_run:
                            self.player.state = self.player.STATE_RUNNING
                        else:
                            self.player.state = self.player.STATE_WALKING

                            # print self.player.state
                            # self.player.state = self.player.STATE_WALK

                            # print("마을오른쪽이동,플레이어 왼쪽달리기")
                            # print(self.room.relativey, self.room.relativex)
                            # print(self.x,self.y) 이건아니다.

                    elif event.key == K_UP:
                        self.locationtext = self.room.exit(self)
                        print "로케이션텍스트: ", self.locationtext
                        self.chooseroom(self.locationtext, self.font)  # 점프한데가 혹시 문으로 들어가는곳인가?
                        # print"점프 ", self.locationtext #뒤에껀 안찍힌듯

                        ########################################
                        # 점프했는데 로프가있을때 -> 로프를 탐
                        ########################################
                        if self.room.collideropes(self.player):
                            # print "Collision with Rope"
                            print"로프에 접촉"
                            climbingover = 0
                            while climbingover == 0:
                                sleep(0.01)
                                for event in pygame.event.get():
                                    if event.type == QUIT:
                                        return
                                    elif event.type == KEYDOWN:
                                        self.keydown = 1
                                        # self.player 1 key controls
                                        if event.key == K_RIGHT:
                                            self.room.moveright()
                                            self.room.direction = "left"
                                            self.player.direction = self.player.RIGHT
                                            if not self.room.collideropes(self.player):
                                                climbingover = 1
                                        elif event.key == K_LEFT:
                                            self.room.moveleft()
                                            self.room.direction = "right"
                                            self.player.direction = self.player.LEFT
                                            if not self.room.collideropes(self.player):
                                                climbingover = 1
                                        elif event.key == K_UP:
                                            self.room.moveup()
                                            if not self.room.collideropes(self.player):
                                                climbingover = 1
                                        elif event.key == K_DOWN:
                                            self.room.movedown()
                                            if not self.room.collideropes(self.player):
                                                climbingover = 1

                                    self.room.update(self.player)
                                    self.room.draw(self.screen, self.player, self.taskbar)
                                    self.taskbar.draw(self)
                                    self.player.update(self.room)
                                    self.player.drawclimbing(self.screen, self.room)
                                    self.bgoverlay.draw(self.screen)
                                    self.meter.draw(self.screen)

                                    pygame.display.update()
                                    self.screen.blit(blankimage, (0, 0))


                        ########################################
                        # 점프했는데 로프가없을때 -> 그냥점프
                        ########################################
                        ####if self.roomnumber == 0:
                        elif self.room.fall(self.player) == 2:  # 캐릭터가 땅을 밟고있다면..
                            print "점프"
                            self.player.jump(self.room)  # 점프함 #버그: 땅을 안밟아도 점프됨
                            # sys.exit()
                            # sleep(1)

                elif event.type == KEYUP:
                    """
                    키가 떼이면 
                    """
                    self.player.state = self.player.STATE_STANDING  # 그냥 서있는 자세이어야함
                    player_run = False  # 달리기 상태정지

            if self.room.collide(self.player) == 1 or self.player.hitpoints <= 0:
                print "game over!"
                exit

            # ===================================================================
            # 공통사항
            # ===================================================================
            # print "점프", self.player.jumpcounter
            self.room.update(self.player)  # 지금은 아무작동안함
            self.room.fall(self.player)  # 중력상태 유지
            self.room.draw(self.screen, self.player, self.taskbar)

            # NOTE : 마을에서는 계속 상태창을 그리는게 과부하 걸릴수있을듯.
            self.taskbar.draw(self)  # 상태창 그리기
            self.meter.draw(self.screen)  # 생명줄 그리기
            self.player.update(self.room)  # 점프중처리
            self.player.draw(self.screen, self.room)
            self.bgoverlay.draw(self.screen)  # 배경이미지 처리

            pygame.display.update()
            self.screen.blit(blankimage, (0, 0))

    # 지금은 안쓰는듯            
    def setxy(self, xx, yy):
        self.x = xx
        self.y = yy

    # 지금은 안쓰는듯
    def setplayerxy(self, xx, yy):
        self.player.x = xx
        self.player.y = yy

    # 선택된방
    # NOTE: set x y in maproom1 and Game() will set it with game.x (self.x) etc. 
    def chooseroom(self, locationtext, font):
        # self :
        # locationtext :
        # font : no use
        if (self.locationtext == ""):
            return
        # Moon woods
        elif (self.locationtext == "Bosque"):
            # ===================================================================
            # 숲(스페인어) 마을 
            # ===================================================================
            self.talker = None
            self.room = MaproomBosqueVillage(self.x, self.y, 2000, 400)
        elif (self.locationtext == "Cavern of Malicia"):
            # ===================================================================
            # 원한(스페인어)의 동굴 
            # ===================================================================
            self.talker = None
            self.room = MaproomCavernofMalicia(self.x, self.y, 2000, 2000)
        elif (self.locationtext == "The Bank"):
            print "은행"
            if self.roomnumber == 1.1: #TODO : 1.1은 무엇을 의미하는건가?
                # FIXME pack store
                1
            self.room = MaproombankBosque(self.screen, self.player, self.taskbar)


            gameover = False
            while gameover == False:
                self.room.update(self.player)  # 지금은 아무작동안함
                # self.room.fall(self.player)  # 중력상태 유지
                self.room.draw(self.screen, self.player, self.taskbar)

                pygame.display.update()

                sleep(0.01)
                for event in pygame.event.get():
                    if event.type == QUIT:
                        print("무기소종료")
                        return
                    elif event.type == KEYDOWN:
                        self.keydown = 1
                        print("무기소키다운1")
                        # self.player 1 key controls
                        if event.key == K_UP:
                            print("무기소키업")
                            self.room.selectorup()
                        elif event.key == K_DOWN:
                            print("무기소키다운2")
                            self.room.selectordown()
                        elif event.key == K_z:
                            self.adapter = self.room.select(self.room)
                            self.manipulateroom(self.adapter)
                            print("무기소Z키");
                            gameover = True

        elif (self.locationtext == "Weapon and Armour shop"):
            if self.roomnumber == 1.1:
                # FIXME pack store
                1
            self.room = MaproomweaponstoreBosque()
            gameover = False
            while gameover == False:
                sleep(0.01)
                for event in pygame.event.get():
                    if event.type == QUIT:
                        print("무기소종료")
                        return
                    elif event.type == KEYDOWN:
                        self.keydown = 1
                        print("무기소키다운1")
                        # self.player 1 key controls
                        if event.key == K_UP:
                            print("무기소키업")
                            self.room.selectorup()
                        elif event.key == K_DOWN:
                            print("무기소키다운2")
                            self.room.selectordown()
                        elif event.key == K_z:
                            self.adapter = self.room.select(self.room)
                            self.manipulateroom(self.adapter)
                            print("무기소Z키");
                            gameover = True

                self.room.draw(self.screen, self.player, self.taskbar)
                self.taskbar.draw(self)
                self.meter.draw(self.screen)
                pygame.display.update()
        elif (self.locationtext == "The Sage Marid"):
            # ===================================================================
            # 현자의 집
            # ===================================================================
            if self.roomnumber == 1.2:
                # FIXME pack store
                1
            self.room = MaproomfortunetellerBosque()
            gameover = False
            while gameover == False:
                sleep(0.01)
                for event in pygame.event.get():
                    if event.type == QUIT:
                        return
                    elif event.type == KEYDOWN:
                        self.keydown = 1
                        # self.player 1 key controls
                        if event.key == K_UP:
                            self.room.selectorup();
                            print("키업")
                        elif event.key == K_DOWN:
                            self.room.selectordown();
                            print("키다운")
                        elif event.key == K_z:
                            self.adapter = self.room.select(self.room)
                            self.manipulateroom(self.adapter)
                            gameover = True

                self.room.draw(self.screen, self.player, self.taskbar)
                self.taskbar.draw(self)
                self.meter.draw(self.screen)
                pygame.display.update()

    # 메인화면?
    def manipulateroom(self, adapter):
        print("무슨함수?")
        if adapter and adapter.room:
            self.room = adapter.room


# 파일이 인터프리터에 의해서 실행되는 경우라면
if __name__ == "__main__":
    print("인터프리터에서 실행 ")
    foo = Game()
