# -*- coding: cp949 -*-
# Copyright (C) Johan Ceuppens 2015
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

class GreenHeart:
	def __init__(self):
        	self.greenimage = pygame.image.load('./pics/meterpiece-green-1x8.png').convert()
        	self.greenimage.set_colorkey((0,0,0))
		
class RedHeart:
	def __init__(self):
        	self.redimage = pygame.image.load('./pics/meterpiece-red-1x8.png').convert()
        	self.redimage.set_colorkey((0,0,0))
		
# 생명표시줄
class Meter:
    "life meter"
    def __init__(self):
	self.max = 1200 
	self.index = 900
	self.greenhearts = []
	self.redhearts = []
	for i in range(0,3):
		self.greenhearts.append(GreenHeart())
	for i in range(0,3):
		self.redhearts.append(RedHeart())
 
    def draw(self,screen):
	# KLUDGY
	j = 0
	for i in range(0,self.max/30):
        	screen.blit(self.redhearts[0].redimage, (169+j, 330))
		j += 1
	j = 0
	for i in range(0,self.index/30):
        	screen.blit(self.greenhearts[0].greenimage, (169+j, 329))
		j += 1
	
	# TODO: 멈춰있으면 자동회복되어야한다.
	def update(self):
		1