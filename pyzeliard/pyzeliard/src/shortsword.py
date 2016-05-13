
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
from sword import *

class ShortSword(Sword):
    "Short Sword"
    def __init__(self, xx,yy,ww,hh):
	Sword.__init__(self, './pics/sword1-40x38.png',255,0,255, xx, yy, ww, hh, "short sword")

    def draw(self, screen):
	screen.blit(self.image, xx, yy)

    def roll(self, player):
	return self.rng.rolld4()
