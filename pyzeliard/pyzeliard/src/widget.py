
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
from widgetbase import *

class Widget(WidgetBase):
    ""
    def __init__(self, xx,yy,ww,hh, parent):
	WidgetBase.__init__(self,xx,yy,ww,hh,parent)
	self.callback = None
	self.r = None

    def enter(self, selector):
	###print "---%s" % self

	self.enterrec(selector)
	print "***********%s" % self.r
	return self.r
	
    def enterrec(self, selector):
	###print "---%s" % self
	if self.collide(selector.x, selector.y) != selector:
		###print "**collide and self.children=%s" % len(self.children)
		if len(self.children) == 0:
			if self.r == None: 
				self.r = self
				###print "---------------------->set return val = %s" % self.r
					
		else:
			for w in self.children:
				w.enterrec(selector)	
	
    def setcallback(self, callback):
	self.callback = callback
