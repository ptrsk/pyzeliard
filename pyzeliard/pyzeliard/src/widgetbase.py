
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

class WidgetBase:
    ""
    def __init__(self, xx,yy,ww,hh, parent):
	self.x = xx
	self.y = yy
	self.w = ww
	self.h = hh

	self.parent = parent
	self.children = []

	self.yoffset = 10

    def addchild(self, widget):
	self.children.append(widget)

    def draw(self, screen, room):
	for w in self.children:
		w.draw(screen,room)

    def collide(self, xx, yy):
	#####print "selectorx=%d selectory=%d widgetx=%d widgety=%d widgetw=%d widgeth=%d" % (xx,yy+self.yoffset,self.x,self.y,self.w,self.h)
	print "selectorx=%d selectory=%d widgetx=%d widgety=%d widgetyw=%d widgetyh=%d" % (xx,yy+self.yoffset,self.x,self.y,self.x+self.w,self.y+self.h)
	if (xx >= self.x and xx <= self.x + self.w and
	yy+self.yoffset >= self.y and yy+self.yoffset <= self.y + self.h):
		print "***collide!"
		return self 
	return None 
