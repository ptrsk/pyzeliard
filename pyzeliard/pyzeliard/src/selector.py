
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
from widget import *

class Selector(Widget):
    ""
    def __init__(self, xx,yy,ww,hh,hoffset, parent, nselections):
	Widget.__init__(self,xx,yy,ww,hh,parent)
	self.image = pygame.image.load('./pics/selector.png').convert()
	self.image.set_colorkey((0,0,0))
	self.nselections = nselections
	self.selectnumber = 0
	self.hoffset = hoffset

    def draw(self, screen, room):
	screen.blit(self.image, (self.x, self.y))

    def moveup(self):
	if self.selectnumber <= 0:
		self.selectnumber = 0
		return
	else:
		self.selectnumber -= 1
		self.y -= self.hoffset

    def movedown(self):
	if self.selectnumber < self.nselections:
		self.selectnumber += 1
		self.y += self.hoffset

    def select(self, widgettree):
	return widgettree.enter(self)
