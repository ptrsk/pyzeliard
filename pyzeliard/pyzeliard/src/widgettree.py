
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

class Widgettree:
    ""
    def __init__(self):
	self.widgetroot = Widget(-1,-1,-1,-1,None) 

    def addchild(self, widget):
	self.widgetroot.addchild(widget)	

    def draw(self, screen, room):
	for w in self.widgetroot.children:
		w.draw(screen,room)

    def enter(self, selector):
	for w in self.widgetroot.children:
		if w.collide(selector.x, selector.y):
			####if len(w.children) > 0:
			return w.enter(selector)
	return None	
