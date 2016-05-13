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
from gameobject import *

class Exit(Gameobject):
    "Exit"
    
    # xx :
    # yy :
    # ww :
    # hh :
    # xoffset :
    # ypffset :
    # roomnumber :
    # locationtext : 위치
    def __init__(self, xx,yy,ww,hh,xoffset,yoffset,roomnumber,locationtext):
        Gameobject.__init__(self,xx,yy)
        self.w = ww
        self.h = hh
        self.hitpoints = 100000000 #FIX else wall/floor disappears

        ### sets x and y in next room
        self.xoffset = xoffset
        self.yoffset = yoffset
        
        self.roomnumber = roomnumber
        self.locationtext = locationtext

    def draw(self, screen, room):
        pass

    def exitp(self, game):
	if (game.player.x > self.x + game.room.relativex and
	 	game.player.x < self.x + game.room.relativex + self.w and
		game.player.y > self.y + game.room.relativey and
		game.player.y < self.y + game.room.relativey + self.h):
		return 1
	return 0
