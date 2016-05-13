
# Copyright (C) Johan Ceuppens 2015
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
from random import *

#### NOTE : override (e.g. in file ropieimpz.py)

class RopeImp:
    "Rope Bridge"
    def __init__(self, ropepieceimagefilename, r,g,b,w,h):
       	self.imagepiece = pygame.image.load(ropepieceimagefilename).convert()
	self.imagepiece.set_colorkey((r,g,b))
	self.imagepiecew = w
	self.imagepieceh = h

    def getimp(self):
	return self

    def attop(self, player):
	if player.attop():
		player.setropetop(self)
 
    def atbottom(self, player):
	if player.atbottom():
		player.setropebottom(self)

