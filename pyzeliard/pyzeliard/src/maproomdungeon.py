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
from maproombase import *

class Maproomdungeon(Maproombase): # 상속받음 Maproombase
    "Dungeon"
    def __init__(self, xx,yy,ww,hh): #생성자
	Maproombase.__init__(self,xx,yy,ww,hh)	

    def fight(self, player):
	for go in self.gameobjects:
        	if (player.x-self.relativex >= go.x  and 
		player.x-self.relativex <= go.x+go.w and 
		player.y+player.h-self.relativey >= go.y+go.h and #FIXED +go.h
		player.y-self.relativey <= go.y):
			go.hitwithplayer(player)
			if go.hitpoints <= 0:
				self.gameojects.remove(go)	
			return go 
	return None


    def update(self, player):
	for go in self.gameobjects:
		go.update(self, player) 
