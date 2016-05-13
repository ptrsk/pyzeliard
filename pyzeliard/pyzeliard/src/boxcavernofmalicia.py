
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
from box import *
from tilemap import *

class BoxCavernOfMalicia(Box):
    ""
    def __init__(self, xx,yy,ww,hh):
        Box.__init__(self,xx,yy,ww,hh)
	self.toptileimage = pygame.image.load('./pics/tile-cavernmalicia-1.png').convert()
	self.toptileimage.set_colorkey((0,0,0))
	self.commontileimage = pygame.image.load('./pics/tile-cavernmalicia-2.png').convert()
	self.commontileimage.set_colorkey((0,0,0))

	self.tilemap = Tilemap(self)

    def gettopimage(self):
	return self.toptileimage

    def getimage(self):
	return self.commontileimage

    def draw(self, screen, room):
	self.tilemap.draw(screen,room)

    def collide(self, room, player):
	if (player.x-room.relativex >= self.x and
	player.x-room.relativex <= self.x+self.w and
	player.y-room.relativey-player.h >= self.y and
	player.y-room.relativey <= self.y+self.h):
		return 2
	return 0	
