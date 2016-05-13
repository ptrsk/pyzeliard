
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
from maproomweaponstore import *
from widgetbox import *
from labelxoffset import *
from selector import *
from maproombosquevillage import *
from maproomadapter import *

class MaproomweaponstoreBosque(Maproomweaponstore):
    "Store"
    def __init__(self):
	Maproomweaponstore.__init__(self)	
	self.roomnumber = 1.1

	self.font = pygame.font.SysFont("Vera", 16)
	box = WidgetBox(340,50,160,90,self.widgettree.widgetroot)

	label1 = Labelxoffset(340,50,100,14,self.font,"Go outside",box,24)
	label2 = Labelxoffset(340,70,100,14,self.font,"Buy weapon",box,24)
	label3 = Labelxoffset(340,90,100,14,self.font,"Buy shield",box,24)
	box.addchild(label1)
	label1.setcallback(self.gooutside)
	box.addchild(label2)
	box.addchild(label3)
	self.selector = Selector(340,40,32,32,21,box,2)
	box.addchild(self.selector)

	self.widgettree.addchild(box)

    def gooutside(self, room):
	return Maproomadapter(MaproomBosqueVillage(-588,0,2000,400))  ### NOTE : go to room 1 
	
    def selectorup(self):
	self.selector.moveup()	

    def selectordown(self):
	self.selector.movedown()	

    def select(self, room):
	w = self.selector.select(self.widgettree)
	print "++++++++++++++++%s" % w
	if w and w.callback:
		return w.callback(room)

    def fight(self, player):
	pass	
