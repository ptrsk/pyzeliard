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

import pygame
from pygame.locals import *
#import random
from time import *

class ScreenOpenningC:
    
    def __init__(self):
                
        gameover = 0  # �������Ῡ�� -- 0:���� �Ȳ���. 1: ����
        
        self.screen = pygame.display.set_mode((640, 400))
        border = pygame.image.load('./pics/openning/image 281.png').convert()  # �ΰ� ȭ��
        
        animation = pygame.image.load('./pics/openning/image 297.bmp').convert()  # �ΰ� ȭ��
        
        
        fontName = "Courier"
        fontColor = (255,255,255)# RGB
        fontBold = True #����
        #fontItalic = True #�����
        fontItalic= False
        fontSize= 20  #��Ʈ ũ��
        offset_height=100   #��Ʈ ����

        text1= "Once, long ago, a terrible storm came to the land of Zeliard."
        text2= "Dark clouds filled the sky; lightning flashed and thunder crashed."
        text3= "Day after day, rain poured from the heavens as if in lament."
        text4= ""
        text5= "On the seventh day of rain, a beautiful young girl stood on her balcony watching this dark, sad rain."
        text6= "The girl was Princess Felicia la Felishika. She was the only daughter of King Felishika, and the light of his life."
        text7= ""

        text8= "Her smiles were like sunshine, her voice as beautiful as that of an angel. She was adored by the people of the kingdom."
        text9= ""

        text10= 'What a dreadful storm! Will it never end?"'
        text11= ""

        text12= "Just as the princess spoke these words, the raindrops turned to grains of sand which covered the ground below her."
        # �ΰ�ȭ�����
        while gameover == 0:
            pygame.display.update()
            self.screen.blit(border, (0, 0))
            self.screen.blit(animation, (30, 30)) # 640*400 �϶� �������� �����ҵ���.
            
            #�������
            sleep(0.01)
            for event in pygame.event.get():
                if event.type == QUIT:
                    #return
                    print(1)
                elif event.type == KEYDOWN:
                    gameover = 1
                if event.type == pygame.MOUSEBUTTONDOWN:
                    gameover = 1

                    print("ȭ������")