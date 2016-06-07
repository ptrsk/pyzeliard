# -*- coding: UTF-8 -*-
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
from maproomstore import *
import color
class Maproombank(Maproomstore):
    """
        Store
        은행 공통사항 - 여기서는 화면출력은 하지않는듯.
    """
    def __init__(self):
        Maproomstore.__init__(self)
        self.bgimage = pygame.image.load('./pics/bg-bank-1.png') # 은행원 얼굴
        self.locationtext = "The Bank"
        self.roomnumber = 1.3

        animTypes = 'work_write'.split()  # 현재 존재하는 그림만 추가할것
        self.animObjs = {}

        for animType in animTypes:
            imagesAndDurations = [('./images/bank/banker_%s_%s.bmp' % (animType, str(num).rjust(3, '0')), 0.09) for num in
                                  range(6)]
            self.animObjs[animType] = pyganim.PygAnimation(imagesAndDurations)  # 이미지 불러오기

    #def draw(self, screen, player, taskbar):
        """
            overriding
        """
        #self.animObjs['work_write'].blit(screen, (self.x, self.y))

        #pygame.draw.rect(screen, color.Colors.WHITE, (120, 100, 640, 300))


    def fight(self, player):
        """
            overriding
        """
        pass
