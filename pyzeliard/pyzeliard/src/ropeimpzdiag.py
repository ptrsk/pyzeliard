
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
from ropeimp import *
import math

class RopeImpzDiag(RopeImp):
    "Rope Bridge"
    def __init__(self,x1,y1,x2,y2,imagefilename,r,g,b):
       	RopeImp.__init__(self,imagefilename,r,g,b,abs(x2-x1),abs(y2-y1))

	self.x1 = x1
	self.y1 = y1
	self.x2 = x2
	self.y2 = y2
