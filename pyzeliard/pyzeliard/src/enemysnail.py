
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
from enemywithdirection import *
from stateimagelibrary import *

class Enemysnail(Enemywithdirection):
    "enemy"
    def __init__(self, xx,yy):
        Enemywithdirection.__init__(self,xx,yy,48,48)
        self.hitpoints = 1 

	self.stimlibleft = Stateimagelibrary()
	self.stimlibright = Stateimagelibrary()
	image = pygame.image.load('./pics/snail-left-48x48-1.png').convert()
	image.set_colorkey((0,0,0))
	self.stimlibleft.addpicture(image)
	image = pygame.image.load('./pics/snail-right-48x48-1.png').convert()
	image.set_colorkey((0,0,0))
	self.stimlibright.addpicture(image)

	self.direction = self.LEFT

    def draw(self, screen, room):
	if self.direction == self.LEFT:
		self.stimlibleft.draw(screen, self.x+room.relativex, self.y+room.relativey)
	elif self.direction == self.RIGHT:
		self.stimlibright.draw(screen, self.x+room.relativex, self.y+room.relativey)

    def update(self, room, player):
   	self.x -= 1 
