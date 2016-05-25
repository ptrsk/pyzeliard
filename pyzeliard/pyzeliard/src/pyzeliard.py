# -*- coding: cp949 -*-
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
        self.screen = pygame.display.set_mode((640, 400)) #������ ũ�� ���� 
        #self.screen = pygame.display.set_mode((640, 400), 0, 32) #������ ũ�� ����
        #self.screen = pygame.display.set_mode((800, 600)) #������ ũ�� ����
        # 1) ȭ�� �ػ󵵸� 480*320���� �ʱ�ȭ. ������ ���, ���� ���� ���� �ʱ�ȭ�ϴ� ���
        #self.screen = pygame.display.set_mode((480, 320), DOUBLEBUF)
        
        # 2) ȭ�� �ػ󵵸� 480*320, ��ü ȭ�� ���, �ϵ���� ���� ���, ���� ���� ���� �ʱ�ȭ�ϴ� ���
        #self.screen = pygame.display.set_mode((480, 320), FULLSCREEN | HWSURFACE | DOUBLEBUF)

        pygame.display.set_caption('Zeliard') #window title
        
        self.font = pygame.font.SysFont("Times", 14) # Ÿ�� ��Ʈ
        self.font2 = pygame.font.SysFont("Coutier", 28) #�ڿ�Ƽ�� ��Ʈ
        self.font3 = pygame.font.SysFont("Vera", 52) #���� ��Ʈ
        blankimage = pygame.image.load('./pics/blank.png').convert() #����ȭ��
        titleimage = pygame.image.load('./pics/titlescreen.png').convert() # �ΰ� ȭ�� 
        gameover = False # �������Ῡ�� -- 0:���� �Ȳ���. 1: ����
        
        """
        run logo
        �ΰ�ȭ�����
        """
        #print("�ΰ�ȭ��")
        while gameover == False:
            pygame.display.update()#ȭ�鰻��
            self.screen.blit(titleimage, (0,0)) #�ΰ�ȭ�� ���
            sleep(0.01)
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == KEYDOWN:
                    gameover = True # �����Ѿ��
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    gameover = True # �����Ѿ��

        """
        initialize game
        ���� ���� �ʱ�ȭ 
        """
        
        #print("��������ȭ��")
        self.meter = Meter() #������ ����
        pygame.key.set_repeat(10,100) #??? (����, ����)
        ####pygame.key.set_repeat(1000,1000)

        ## offsets for room changing
        self.x = 0 #����ġ 
        self.y = 0

        #self.player = Player(280,252)# �÷��̾� ��ġ (X��, Y��) --ȭ�� �߾ӿ��� �󸶳� ġ���������� Ȯ�� ȭ���߾ӿ��� �־���
        self.player = Player(280,236)# �÷��̾� ��ġ (X��, Y��) --ȭ�� �߾ӿ��� �󸶳� ġ���������� Ȯ�� ȭ���߾ӿ��� �־���
        #self.player = Player(280,199) #-- �̰� ������

        # ���� �ε�
        self.room = MaproomBosqueVillage(-700,0,3312,288) #����� ����ũ���� ��� x��, y��, ����ũ��, ����ũ��
        #self.room = MaproomBosqueVillage(-700,0,2000,400) #����� ����ũ���� ���
        ###self.room = MaproomCavernofMalicia(0,0,2000,400)
        ###self.room = MaproomweaponstoreBosque()
        ###self.room = MaproomfortunetellerBosque()
        ###self.room = MaproombankBosque()


        self.locationtext = self.room.locationtext # ���̸� �Է�
        self.roomnumber = self.room.roomnumber #���ȣ �Է� 
 
        self.bgoverlay = BGOverlay(0,0) # ������ ����
        self.taskbar = Taskbar(self.screen, self.font2, self.player) # �۾�ǥ���� ���̱�. screen, font, player
        self.characterscreen = CharacterScreen(self.font) # �κ��丮â

        #gameflag = 0 # �Ⱦ���. �ƹ����� gameover�� ��Ÿ�ε�.

        #print("���α׷� ����")
        #os.system("pause")
        #sys.exit()

        ######################
        # ���� ���� : ����
        ######################        
        gameover = False # �������Ῡ�� -- 0: ������ 1: ����
        while gameover == False:
            self.player.h = 72 # NOTE: for ducking, FIXME 48
            sleep(0.01)
            
            for event in pygame.event.get():
                if event.type == QUIT: # X��ư
                    print("x:����")
                    return
                elif event.type == KEYDOWN:
                    #print("Ű����")
                    self.keydown = 1
                    # self.player 1 key controls
                    
                    if event.key == K_x:
                        print("x:��ȭ")
                        self.talker = self.player.talk(self) # Todo: ������.
                    elif event.key == K_z: #Z��ư Ŭ���� ����
                        print("z:����")
                        if self.player.fightcounter == 0:
                            self.player.fight(self.room,self.player,self.taskbar.sword)
                            self.player.fightcounter = 10
                    elif event.key == K_c: #c��������
                        print("c:��������")
                        self.player.cast(self)
                    elif event.key == K_p:
                        print("p:�Ŀ�?")
                        self.player.deitypower(self)
                    elif event.key == K_i:
                        ###########################
                        # �κ�â ó��
                        # Todo: ���콺���� ����ؼ� ȭ���� ���ŵȴ�. ���콺�� �ȵǰ� �Ұ�
                        ###########################
                        self.charscreenover = False
                        while self.charscreenover == False:
                            sleep(0.01)
                            for event in pygame.event.get():
                                if event.type == QUIT: # â������.
                                    print("â�ݱ� ������ �����")
                                    return
                                elif event.type == KEYDOWN:
                                    self.keydown = 1
                                    print("Ű���� ����")
                                    if event.key == K_ESCAPE or event.key == K_i:
                                        print("I �Ǵ� ESC���� �κ��丮â �ݱ�")
                                        self.charscreenover = True
                                        
                                #����â�鰻��
                                self.characterscreen.draw(self) #�κ�â ����
                                self.taskbar.draw(self) #�۾�â ����
                                self.bgoverlay.draw(self.screen) #���â ����
                                self.meter.draw(self.screen) #����ǥ���� ����
                                pygame.display.update();
                                print("i:�κ��丮->����->ESC�Ǵ� IŰ���� ����")
                                ###self.screen.blit(blankimage, (0,0))

                    elif event.key == K_DOWN:
                        self.keydown = 2
                        print("Ű�ٿ�")

                        #FIXME keydown = 2
                        #self.room.moveup()    
                    elif event.key == K_RIGHT:
                        self.room.moveright() # ������ �̵���Ű��
                        self.room.direction = "left"
                        self.player.direction = self.player.RIGHT 
                        self.player.state = self.player.STATE_WALK
                        
                        ##print("���� �����̵�,�÷��̾� �����ʴ޸���")
                        #print(self.player.x, self.player.y) #ĳ���ʹ� �׻� �߾ӿ� �ִ�. �׷��� �ٲ�������.
                        #print(self.room.relativey, self.room.relativex)
                        
                    elif event.key == K_LEFT:
                        self.room.moveleft()
                        self.room.direction = "right"
                        self.player.direction = self.player.LEFT
                        self.player.state = self.player.STATE_WALK
                         
                        #print("�����������̵�,�÷��̾� ���ʴ޸���")
                        #print(self.room.relativey, self.room.relativex)
                        #print(self.x,self.y) �̰Ǿƴϴ�.
                         
                    elif event.key == K_UP:
                        self.locationtext = self.room.exit(self)
                        self.chooseroom(self.locationtext, self.font) #�����ѵ��� Ȥ�� ������ ���°��ΰ�?
                        #print"���� ", self.locationtext #�ڿ��� ��������

                        ########################################
                        # �����ߴµ� ������������ -> ������ Ž
                        ########################################
                        if self.room.collideropes(self.player):
                                #print "Collision with Rope"
                                print"������ ����"
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
                                        self.room.draw(self.screen,self.player,self.taskbar)
                                        self.taskbar.draw(self)
                                        self.player.update(self.room)
                                        self.player.drawclimbing(self.screen,self.room)
                                        self.bgoverlay.draw(self.screen)
                                        self.meter.draw(self.screen)

                                        pygame.display.update()
                                        self.screen.blit(blankimage, (0,0))
                                        

                        ########################################
                        # �����ߴµ� ������������ -> �׳�����
                        ########################################
                        ####if self.roomnumber == 0:
                        elif self.room.fall(self.player) == 2: #ĳ���Ͱ� ���� ����ִٸ�..
                            print "����"                            
                            self.player.jump(self.room) # ������ #����: ���� �ȹ�Ƶ� ������
                            #sys.exit()
                            #sleep(1)

                elif event.type == KEYUP:
                    """
                    Ű�� ���̸� �׳� ���ִ� �ڼ��̾����
                    """
                    self.player.state = self.player.STATE_STAND

            if self.room.collide(self.player) == 1 or self.player.hitpoints <= 0:
                print "game over!"
                exit
            
            #===================================================================
            # �������
            #===================================================================
            #print "����", self.player.jumpcounter
            self.room.update(self.player) # ������ �ƹ��۵�����
            self.room.fall(self.player) # �߷»��� ����
            self.room.draw(self.screen,self.player,self.taskbar)
            self.taskbar.draw(self) #����â �׸���
            self.meter.draw(self.screen) # ������ �׸���
            self.player.update(self.room) # ������ó��
            self.player.draw(self.screen,self.room)
            self.bgoverlay.draw(self.screen) # ����̹��� ó��
            
            pygame.display.update()
            self.screen.blit(blankimage, (0,0))
            #print "����" , self.player.state


    # ������ �Ⱦ��µ�            
    def setxy(self,xx,yy):
        self.x = xx
        self.y = yy

    # ������ �Ⱦ��µ�
    def setplayerxy(self,xx,yy):
        self.player.x = xx
        self.player.y = yy

    # ���õȹ�
    # NOTE: set x y in maproom1 and Game() will set it with game.x (self.x) etc. 
    def chooseroom(self, locationtext, font):
        if (self.locationtext == ""):
            return
        # Moon woods
        elif (self.locationtext == "Bosque"):
            #===================================================================
            # ��(�����ξ�) ���� 
            #===================================================================
            self.talker = None
            self.room = MaproomBosqueVillage(self.x,self.y,2000,400)
        elif (self.locationtext == "Cavern of Malicia"):
            #===================================================================
            # ����(�����ξ�)�� ���� 
            #===================================================================
            self.talker = None
            self.room = MaproomCavernofMalicia(self.x,self.y,2000,2000)
        elif (self.locationtext == "Weapon and Armour shop"):
            #===================================================================
            # �������ۼ� ���� 
            #===================================================================
            if self.roomnumber == 1.1:
                # FIXME pack store
                1
            self.room = MaproomweaponstoreBosque()
            print("�������ۼ�")
            
            gameover = False
            while gameover == False:
                sleep(0.01)
                for event in pygame.event.get():
                    if event.type == QUIT:
                        print("���������")
                        return
                    elif event.type == KEYDOWN:
                        self.keydown = 1
                        print("�����Ű�ٿ�1")
                        # self.player 1 key controls
                        if event.key == K_UP:
                            print("�����Ű��")
                            self.room.selectorup()
                        elif event.key == K_DOWN:
                            print("�����Ű�ٿ�2")
                            self.room.selectordown()
                        elif event.key == K_z:
                            self.adapter = self.room.select(self.room)
                            self.manipulateroom(self.adapter)
                            print("�����ZŰ"); 
                            gameover = True

                self.room.draw(self.screen,self.player,self.taskbar)
                self.taskbar.draw(self)
                self.meter.draw(self.screen)
                pygame.display.update()
        elif (self.locationtext == "The Sage Marid"):
            #===================================================================
            # ������ ��
            #===================================================================
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
                            print("Ű��")
                        elif event.key == K_DOWN:
                            self.room.selectordown(); 
                            print("Ű�ٿ�")	
                        elif event.key == K_z:
                            self.adapter = self.room.select(self.room)
                            self.manipulateroom(self.adapter)
                            gameover = True

                self.room.draw(self.screen,self.player,self.taskbar)
                self.taskbar.draw(self)
                self.meter.draw(self.screen)
                pygame.display.update()

    # ����ȭ��?
    def manipulateroom(self, adapter):
        print("�����Լ�?")
        if adapter and adapter.room:
            self.room = adapter.room

# ������ ���������Ϳ� ���ؼ� ����Ǵ� �����
if __name__ == "__main__":
    print("���������Ϳ��� ���� ")
    foo = Game()
