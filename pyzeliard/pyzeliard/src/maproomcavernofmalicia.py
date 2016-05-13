
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
from maproomdungeon import *
from box import *
from enemysnail import *
from boxcavernofmalicia import *
from ropez import *
from ropeellips import *
from ropesinus import *

class MaproomCavernofMalicia(Maproomdungeon):
    "Dungeon"
    def __init__(self, xx,yy,ww,hh):
	Maproomdungeon.__init__(self,xx,yy,ww,hh)	
	self.bgimage = pygame.image.load('./pics/bg-cavern-of-malicia-1.png')
	self.locationtext = "Cavern of Malicia"
	self.roomnumber = 2
    	####self.gameobjects.append(Box(0,300,2000,120))
    	self.gameobjects.append(BoxCavernOfMalicia(0,300,2000,120))

	self.gameobjects.append(Enemysnail(500,207-60))

	###self.ropes.append(Ropez(300,200,100))
	self.ropes.append(Ropez(900,150,100))
	####self.ropes.append(RopeEllips(3,2,1,1,1))
	self.ropes.append(RopeSinus(700,100,800,100,0.1,0.01,100))
