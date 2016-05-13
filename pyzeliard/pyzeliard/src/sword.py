
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
from rng import *

class Sword:
    "Sword"
    def __init__(self, imagefilename, r,g,b, xx,yy,ww,hh,typetext):
        self.image = pygame.image.load(imagefilename).convert()
        self.image.set_colorkey((r,g,b))
	self.x = xx
	self.y = yy
	self.w = ww
	self.h = hh
	self.typetext = typetext
	self.rng = RNG(self)

    def draw(self, screen):
	pass

    def roll(self):
	return self.rng.rolld4()
