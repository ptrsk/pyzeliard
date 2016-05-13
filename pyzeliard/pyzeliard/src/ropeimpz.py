
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
from ropeimp import *

### NOTE : a rope with a height

class RopeImpz(RopeImp):
    "Rope Bridge"
    def __init__(self,xx,yy,hh,imagefilename,r,g,b,w,h):
       	RopeImp.__init__(self,imagefilename,r,g,b,w,h)

	self.x = xx
	self.y = yy
	self.h = hh
	self.w = 10 

    def transform(self, room):
	self.x += room.relativex
	self.y += room.relativey

    def transformback(self, room):
	self.x -= room.relativex
	self.y -= room.relativey

    def drawon(self, screen, room):
	for i in range(0,self.h/self.imagepieceh):
		screen.blit(self.imagepiece,(self.x+room.relativex, self.y+room.relativey+self.imagepieceh*i))
