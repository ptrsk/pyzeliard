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

class TitleScreenC:
    
    def __init__(self):
        #pygame.init()
        
        print("타이틀 찍기")
        gameover = 0  # 게임종료여부 -- 0:게임 안끊남. 1: 끝남
        
        self.screen = pygame.display.set_mode((640, 400))
        titleimage = pygame.image.load('./pics/titlescreen.png').convert()  # 로고 화면
        # 로고화면띄우기
        while gameover == 0:
            pygame.display.update()
            self.screen.blit(titleimage, (0, 0))
            sleep(0.01)
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == KEYDOWN:
                    gameover = 1
                if event.type == pygame.MOUSEBUTTONDOWN:
                    gameover = 1

                    print("화면찍음")