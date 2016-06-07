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

# 전면에 보이는 벽 배경
class BGOverlay:
    ""
    def __init__(self, xx,yy):
        	self.x = xx # no use
        	self.y = yy # no use

        	self.middleimage = pygame.image.load('./pics/statue-middle.png').convert()
        	self.middleimage.set_colorkey((255,255,255)) 
        	self.leftimage = pygame.image.load('./pics/statue-left.png').convert()
        	self.leftimage.set_colorkey((255,255,255)) 
        	self.rightimage = pygame.image.load('./pics/statue-right.png').convert()
        	self.rightimage.set_colorkey((255,255,255)) 

    def draw(self, screen):
		screen.blit(self.middleimage, (95,0))	
		screen.blit(self.leftimage, (0,0))	
		screen.blit(self.rightimage, (545,0))	
