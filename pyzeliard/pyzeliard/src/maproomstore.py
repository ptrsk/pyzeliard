
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
from widgettree import *

class Maproomstore(Maproombase):
    "Store"
    def __init__(self):
	Maproombase.__init__(self,0,0,640,400)	
	self.widgettree = Widgettree()

    def fight(self, player):
	pass	

    def draw(self, screen, room,taskbar):
	Maproombase.draw(self,screen,room,taskbar)
	self.widgettree.draw(screen, room)
