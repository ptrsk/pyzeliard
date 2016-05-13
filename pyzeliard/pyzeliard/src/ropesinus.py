
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
from ropesinusbase import *

class RopeSinus(RopeSinusBase):
    "Rope class"
    def __init__(self,x1,y1,x2,y2,theta,dtheta,dy):
	RopeSinusBase.__init__(self,x1,y1,x2,y2,theta,dtheta,dy)

    def climb(self, player):
	if self.getimp().attop(player) or self.getimp().atbottom(player):
		return	
	else:
		player.climb(self)	

    ### The rope pulls up
#    def raise(self, player):
#	pass	

    ### The rope falls down
    def lower(self, player):
	self.getimp().lower(player)	
